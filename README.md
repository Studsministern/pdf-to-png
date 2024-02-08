# pdf-to-png 🖼

Microservice for sending in a PDF and getting back a PNG of the first page. Built for creating PNGs for displaying HeHEs on [Efterphest](https://github.com/esek/efterphest).

Written in Python, using [FastAPI](https://fastapi.tiangolo.com/), to quickly build a working microservice.

## 🚀 Endpoints

### `POST /convert`

Sending in a PDF will return the first page of the PDF as a PNG.

### `GET /status`

Status endpoint that just informs that the system isn't dead

## Quickstart

Install the requirements from `requirements.txt` using:

```bash
pip install -r requirements.txt
```

Start the microservice by running the following command from the root of this directory:

```
uvicorn src.main:app --reload
```