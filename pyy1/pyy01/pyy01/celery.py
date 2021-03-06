from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTING_MODULE", "pyy01.settings")

app = Celery("mycelery")

app.conf.timezone = "Asia/Shanghai"

app.config_from_object("django.conf:settings")

app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)
