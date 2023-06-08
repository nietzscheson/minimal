import sys

from django.conf import settings
from django.urls import path, re_path
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.views.debug import default_urlconf
from django.contrib import admin

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

settings.configure(
    SECRET_KEY="change-me",
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
    DATABASES = {
        'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / '/app/db.sqlite3',
        }
    },
    INSTALLED_APPS = [
        'app.apps.AppConfig',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.staticfiles',
    ],
    AUTH_USER_MODEL = 'app.User',
    STATIC_URL = '/static/',
    TIME_ZONE = 'UTC',
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        }
    ]
)

def minimal(request):
    return HttpResponse('<h1>Django Minimal Project!</h1>')

urlpatterns = [
    re_path(r'^minimal/?$', minimal, name='minimal'),
    path('', default_urlconf, name='index'),

]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
else:

    from django.core.wsgi import get_wsgi_application

    application = get_wsgi_application()

