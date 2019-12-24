# flake8: noqa

import json
import os.path

from django.core.exceptions import ImproperlyConfigured

from .base import *

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.json")

with open(CONFIG_FILE, "rt") as f:
    CONFIG = json.loads(f.read())


def get_config(key, default=None):
    """Get the secret variable or return explicit exception."""
    try:
        return CONFIG[key]
    except KeyError:
        if default:
            return default

        error_msg = f"Set the {key} in configuration file"
        raise ImproperlyConfigured(error_msg)


DEBUG = False

ADMINS = ("Khasbilegt", "khasbilegt@form.mn")

ALLOWED_HOSTS = ["store.form.mn"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "form",
        "USER": "form",
        "PASSWORD": get_config("DB_PASSWORD"),
        "HOST": get_config("DB_HOST", "127.0.0.1"),
        "CONN_MAX_AGE": 3600,  # 1 hour
    }
}

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
MEDIA_URL = "https://media.form.mn/"
STATIC_URL = "https://static.form.mn/"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
