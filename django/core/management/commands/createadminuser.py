from django.core.management.base import BaseCommand
from blog.models import User


class Command(BaseCommand):
    help = 'Creates a superuser if one does not already exist.'

    def handle(self, *args, **options):
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(username='admin', password='admin')
            self.stdout.write('Superuser created successfully.')
        else:
            self.stdout.write('Superuser already exists.')
