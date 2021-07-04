import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stackoverflowapi.settings')
app = Celery('stackoverflowapi')

BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
app.conf.broker_url = BASE_REDIS_URL

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))


