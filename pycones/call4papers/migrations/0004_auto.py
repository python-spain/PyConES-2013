# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field speakers on 'Talk'
        db.create_table('call4papers_talk_speakers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('talk', models.ForeignKey(orm['call4papers.talk'], null=False)),
            ('speaker', models.ForeignKey(orm['call4papers.speaker'], null=False))
        ))
        db.create_unique('call4papers_talk_speakers', ['talk_id', 'speaker_id'])


    def backwards(self, orm):
        # Removing M2M table for field speakers on 'Talk'
        db.delete_table('call4papers_talk_speakers')


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
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['call4papers.Speaker']"}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'speakers'", 'symmetrical': 'False', 'to': "orm['call4papers.Speaker']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['call4papers']