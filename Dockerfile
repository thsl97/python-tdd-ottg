FROM ubuntu:18.04
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y firefox firefox-geckodriver \
    python3-pip python3-venv
