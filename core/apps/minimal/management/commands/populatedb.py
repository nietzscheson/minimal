from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from django.contrib.auth.hashers import make_password
from apps.minimal.models import User

class Command(BaseCommand):
    help = 'Populate Database'

    def seeder_database(self):
        User.objects.create_user('admin', 'admin@admin.com', 'admin', **{"is_active": True, "is_staff": True, "is_superuser": True})
    def handle(self, *args, **options):
        self.seeder_database()