
# syntax=docker/dockerfile:1

FROM python:3.9-buster

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install build-essential -y

RUN apt-get update && \
    apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Bangkok /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata
ENV TZ="Asia/Bangkok"


RUN pip3 install mysqlclient

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV TZ = Asia/Bangkok

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


