from base64 import b64encode

import asyncio
from fastapi import APIRouter, HTTPException, status, UploadFile

from utils.pdf_converter import convert_pdf


router = APIRouter()


@router.get("/")
def root():
    return {"message": "Hello there!", "answer": "Ah, General Kenobi!"}


@router.get("/status", tags=["status"], status_code=status.HTTP_200_OK)
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


@router.post(
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
