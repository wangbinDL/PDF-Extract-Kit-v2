import json
import os
from collections import defaultdict
from utils.extract import md_tex_filter
from utils.match import match_gt2pred, match_gt2pred_textblock, formula_format
from utils.read_files import read_md_file
from registry.registry import DATASET_REGISTRY

@DATASET_REGISTRY.register("end2end_dataset")
class End2EndDataset():
    def __init__(self, cfg_task):
        gt_path = cfg_task['dataset']['ground_truth']['data_path']
        pred_folder = cfg_task['dataset']['prediction']['data_path']
        with open(gt_path, 'r') as f:
            gt_samples = json.load(f)

        self.samples = self.get_matched_elements(gt_samples, pred_folder)
        # self.samples_dict = {}
        # for item in self.samples:
        #     self.samples_dict[os.path.basename(item["page_info"]["image_path"])] = item

    def __getitem__(self, cat_name, idx):
        return self.samples[cat_name][idx]
    
    # def get_with_image_name(self, image_name):
    #     return self.samples_dict[image_name]
    
    def get_page_elements(self, selected_annos):
        saved_element_dict = defaultdict(list)
        for item in selected_annos['layout_dets']:
            saved_element_dict[item["category_type"]].append(item)
        return saved_element_dict

    def get_sorted_text_list(self, selected_annos, txt_type):
        # txt_type: text, latex, html
        text_list = []
        for item in selected_annos:
            if item.get('order'):
                order = item['order']
            else:
                order = 0
            if item.get(txt_type):
                txt = item[txt_type]
            else:
                txt = ""
                print(f'Cannot find GT text for {item}')
            text_list.append((order, txt))
        sorted_text_list = sorted(text_list, key=lambda x: x[0])
        return [_[1] for _ in sorted_text_list]
    
    def get_matched_elements(self, gt_samples, pred_folder):
        plain_text_match = []
        inline_formula_match = []
        title_match = []
        display_formula_match = []
        table_match = []

        for sample in gt_samples:
            img_name = os.path.basename(sample["page_info"]["image_path"])
            
            # # test english content only
            # if img_name.startswith('yanbao') or img_name.startswith('jiaocai_2013_AMC_12A.pdf_9'):
            #     continue

            # print('Process: ', img_name)
            pred_content = read_md_file(os.path.join(pred_folder, img_name[:-4] + '.md'))
            pred_text_list, pred_display_list, pred_table_list, pred_title_list = md_tex_filter(pred_content)
            # print('pred_text_list: ', pred_text_list)
            # print('pred_display_list: ', pred_display_list)
            # print('pred_table_list', pred_table_list)
            # print('pred_title_list: ', pred_title_list)

            gt_page_elements = self.get_page_elements(sample)
            # print('gt_page_elements: ', gt_page_elements.keys())

            if gt_page_elements.get('text_block'):
                gt_text_list = self.get_sorted_text_list(gt_page_elements['text_block'], 'text')
                # print('gt_text_list: ', gt_text_list)
                plain_text_match_s, inline_formula_match_s = match_gt2pred_textblock(gt_text_list, pred_text_list)
                # print('plain_text_match_s: ', plain_text_match_s)
                # print('-'*10)
                # print('inline_formula_match_s', inline_formula_match_s)
                # print('-'*10)
                plain_text_match.extend(plain_text_match_s)

                formated_inline_formula = formula_format(inline_formula_match_s, img_name)
                inline_formula_match.extend(formated_inline_formula)
                # print('inline_formula_match_s: ', inline_formula_match_s)
                # print('-'*10)
                
            if gt_page_elements.get('title'):
                gt_title_list = self.get_sorted_text_list(gt_page_elements['title'], 'text')
                # print('gt_title_list: ', gt_title_list)
                title_match_s = match_gt2pred(gt_title_list, pred_title_list, 'text')
                title_match.extend(title_match_s)
                # print('title_match_s: ', title_match_s)
                # print('-'*10)
            if gt_page_elements.get('isolated_formula'):
                gt_display_list = self.get_sorted_text_list(gt_page_elements['isolated_formula'], 'latex')
                # print('gt_display_list: ', gt_display_list)
                display_formula_match_s = match_gt2pred(gt_display_list, pred_display_list, 'formula')
                formated_display_formula = formula_format(display_formula_match_s, img_name)
                # print('display_formula_match_s: ', display_formula_match_s)
                # print('-'*10)
                display_formula_match.extend(formated_display_formula)
            if gt_page_elements.get('table'):
                gt_table_list = self.get_sorted_text_list(gt_page_elements['table'], 'html')
                # print('gt_table_list', gt_table_list)
                table_match_s = match_gt2pred(gt_table_list, pred_table_list, 'table')
                # print('table_match_s: ', table_match_s)
                # print('-'*10)
                table_match.extend(table_match_s)

        
        matched_samples_all = {
            'text_block': DATASET_REGISTRY.get('recogition_end2end_base_dataset')(plain_text_match),
            'title': DATASET_REGISTRY.get('recogition_end2end_base_dataset')(title_match), 
            'inline_formula': DATASET_REGISTRY.get('recogition_end2end_formula_dataset')(inline_formula_match), 
            'display_formula':  DATASET_REGISTRY.get('recogition_end2end_formula_dataset')(display_formula_match), 
            'table': DATASET_REGISTRY.get('recogition_end2end_table_dataset')(table_match)
        }
        
        return matched_samples_all
    
    