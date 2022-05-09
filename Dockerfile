
# syntax=docker/dockerfile:1

FROM python:3.9-buster

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install build-essential -y

RUN pip3 install mysqlclient

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


