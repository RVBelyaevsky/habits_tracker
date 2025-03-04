# habits_tracker
# Проект по реализации бэкенд-части SPA веб-приложения "трекер полезных привычек"
# Установка 
1. клонирорвать репозитарий https://github.com/RVBelyaevsky/habits_tracker.git
2. установить зависимости из файла requirements.txt
3. заполнить .env.sample
4. запустить приложение >>> python manage.py runserver
5. запустить воркер >>> celery -A config worker -l INFO --pool=solo
6. запустить планировщик >>> celery -A config beat -l info -S django
# Документация
**http://127.0.0.1:8000/docs/swagger/**