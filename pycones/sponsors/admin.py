# -*- coding: utf-8 -*-
from django.contrib import admin
from pycones.sponsors.models import Sponsor, Prospect

admin.site.register(Sponsor)

class ProspectAdmin(admin.ModelAdmin):
    list_display = ('company', 'previous_interest', 'already_contacted', 'status', 'accepted_level', 'user_in_charge')
    list_filter = ('previous_interest', 'already_contacted', 'status', 'user_in_charge', 'accepted_level', 'invoice_status')


admin.site.register(Prospect, ProspectAdmin)
