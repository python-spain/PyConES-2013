# -*- coding: utf-8 -*-

from django.db import models

SPONSOR_LEVELS = (
    ('diamond', 'DIAMANTE'),
    ('platinum', 'PLATINO'),
    ('gold', 'ORO'),
    ('silver', 'PLATA'),
)

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=255)
    level = models.CharField(max_length=100, choices=SPONSOR_LEVELS)
    image = models.ImageField(upload_to='.')

    class Meta:
        verbose_name = 'patrocinador'
        verbose_name_plural = 'patrocinadores'

    def __unicode__(self):
        return self.name
