from .base import *


INSTALLED_APPS += ["django_extensions", "debug_toolbar"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"