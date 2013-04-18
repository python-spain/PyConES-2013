# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Subscription', fields ['newsletter', 'user']
        db.delete_unique('newsletter_subscription', ['newsletter_id', 'user_id'])

        # Deleting field 'Subscription.newsletter'
        db.delete_column('newsletter_subscription', 'newsletter_id')

        # Deleting field 'Subscription.user'
        db.delete_column('newsletter_subscription', 'user_id')

        # Adding field 'Subscription.user_email'
        db.add_column('newsletter_subscription', 'user_email',
                      self.gf('django.db.models.fields.EmailField')(default=None, max_length=75),
                      keep_default=False)

        # Adding field 'Subscription.val_token'
        db.add_column('newsletter_subscription', 'val_token',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=128),
                      keep_default=False)

        # Deleting field 'Newsletter.name'
        db.delete_column('newsletter_newsletter', 'name')

        # Adding field 'Newsletter.title'
        db.add_column('newsletter_newsletter', 'title',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255),
                      keep_default=False)

        # Adding field 'Newsletter.head'
        db.add_column('newsletter_newsletter', 'head',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)

        # Adding field 'Newsletter.send_date'
        db.add_column('newsletter_newsletter', 'send_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)

        # Adding M2M table for field articles on 'Newsletter'
        db.create_table('newsletter_newsletter_articles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsletter', models.ForeignKey(orm['newsletter.newsletter'], null=False)),
            ('article', models.ForeignKey(orm['newsletter.article'], null=False))
        ))
        db.create_unique('newsletter_newsletter_articles', ['newsletter_id', 'article_id'])

        # Deleting field 'Article.publish_date'
        db.delete_column('newsletter_article', 'publish_date')


    def backwards(self, orm):
        # Adding field 'Subscription.newsletter'
        db.add_column('newsletter_subscription', 'newsletter',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='subscriptions', to=orm['newsletter.Newsletter']),
                      keep_default=False)

        # Adding field 'Subscription.user'
        db.add_column('newsletter_subscription', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='subscriptions', to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Subscription.user_email'
        db.delete_column('newsletter_subscription', 'user_email')

        # Deleting field 'Subscription.val_token'
        db.delete_column('newsletter_subscription', 'val_token')

        # Adding unique constraint on 'Subscription', fields ['newsletter', 'user']
        db.create_unique('newsletter_subscription', ['newsletter_id', 'user_id'])

        # Adding field 'Newsletter.name'
        db.add_column('newsletter_newsletter', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, unique=True),
                      keep_default=False)

        # Deleting field 'Newsletter.title'
        db.delete_column('newsletter_newsletter', 'title')

        # Deleting field 'Newsletter.head'
        db.delete_column('newsletter_newsletter', 'head')

        # Deleting field 'Newsletter.send_date'
        db.delete_column('newsletter_newsletter', 'send_date')

        # Removing M2M table for field articles on 'Newsletter'
        db.delete_table('newsletter_newsletter_articles')

        # Adding field 'Article.publish_date'
        db.add_column('newsletter_article', 'publish_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)


    models = {
        'newsletter.article': {
            'Meta': {'ordering': "['create_date']", 'object_name': 'Article'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'newsletter.newsletter': {
            'Meta': {'ordering': "['send_date']", 'object_name': 'Newsletter'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['newsletter.Article']", 'symmetrical': 'False'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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