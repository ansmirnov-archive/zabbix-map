__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from django.contrib import admin
from main import models

class SwitchAdmin(admin.ModelAdmin):
    search_fields = ['zabbix_name']

class PointAdmin(admin.ModelAdmin):
    search_fields = ['geo_N', 'geo_E']

admin.site.register(models.Switch, SwitchAdmin)
admin.site.register(models.Point, PointAdmin)