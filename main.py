from fastapi import FastAPI
import uvicorn

from utils.routes import router

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

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
