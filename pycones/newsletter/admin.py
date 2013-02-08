from django.contrib import admin

from symposion.newsletter.models import Newsletter,Article

admin.site.Register(Newsletter)
admin.site.Register(Article)


