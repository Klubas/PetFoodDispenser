FROM balenalib/raspberrypi3-python:latest-build
ENV UDEV=on

RUN install_packages cron
RUN pip3 install RPi.GPIO schedule pytz

COPY ./start.sh /
COPY ./ServoControl/. /ServoControl/

RUN chmod a+x /start.sh

ENTRYPOINT [ "/bin/bash" ]
CMD [ "-c", "/start.sh"]