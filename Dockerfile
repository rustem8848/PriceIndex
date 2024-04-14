# Используем базовый образ Python
FROM python:3.9

# Переключаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 5000 для Flask-приложения
EXPOSE 5000

# Запускаем Flask-приложение
CMD ["python", "website.py"]