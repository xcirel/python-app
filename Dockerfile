FROM python:3.11-alpine

COPY requirements.txt /tmp
COPY ./src /src
RUN pip install -r /tmp/requirements.txt
RUN adduser xcirel --disabled-password
RUN apk add curl --no-cache

USER xcirel
ENTRYPOINT ["python", "src/app.py"]
HEALTHCHECK CMD curl -k --fail http://localhost:5000/api/v1/healthz
