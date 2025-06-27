FROM ubuntu:latest
LABEL authors="Anjar"

ENTRYPOINT ["top", "-b"]