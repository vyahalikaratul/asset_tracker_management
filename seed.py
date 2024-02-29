# seeds.py

from django.contrib.auth.models import User


def create_admin():
    admin_username = 'admin'
    admin_password = 'admin123'
    if not User.objects.filter(username=admin_username).exists():
        User.objects.create_superuser(admin_username, 'atulvyahalikar2010@gmail.com', admin_password)


def run_seeders():
    create_admin()


if __name__ == '__main__':
    run_seeders()
