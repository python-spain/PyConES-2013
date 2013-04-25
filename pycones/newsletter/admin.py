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
        subject = newsletter.title
        template = 'newsletter_mail.html'
        context = {'newsleter': newsletter}
        to = [s.user_email for s in Subscription.objects.all()]
        utils.send_mail_wrapper(subject, template, context, to)
        newsletter.sent = True
        newsletter.save()

send_newsletter.short_description = (u'Enviar newsletter')


class NewsletterAdmin(admin.ModelAdmin):
    model = Newsletter
    list_display = ('__unicode__', 'created_date', 'sent', 'sent_date')
    actions = [send_newsletter]

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Subscription)

