# -*- coding: utf-8 -*-

from django.contrib import admin
from pycones.call4papers.models import Speaker, Talk

admin.site.register(Speaker)

class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'level', 'selected',)
    list_filter = ('level', 'selected',)

admin.site.register(Talk, TalkAdmin)
