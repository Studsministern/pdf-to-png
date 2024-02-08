from pdf2image import convert_from_bytes
from typing import Image

def convert_to_pdf(pdf_bytes: bytes) -> Image:
    pages = convert_from_bytes(pdf_file=pdf_bytes, last_page=1)
    return pages[0]
