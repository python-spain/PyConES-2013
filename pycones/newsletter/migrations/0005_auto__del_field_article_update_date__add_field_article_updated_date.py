# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Article.update_date'
        db.delete_column('newsletter_article', 'update_date')

        # Adding field 'Article.updated_date'
        db.add_column('newsletter_article', 'updated_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 4, 19, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Article.update_date'
        db.add_column('newsletter_article', 'update_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=None, blank=True),
                      keep_default=False)

        # Deleting field 'Article.updated_date'
        db.delete_column('newsletter_article', 'updated_date')


    models = {
        'newsletter.article': {
            'Meta': {'ordering': "['created_date']", 'object_name': 'Article'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'newsletter.newsletter': {
            'Meta': {'ordering': "['send_date']", 'object_name': 'Newsletter'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['newsletter.Article']", 'symmetrical': 'False'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'head': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'send_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'newsletter.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'val_token': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['newsletter']