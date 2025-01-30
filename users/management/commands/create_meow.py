from django.core.management.base import BaseCommand
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **kwargs):
        user = CustomUser.objects.create(email='meow@meow.meow')
        user.set_password('meow')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
