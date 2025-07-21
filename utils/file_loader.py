# utils/file_loader.py
from docx import Document
from PyPDF2 import PdfReader
import pandas as pd

def load_file(file):
    if file.name.endswith(".pdf"):
        return "\n".join([p.extract_text() for p in PdfReader(file).pages])
    elif file.name.endswith(".docx"):
        return "\n".join([para.text for para in Document(file).paragraphs])
    elif file.name.endswith(".csv"):
        df = pd.read_csv(file)
        return df.to_csv(index=False)
    else:
        raise ValueError("Unsupported file format")
