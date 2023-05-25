FROM ubuntu:latest
RUN apt-get -y update
FROM python:3
RUN pip install --upgrade pip
COPY . .
WORKDIR /seovermind
ADD 'SEOvermind0.1-Beta.py' /
COPY requirements.txt /seovermind/
RUN pip install --requirement /seovermind/requirements.txt
COPY . /seovermind/
CMD [ "python", "./SEOvermind0.1-Beta.py" ]