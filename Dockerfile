FROM python:3.11-slim

WORKDIR /crear-amoblamientos

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "crear_amoblamientos.wsgi:application", "--bind", "0.0.0.0:8000"]


