FROM balenalib/raspberrypi3-python:latest-build
ENV UDEV=on

WORKDIR /usr/app
COPY ./requirements.txt .
COPY ./src/. ./src/

RUN pip3 install -r requirements.txt

WORKDIR /usr/app/src
CMD ["python3", "run.py"]
#CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:main"]