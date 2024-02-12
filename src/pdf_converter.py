import io
from typing import BinaryIO
from pdf2image import convert_from_bytes


def convert_pdf(file: BinaryIO) -> bytes:
    """
    Convert a PDF file to a PNG image.

    Args:
        file (BinaryIO): The PDF file to convert.

    Returns:
        bytes: The converted PNG image data.
    """
    bytes = file.read()
    pages = convert_from_bytes(pdf_file=bytes, last_page=1)
    image = pages[0]

    image_data = io.BytesIO()
    image.save(image_data, format=image.format)
    return image_data.getvalue()
