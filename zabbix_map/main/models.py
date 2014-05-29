from django.db import models

class Switch(models.Model):
	zabbix_id = models.IntegerField(db_index=True)
	zabbix_name = models.CharField(max_length=250)
	parent = models.ForeignKey('self')
	point = models.ForeignKey('Point')
	def __unicode__(self):
            return '%s' % (str(self.zabbix_name))

class Point(models.Model):
    geo_N = models.FloatField()
    geo_E = models.FloatField()
    name = models.CharField(max_length=250, default='')

    def __unicode__(self):
        return '%s, %s' % (str(self.geo_N), str(self.geo_E))
