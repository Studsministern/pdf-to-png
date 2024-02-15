import io

from PIL import Image

from utils.pdf_converter import convert_pdf
import tests.test_utils as test


def test_convert_pdf():
    with open(test.PDF_PATH, "rb") as test_pdf:
        # Check the return type of the function
        image_bytes = convert_pdf(test_pdf)
        assert isinstance(image_bytes, bytes)

        # Check that the conversion of the image works as expected
        image = Image.open(io.BytesIO(image_bytes))
        assert isinstance(image, Image.Image)
        image.save(test.PNG_PATH, "PNG")
