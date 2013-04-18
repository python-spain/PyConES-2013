from django.contrib import admin

from pycones.newsletter.models import Newsletter,Article,Subscription

admin.site.register(Article)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'create_date')

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Subscription)

