__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from django.core.management.base import BaseCommand, CommandError
from main import models

class Command(BaseCommand):
    args = '<zabbix_id zabbix_name>'
    help = ''

    def handle(self, *args, **options):
        zabbix_id, zabbix_name = int(args[0]), args[1]
        
