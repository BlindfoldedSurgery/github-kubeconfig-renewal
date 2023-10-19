FROM python:3.12-slim

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD src src
ADD config.py .
ADD main.py .

CMD python -B -OO main.py
