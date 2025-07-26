FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY extractor.py .
COPY persona_job.json .

RUN pip install pymupdf

CMD ["python", "extractor.py"]
