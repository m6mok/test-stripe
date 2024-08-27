import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    help = 'Создает суперпользователя на основе переменных окружения'

    def handle(self, *args, **kwargs):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if not username or not password:
            self.stdout.write(
                self.style.ERROR(
                    'Переменные окружения DJANGO_SUPERUSER_USERNAME и '
                    'DJANGO_SUPERUSER_PASSWORD должны быть установлены'
                )
            )
            return

        try:
            _ = User.objects.get(username=username)
            self.stdout.write(
                self.style.SUCCESS('Суперпользователь уже существует.')
            )
        except ObjectDoesNotExist:
            User.objects.create_superuser(username=username, password=password)
            self.stdout.write(
                self.style.SUCCESS('Суперпользователь успешно создан.')
            )
