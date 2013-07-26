# -*- coding: utf-8 -*-
from django.core import mail
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import admin
from django.contrib.sites.models import Site
from pycones import utils
from pycones.newsletter.models import Newsletter, Article, Subscription

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'order', 'created_date', 'visible')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)


class NewsletterAdmin(admin.ModelAdmin):
    model = Newsletter
    list_display = ('__unicode__', 'created_date', 'sent', 'sent_date')

admin.site.register(Newsletter, NewsletterAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    list_display = ('user_email', 'admin')

admin.site.register(Subscription, SubscriptionAdmin)

