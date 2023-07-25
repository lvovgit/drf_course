from django.core.management import BaseCommand
from users.models import User, UserRoles


class Command(BaseCommand):
    def handle(self, *args, **options):
        # user = User.objects.create_user()  # такое создание после переопределения на email в моделях UserCManager
        # user.save()
        user = User.objects.create(
            email='lionsonsam@yandex.ru',
            first_name='moder',
            last_name='moder',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            role=UserRoles.MODERATOR,
        )
        user.set_password('123')
        user.save()