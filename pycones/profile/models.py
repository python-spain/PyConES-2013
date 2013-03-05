# -*- coding: utf-8 -*-

from django.db import models


class Profile(models.Model):
    user = models.OneToOneField("auth.User", related_name="profile")
    newsletter_token = models.CharField(max_length=40, blank=True)

    def __unicode__(self):
        return unicode(self.user)
