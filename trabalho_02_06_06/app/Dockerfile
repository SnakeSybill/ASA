FROM python:3.7-alpine
WORKDIR ./
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
# ENV http_proxy proxy.ufu.br:
RUN apk add --no-cache postgresql-dev gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]