FROM python:3.10-slim

RUN apt update && \
apt install -y netcat-traditional && \
apt install -y curl && \
apt install vim -y && \
apt clean && \
rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
COPY src/ .

RUN pip install -r requirements.txt

EXPOSE 5000 

ENTRYPOINT ["python"]
CMD ["app.py"]
