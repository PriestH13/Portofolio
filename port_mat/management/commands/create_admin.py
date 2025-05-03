from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Crea un superuser automaticamente se non esiste.'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'PretisH13')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'mateo.prifti13@gmail.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '0324')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' creato con successo"))
        else:
            self.stdout.write(f"Superuser '{username}' esiste già")
