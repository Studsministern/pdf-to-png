FROM python:3.12

# TODO: Check the WORKDIR. /usr/app? /usr/src?
WORKDIR /app 

# TODO: install with pyproject.toml and pip before copying everything?
COPY . .

RUN pip install .

# TODO: Correct port?
ENV PORT=8080

# TODO: Does this port matter? Or must it just be the same as localhost port?
EXPOSE 3000

CMD [ "python3", "-m", "uvicorn", "src.main:app" ]