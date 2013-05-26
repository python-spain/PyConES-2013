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

def send_newsletter(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied

    for newsletter in queryset:
        emails = []
        subject = '[PyConEs] %s' % newsletter.title
        context = {
            'newsletter': newsletter,
            'mail': True
        }
        from_email = settings.EMAIL_HOST_USER
        template_txt = 'newsletter/newsletter.txt'
        template_html =  'newsletter/newsletter.html'

        subscribers = Subscription.objects.all()
        if settings.EMAIL_DEBUG:
            subscribers = subscribers.filter(admin=True)

        for subscriber in subscribers:
            to = [subscriber.user_email]
            current_site = Site.objects.get_current()
            context['unsubscribe_url'] = 'http://%s%s?user_email=%s&val_token=%s' % (current_site.domain, reverse('unsubscribe_newsletter'), subscriber.user_email, subscriber.val_token)
            context['static_url'] = 'http://%s%s' % (current_site.domain, settings.STATIC_URL)

            email = utils.mail_wrapper(subject, context, from_email, to, template_txt, template_html)
            emails.append(email)

        connection = mail.get_connection(fail_silently=True)
        connection.send_messages(emails)

        newsletter.sent = True
        newsletter.save()

send_newsletter.short_description = (u'Enviar newsletter')


class NewsletterAdmin(admin.ModelAdmin):
    model = Newsletter
    list_display = ('__unicode__', 'created_date', 'sent', 'sent_date')
    actions = [send_newsletter]

admin.site.register(Newsletter, NewsletterAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    list_display = ('user_email', 'admin')

admin.site.register(Subscription, SubscriptionAdmin)

