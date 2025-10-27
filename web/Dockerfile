# web/Dockerfile
FROM python:3.11-slim

# set workdir
WORKDIR /app

# copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY main.py .

# expose port
EXPOSE 8000

# start command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
