# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Установим зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем код
COPY . /app

# Запускаем приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
