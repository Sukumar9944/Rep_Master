FROM python:3.11-slim

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install -y espeak && apt-get install -y alsa-utils

RUN pip3 install -r requirements.txt

CMD ["streamlit","run","app.py"]