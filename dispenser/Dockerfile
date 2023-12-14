FROM balenalib/generic-amd64-python:latest-build
ENV UDEV=on
ENV EMULATED=1

WORKDIR /usr/app

COPY ./requirements.txt .
COPY ./src/. ./src/

RUN install_packages ffmpeg v4l-utils
RUN pip3 install -r requirements.txt

WORKDIR /usr/app/src
#CMD ["python3", "run.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:80", "-w", "1", "run:app"]