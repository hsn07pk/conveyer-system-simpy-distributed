# File: server/Dockerfile  
FROM python:3.9  
WORKDIR /app  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  
EXPOSE 50051 8000
COPY . .  
CMD ["python", "server.py"]  