FROM python:3.9

WORKDIR /api

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY studentsperformance .
COPY README.md .

EXPOSE 5000

CMD ["python", "main.py"]