import asyncio
from base64 import b64encode

from fastapi import FastAPI, HTTPException, status, UploadFile

from src.pdf_converter import convert_pdf


description = """
Microservice for sending in a PDF and getting back a PNG of the first page.

Built to convert the PDFs for HeHEs into PNGs that can be displayed to users.

### Note

This API is only intended to be used by the [E-guild at LTH](https://github.com/esek).
"""

app = FastAPI(
    title="PDF to PNG",
    description=description,
    version="0.1.0",
    contact={
        "name": "Eric Weidow",
        "url": "https://github.com/Studsministern",
        "email": "eric@weidow.se",
    },
)


@app.get("/")
def root():
    return {"message": "Hello there!", "answer": "Ah, General Kenobi!"}


@app.get("/status", tags=["status"], status_code=status.HTTP_200_OK)
def get_status():
    """
    Returns the status of the application.

    **Returns**:
    - **status**: Contains the status of the application:
    ```json
    {
        "status": "OK"
    }
    ```
    """
    return {"status": "OK"}


@app.post(
    "/convert",
    tags=["convert"],
    status_code=status.HTTP_201_CREATED,
)
async def convert(file: UploadFile):
    """
    Converts a PDF file to a base64 encoded image.

    **Args**:
    - **file** ([UploadFile](https://fastapi.tiangolo.com/reference/uploadfile/)): The PDF file to be converted:
    ```json
    {
        "file": <A PDF file>
    }
    ```

    **Returns**:
    - **image_b64**: A **JSON** containing the base64 encoded image:
    ```json
    {
        "image_b64": <A base64 encoded image>
    }
    ```
    """

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid input. File must be a PDF",
        )

    image_bytes = await asyncio.to_thread(convert_pdf, file.file)
    image_b64 = b64encode(image_bytes)
    await file.close()
    return {"image_b64": image_b64}
