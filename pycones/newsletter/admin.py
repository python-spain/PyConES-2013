from django.contrib import admin

from pycones.newsletter.models import Newsletter, Article, Subscription

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'created_date', 'visible')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    model = Newsletter
    list_display = ('__unicode__', 'created_date', 'sent')

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Subscription)

