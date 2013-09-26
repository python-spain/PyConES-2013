# -*- coding: utf-8 -*-

from django.contrib import admin
from pycones.call4papers.models import Speaker, Talk

admin.site.register(Speaker)

class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'talk_speakers', 'selected', 'confirmed')
    list_filter = ('level', 'selected', 'confirmed')
    filter_horizontal = ('speakers',)

    def talk_speakers(self, obj):
        return ', '.join([sp.name for sp in obj.speakers.all()])
    talk_speakers.short_description = 'Speakers'

admin.site.register(Talk, TalkAdmin)
