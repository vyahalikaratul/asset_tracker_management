# from django.core.management.base import BaseCommand
# from django.contrib.admin.models import LogEntry
# from authentication.models import CustomUser
#
# class Command(BaseCommand):
#     help = 'Fixes invalid foreign key references in django_admin_log'
#
#     def handle(self, *args, **options):
#         LogEntry.objects.filter(user_id__isnull=False).exclude(user_id__in=CustomUser.objects.values_list('id', flat=True)).delete()
