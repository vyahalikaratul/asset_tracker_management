
from django.core.management.base import BaseCommand
from authentication.models import CustomUser


class Command(BaseCommand):
    """
    Django management command for seeding the system admin user.

    This command creates a superuser with predefined username, email, and password if the user doesn't already exist.
    """
    help = 'Seeds the system admin user'

    def handle(self, *args, **options):
        """
        Method executed when the management command is invoked.

        It creates a superuser with predefined username, email, and password if the user doesn't already exist.
        """
        username = 'admin'
        email = 'atulvyahalikar2010@gmail.com'
        password = 'atul1234'  # Choose a strong password

        if not CustomUser.objects.filter(email=email).exists():  # Update this line
            CustomUser.objects.create_superuser(email=email, password=password)
            self.stdout.write(self.style.SUCCESS('System admin created successfully'))
        else:
            self.stdout.write(self.style.WARNING('System admin already exists'))

