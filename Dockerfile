# Используем официальный образ Python 3.11
FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем только нужные файлы
COPY requirements.txt .
COPY Dockerfile .
COPY app.py .
COPY README.md .

# Запускаем Streamlit
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
