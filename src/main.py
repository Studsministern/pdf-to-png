import asyncio
from base64 import b64encode

from fastapi import FastAPI, status, UploadFile, Response
from pydantic import BaseModel, Field

from src.pdf_converter import convert_pdf


description = """
Microservice for sending in a PDF and getting back a PNG of the first page.

Built to convert the PDFs for student newspapers into PNGs that can be displayed to users.

### Note

This API is only intended to be used by the [E-guild at LTH](https://github.com/esek).
"""

app = FastAPI(
    title="PDF to PNG",
    description=description,
    # summary="Uploading a PDF will return a PNG",
    version="0.1.0",
    # terms_of_service="http://example.com/terms/",
    contact={
        "name": "Eric Weidow",
        "url": "https://github.com/Studsministern",
        "email": "eric@weidow.se",
    },
    # license_info={
    #     "name": "Apache 2.0",
    #     "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    # },
)



@app.get("/")
def root():
    return {"message": "Hello there!", "answer": "Ah, General Kenobi!"}



# TODO: Split status into a route and models
class Status(BaseModel):
    status: str = Field(examples=["OK"])

@app.get(
    "/status",
    tags=["status"],
    status_code=status.HTTP_200_OK,
    response_model=Status
)
def get_status():
    """
    Returns the status of the application.
    
    **Returns**:
    - `status`: Contains the status of the application.
              Will return '{"status": "OK"}' if everything works as intended.
    """
    return {"status": "OK"}


# TODO: Split convert into a route and models
class PDF(BaseModel):
    file: UploadFile = Field(examples=["<a PDF file>"])

class PNG(BaseModel):
    image_b64: bytes = Field(examples=["<base64 encoded bytes for a PNG>"])

@app.post(
    "/convert",
    tags=["convert"],
    status_code=status.HTTP_201_CREATED,
    response_model=PNG
)
async def convert(file: PDF, response: Response):
    """
    Converts a PDF file to a base64 encoded image.

    **Args**:
    - `file` ([UploadFile](https://fastapi.tiangolo.com/reference/uploadfile/)): The PDF file to be converted.

    **Returns**:
    - `image_b64`: A **JSON** containing the base64 encoded image.
    """

    if file.content_type != "application/pdf":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return "Invalid input. File must be a PDF"
    
    image_bytes = await asyncio.to_thread(convert_pdf, file.file)
    image_b64 = b64encode(image_bytes)
    await file.close()
    return { "image_b64": image_b64 }
