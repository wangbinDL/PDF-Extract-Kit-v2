import os
from torch.utils.data import Dataset
from pdf_extract_kit.utils.pdf_utils import load_pdf

class PDFDataset(Dataset):
    def __init__(self, pdf_dir):
        self.pdf_files = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

    def __len__(self):
        return len(self.pdf_files)

    def __getitem__(self, idx):
        pdf_path = self.pdf_files[idx]
        images = load_pdf(pdf_path)
        return images, pdf_path