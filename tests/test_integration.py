import io
from base64 import b64decode

from PIL import Image
import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient

from main import app
import tests.test_utils as test


client = TestClient(app)


def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


@pytest.mark.asyncio
async def test_convert():
    with open(test.PDF_PATH, "rb") as test_pdf:
        # Call the endpoint with the PDF file and ensure the response is succcessful
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.post("/convert", files={"file": test_pdf})
        assert response.status_code == 201

        # Convert the b64 encoded image from the response to bytes, and then into an image
        # Inspired from this Stack Overflow answer: https://stackoverflow.com/a/32908899
        image_b64: str = response.json()["image_b64"]
        image_bytes = b64decode(image_b64)
        image = Image.open(io.BytesIO(image_bytes))
        image.save(test.PNG_PATH, "PNG")
