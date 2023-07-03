FROM python:3.10-alpine
LABEL "Created"="Vladimir_SH"

ARG base_url
ENV BASE_URL $base_url
ARG user_name
ENV UNAME $user_name
ARG password
ENV PAWORD $password

#VOLUME/TestResultContainer
WORKDIR /app
COPY requirements.txt . /app/
RUN apk update && apk upgrade && apk add bash
RUN pip3 install requirements.txt
COPY . .



CMD pytest --alluredir=TestResultContainer

#Instructions for launch docker container

#docker build -t test_container:v1 --build-arg BASE_URL=https://restful-booker.herokuapp.com\
 #UNAME=admin PAWORD=password1234 .

#docker cp $(docker -a -q | head -1 ):/app .


