# -*- coding: utf-8 -*-

from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100,
                    blank=True, null=True)
    web = models.CharField(max_length=100,
                    blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = u'ponente'
        ordering = 'name'

    def __unicode__(self):
        return self.name

TALK_LEVELS = (
    ('basic', u'Básico'),
    ('advanced', u'Avanzado'),
    ('scientific', u'Científico'),
)

class Talk(models.Model):
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=100, choices=TALK_LEVELS,
                        blank=True, null=True)
    speaker = models.ForeignKey(Speaker)
    speakers = models.ManyToManyField(Speaker, related_name='speakers')
    abstract = models.TextField(blank=True, null=True)
    selected = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'charla'

    def __unicode__(self):
        return self.title

