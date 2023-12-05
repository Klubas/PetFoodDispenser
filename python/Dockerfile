FROM balenalib/raspberrypi3-python:latest-build

RUN install_packages cron
RUN pip3 install RPi.GPIO

COPY ./scripts/. /scripts/

RUN chmod a+x /scripts/start.sh

ENV UDEV=on

ENTRYPOINT [ "/bin/bash" ]
CMD [ "-c", "/scripts/start.sh"]