FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn run:app -b 0.0.0.0:9000

EXPOSE 9000



