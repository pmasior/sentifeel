FROM python:3.12

WORKDIR /app

COPY requirements.txt ./
RUN ["python3", "-m", "pip", "install", "-r", "requirements.txt"]

CMD ["bash"]
