from fastapi import FastAPI, status, UploadFile, Response
from src.pdf_converter import convert_pdf

app = FastAPI()

@app.get("/status", status_code=status.HTTP_200_OK)
def get_status():
    return {"status": "OK"}

@app.post("/convert", status_code=status.HTTP_201_CREATED)
def convert(file: UploadFile, response: Response):
    if file.content_type != 'application/pdf':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return "Invalid input. File must be a PDF"
    
    image = convert_pdf(file)
    return {"data": image}
