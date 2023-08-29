import os
from celery import Celery

# Установка переменной окружения для настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject4.settings')

# Создание экземпляра объекта Celery
app = Celery('djangoProject4')

# Загрузка настроек из файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из файлов tasks.py в приложениях Django
app.autodiscover_tasks()
