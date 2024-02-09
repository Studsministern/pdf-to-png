# pdf-to-png 🖼

Microservice for sending in a PDF and getting back a PNG of the first page. Built to convert the PDFs for HeHEs on [Efterphest](https://github.com/esek/efterphest) into PNGs that can be displayed to users.

Written in Python, using [FastAPI](https://fastapi.tiangolo.com/), to quickly build a working microservice.

## 🚀 Endpoints

### `POST /convert`

Sending in a PDF-file will return the first page of the PDF as a PNG.

### `GET /status`

Status endpoint that just informs that the system isn't dead

## Quickstart

Create a `venv` environment. Then install the requirements to the environment from `requirements.txt` using:

```bash
pip install -r requirements.txt
```

Use the following command from the root of this directory to start the microservice. Then [uvicorn](https://www.uvicorn.org/) is used to start an instance of a FastAPI server (called `app` in `/src/main.py`):

```bash
python3 -m uvicorn src.main:app --reload
```
