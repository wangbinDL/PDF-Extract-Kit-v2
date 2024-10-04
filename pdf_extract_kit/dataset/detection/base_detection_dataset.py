# Ultralytics YOLO 🚀, AGPL-3.0 license

import os
from pathlib import Path
from copy import deepcopy
from PIL import Image, ImageOps
from multiprocessing.pool import ThreadPool

from torch.utils.data import Dataset

from ultralytics.utils import NUM_THREADS, TQDM
from ultralytics.data.utils import IMG_FORMATS, exif_size

class BaseDetectionDataset(Dataset):
    def __init__(self, image_list):
        super().__init__()
        self.im_files = self.get_img_files(image_list)
        self.labels = self.cache_labels()
        self.ni = len(self.labels)    # number of images
        
    def verify_image(self, im_file):
        nc, msg = 0, ""
        try:
            im = Image.open(im_file)
            im.verify()  # PIL verify
            shape = exif_size(im)  # image size
            shape = (shape[1], shape[0])  # hw
            assert (shape[0] > 9) & (shape[1] > 9), f"image size {shape} <10 pixels"
            assert im.format.lower() in IMG_FORMATS, f"invalid image format {im.format}"
            if im.format.lower() in ("jpg", "jpeg"):
                with open(im_file, "rb") as f:
                    f.seek(-2, 2)
                    if f.read() != b"\xff\xd9":  # corrupt JPEG
                        ImageOps.exif_transpose(Image.open(im_file)).save(im_file, "JPEG", subsampling=0, quality=100)
                        msg = f"{prefix}WARNING ⚠️ {im_file}: corrupt JPEG restored and saved"
            return [im, im_file, shape, nc, msg]
        except Exception as e:
            nc = 1
            msg = f"WARNING ⚠️ {im_file}: ignoring corrupt image/label: {e}"
            return [None, None, nc, msg]
        
        return im, im_file, shape, nc, msg
        
    def cache_labels(self):
        """
        Cache dataset labels, check images and read shapes.

        Args:
            path (Path): Path where to save the cache file. Default is Path('./labels.cache').

        Returns:
            (dict): labels.
        """
        x = {"labels": []}
        nc, msgs = 0, []  # number missing, found, empty, corrupt, messages
        desc = f"Scanning ..."
        total = len(self.im_files)
        nkpt, ndim = (0, 0)
        
        verify_func = self.verify_image
        with ThreadPool(NUM_THREADS) as pool:
            results = pool.imap(
                func=verify_func,
                iterable=self.im_files,
            )
            pbar = TQDM(results, desc=desc, total=total)
            for im_file, im_path, shape, nc_f, msg in pbar:
                nc += nc_f
                if im_file:
                    x["labels"].append(
                        dict(
                            im_path=im_path,
                            shape=shape,
                        )
                    )
                if msg:
                    msgs.append(msg)
                pbar.desc = f"{desc} {total} images, {nc} corrupt"
            pbar.close()

        return x["labels"]
        
    def get_image_and_label(self, index):
        """Get and return label information from the dataset."""
        label = deepcopy(self.labels[index])
        label["img"], label["ori_shape"], label["resized_shape"] = self.load_image(index)
        label["ratio_pad"] = (
            label["resized_shape"][0] / label["ori_shape"][0],
            label["resized_shape"][1] / label["ori_shape"][1],
        )  # for evaluation
        return label
    
    def get_img_files(self, img_path):
        """Read image files."""
        try:
            f = []  # image files
            for p in img_path if isinstance(img_path, list) else [img_path]:
                p = Path(p).resolve()  # os-agnostic
                if p.is_dir():  # dir
                    f += glob.glob(str(p / "**" / "*.*"), recursive=True)
                    # F = list(p.rglob('*.*'))  # pathlib
                elif p.is_file() and 'txt' in str(p):  # file
                    with open(p) as t:
                        t = t.read().strip().splitlines()
                        parent = str(p.parent) + os.sep
                        f += [x.replace("./", parent) if x.startswith("./") else x for x in t]  # local to global path
                        # F += [p.parent / x.lstrip(os.sep) for x in t]  # local to global path (pathlib)
                elif p.is_file() and not ('txt' in str(p)):
                    parent = str(p.parent) + os.sep
                    f.append(str(p).replace("./", parent) if str(p).startswith("./") else str(p))
                else:
                    raise FileNotFoundError(f"{self.prefix}{p} does not exist")
            im_files = sorted(x.replace("/", os.sep) for x in f if x.split(".")[-1].lower() in IMG_FORMATS)
            assert im_files, f"{self.prefix}No images found in {img_path}"
        except Exception as e:
            raise FileNotFoundError(f"{self.prefix}Error loading data from {img_path}") from e
        return im_files
    
    def __getitem__(self, index):
        """Returns transformed label information for given index."""
        image_and_label = self.get_image_and_label(index)
        return image_and_label
    
    def __len__(self):
        """Returns the length of the labels list for the dataset."""
        return len(self.labels)