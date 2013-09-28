# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Talk.sc_hour'
        db.add_column('call4papers_talk', 'sc_hour',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Talk.sc_track'
        db.add_column('call4papers_talk', 'sc_track',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Talk.sc_day'
        db.add_column('call4papers_talk', 'sc_day',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'Talk', fields ['sc_hour', 'sc_day', 'sc_track']
        db.create_unique('call4papers_talk', ['sc_hour', 'sc_day', 'sc_track'])


    def backwards(self, orm):
        # Removing unique constraint on 'Talk', fields ['sc_hour', 'sc_day', 'sc_track']
        db.delete_unique('call4papers_talk', ['sc_hour', 'sc_day', 'sc_track'])

        # Deleting field 'Talk.sc_hour'
        db.delete_column('call4papers_talk', 'sc_hour')

        # Deleting field 'Talk.sc_track'
        db.delete_column('call4papers_talk', 'sc_track')

        # Deleting field 'Talk.sc_day'
        db.delete_column('call4papers_talk', 'sc_day')


    models = {
        'call4papers.speaker': {
            'Meta': {'ordering': "['name']", 'object_name': 'Speaker'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'call4papers.talk': {
            'Meta': {'unique_together': "(['sc_hour', 'sc_track', 'sc_day'],)", 'object_name': 'Talk'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sc_day': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'sc_hour': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'sc_track': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'talks'", 'symmetrical': 'False', 'to': "orm['call4papers.Speaker']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['call4papers']