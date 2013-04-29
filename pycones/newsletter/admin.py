# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from pycones import utils
from pycones.newsletter.models import Newsletter, Article, Subscription

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'created_date', 'visible')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)

def send_newsletter(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    for newsletter in queryset:
        subject = '[PyConEs] %s' % newsletter.title
        template = 'newsletter/newsletter_mail.html'
        context = {'newsleter': newsletter}
        from_email = settings.EMAIL_HOST_USER
        context = {'newsletter': newsletter}
        template_txt = 'newsletter/newsletter_mail.txt'
        template_html =  'newsletter/newsletter_mail.html'
        to = [s.user_email for s in Subscription.objects.all()]
        utils.send_mail_wrapper(subject, context, from_email, to, template_txt, template_html)
        newsletter.sent = True
        newsletter.save()

send_newsletter.short_description = (u'Enviar newsletter')


class NewsletterAdmin(admin.ModelAdmin):
    model = Newsletter
    list_display = ('__unicode__', 'created_date', 'sent', 'sent_date')
    actions = [send_newsletter]

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Subscription)

