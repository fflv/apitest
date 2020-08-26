Инструкция по разворачиванию (локально):

1. Создать виртуальное окружение, активировать
python3 -m venv venv
source venv/bin/activate

2. Установить зависимости
pip install -r requirements.txt

3. Выполнить миграции, находясь в каталоге drfquestions
python manage.py makemigrations
python manage.py migrate

4. Создать суперпользователя
python manage.py createsuperuser

5. Запустить сервер и выполнить вход в административную панель
python manage.py runserver

6. После этого можно использовать API для создания опросов/вопросов/ответов

Автодокументирование API, точки входа:
localhost:8000/swagger/
localhost:8000/redoc/


Задачи, не решённые за отведенное время:
 -валидация типов вопросов
 -покрытие кода тестами
 -разворачивание приложения в docker
