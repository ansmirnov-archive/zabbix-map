# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Switch'
        db.create_table(u'main_switch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zabbix_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('zabbix_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Switch'])),
            ('point', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Point'])),
        ))
        db.send_create_signal(u'main', ['Switch'])

        # Adding model 'Point'
        db.create_table(u'main_point', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geo_N', self.gf('django.db.models.fields.FloatField')()),
            ('geo_E', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'main', ['Point'])


    def backwards(self, orm):
        # Deleting model 'Switch'
        db.delete_table(u'main_switch')

        # Deleting model 'Point'
        db.delete_table(u'main_point')


    models = {
        u'main.point': {
            'Meta': {'object_name': 'Point'},
            'geo_E': ('django.db.models.fields.FloatField', [], {}),
            'geo_N': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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