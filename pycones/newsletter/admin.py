from django.contrib import admin

from pycones.newsletter.models import Newsletter,Article,Subscription

admin.site.register(Newsletter)
admin.site.register(Article)
admin.site.register(Subscription)

