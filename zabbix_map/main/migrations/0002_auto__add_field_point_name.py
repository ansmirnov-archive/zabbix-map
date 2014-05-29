# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Point.name'
        db.add_column(u'main_point', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Point.name'
        db.delete_column(u'main_point', 'name')


    models = {
        u'main.point': {
            'Meta': {'object_name': 'Point'},
            'geo_E': ('django.db.models.fields.FloatField', [], {}),
            'geo_N': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        u'main.switch': {
            'Meta': {'object_name': 'Switch'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Switch']"}),
            'point': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Point']"}),
            'zabbix_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'zabbix_name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['main']