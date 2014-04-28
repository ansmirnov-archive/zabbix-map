__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from django.contrib import admin
from main import models

admin.site.register(models.Switch)
admin.site.register(models.Point)