FROM python:3.8.2-buster

WORKDIR /

RUN apt-get update
COPY requirements.txt /
RUN pip3 install -r requirements.txt

COPY . .
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["uvicorn", "main:app","--host","0.0.0.0"]
