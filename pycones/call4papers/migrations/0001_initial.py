# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Speaker'
        db.create_table('call4papers_speaker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('web', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('call4papers', ['Speaker'])

        # Adding model 'Talk'
        db.create_table('call4papers_talk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('speaker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['call4papers.Speaker'])),
            ('abstract', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('selected', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('call4papers', ['Talk'])


    def backwards(self, orm):
        # Deleting model 'Speaker'
        db.delete_table('call4papers_speaker')

        # Deleting model 'Talk'
        db.delete_table('call4papers_talk')


    models = {
        'call4papers.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'call4papers.talk': {
            'Meta': {'object_name': 'Talk'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['call4papers.Speaker']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['call4papers']