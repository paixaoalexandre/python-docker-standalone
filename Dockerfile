FROM python:3.10
ADD . /src/apps
WORKDIR /src/apps
RUN pip install -r requirements.txt