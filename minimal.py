import sys
import os

from django.conf import settings
from django.conf.urls import url
from django.urls import path
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.apps import AppConfig

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

settings.configure(
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
    DATABASES = {
        'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
        }
    },
    INSTALLED_APPS = [
        'app.apps.AppConfig',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.staticfiles',
        'graphene_django',
        'django_seed',
        'corsheaders'
    ],
    AUTH_USER_MODEL = 'app.User',
    STATIC_URL = '/static/',
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware'
    ],
    TIME_ZONE = 'UTC',
    GRAPHENE = {
        'SCHEMA': 'app.schema.schema'
    },
    CORS_ORIGIN_WHITELIST = [
        'http://localhost:3000',
        'http://client:3000'
    ],
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        }
    ]
)

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

def index(request):
    return HttpResponse('<h1>Django Minimal Project!</h1>')

urlpatterns = [
    url(r'^$', index),
    url(r'^graphql$', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
else:

    from django.core.wsgi import get_wsgi_application

    application = get_wsgi_application()

