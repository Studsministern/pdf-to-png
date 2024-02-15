FROM python:3.12

WORKDIR /app
COPY . .
RUN pip install .

EXPOSE 8080

CMD [ "python3", "main.py" ]