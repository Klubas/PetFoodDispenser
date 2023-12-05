#FROM hurlenko/filebrowser:v2.22.4
FROM hurlenko/filebrowser:latest
ENV UDEV=on

COPY ./run.sh /
RUN chmod a+x /run.sh

ENTRYPOINT [ "/bin/sh" ]
CMD [ "-c", "/run.sh"]