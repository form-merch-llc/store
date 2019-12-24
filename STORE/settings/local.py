# flake8: noqa

from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

INTERNAL_IPS = ["127.0.0.1", "localhost"]

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "form",
        "USER": "form",
        "PASSWORD": "F0rmM3rchLLC",
        "HOST": "127.0.0.1",
    }
}

MEDIA_URL = "/media/"
STATIC_URL = "/static/"

CORS_ORIGIN_ALLOW_ALL = True

EMAIL_FROM = "noreply@form.mn"

LOGIN_REDIRECT_URL = "/"
