FROM python:3.9.6-slim-buster

RUN apt-get -y update && \
    apt-get -y install libffi-dev libnacl-dev libpython3-dev && \
    python3 -m pip install -U discord.py && \
    pip3 install python-twitter

WORKDIR /app
