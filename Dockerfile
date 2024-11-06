FROM python:3.12.6-slim

RUN apt-get update && \
    apt-get install -y tesseract-ocr libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

WORKDIR /app
# Install Python dependencies
RUN pip install python-dotenv
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10011

CMD ["python", "_server.py"]