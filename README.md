# pdf-to-png 🖼

Microservice for sending in a PDF and getting back a PNG of the first page. Built to convert the PDFs for HeHEs on [Efterphest](https://github.com/esek/efterphest) into PNGs that can be displayed to users.

Written in Python, using [FastAPI](https://fastapi.tiangolo.com/), to quickly build a working microservice.

## 🚀 Endpoints

FastAPI autogenerates some documentation for endpoints at `/docs`, where it is also possible to manually test the endpoints.

### `POST /convert`

Sending in a PDF-file will return the first page of the PDF as a PNG.

### `GET /status`

Status endpoint that just informs that the system isn't dead

## Quickstart

[Create a  venv environment](https://towardsdatascience.com/getting-started-with-python-virtual-environments-252a6bd2240). Then install the dependencies to the environment from `pyproject.toml` using pip:

```bash
pip install .
```

Start the microservice using the following command from the root of this directory. [uvicorn](https://www.uvicorn.org/) is used to start an instance of a FastAPI server (called `app` in `/src/main.py`):

```bash
python3 -m uvicorn src.main:app --reload
```

## Testing

To download all test dependencies, run:

```bash
pip install -e '.[test]'
```

For unit testing and integration testing, `pytest` and the FastAPI `TestClient` is used in the `tests` directory. To run all tests, just run the following command:

```bash
pytest
```

`print`-statements can be added in the code. Then the `-s` flag can be added to the command above to see output from the `print`-statements to the terminal.
