from django.db import models

class Switch(models.Model):
	zabbix_id = models.IntegerField(db_index=True)
	zabbix_name = models.CharField(length=250)
	parent_id = models.IntegerField(db_index=True)
	point = models.ForeignKey('Point')

class Point(models.Model):
	geo_N = models.FloatField()
	geo_E = models.FloatField()
