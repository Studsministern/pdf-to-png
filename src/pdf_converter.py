from fastapi import UploadFile
from pdf2image import convert_from_bytes
from PIL.Image import Image

def convert_pdf(upload_file: UploadFile) -> Image:
    bytes = upload_file.file.read()
    pages = convert_from_bytes(pdf_file=bytes, last_page=1)
    return pages[0]
