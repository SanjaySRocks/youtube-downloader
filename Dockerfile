FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
        ffmpeg

RUN pip install git+https://github.com/ytdl-org/youtube-dl.git

