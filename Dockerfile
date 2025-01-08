# Используем официальный Python-образ
FROM python:3.13
# Устанавливаем переменные окружения для работы с базой данных (можно указать, если необходимо)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Устанавливаем рабочую директорию в контейнере
WORKDIR /code
# Копируем файл зависимостей в контейнер
COPY requirements.txt /code/
# Устанавливаем зависимости
RUN pip install -r requirements.txt
# Копируем весь код проекта в рабочую директорию контейнера
COPY . /code/
# Открываем порт, на котором будет работать сервер (обычно 8000 для Django)
EXPOSE 8000
# Запуск приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]