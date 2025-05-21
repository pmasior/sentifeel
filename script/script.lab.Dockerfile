FROM python:3.12

WORKDIR /app

RUN ["apt-get", "update"]
RUN ["apt-get", "--yes", "install", "firefox-esr"]

COPY requirements.txt ./
RUN ["python3", "-m", "pip", "install", "-r", "requirements.txt"]

CMD ["bash"]
