# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


SPONSOR_LEVELS = (
    ('diamond', u'DIAMANTE'),
    ('platinum', u'PLATINO'),
    ('gold', u'ORO'),
    ('silver', u'PLATA'),
    ('bronze', u'BRONZE'),
)

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=255)
    level = models.CharField(max_length=100, choices=SPONSOR_LEVELS)
    image = models.ImageField(upload_to='.')

    class Meta:
        verbose_name = u'patrocinador'
        verbose_name_plural = u'patrocinadores'

    def __unicode__(self):
        return self.name


STATUS_LEVELS = (
    ('reject', u'Rechazo'),
    ('objection', u'Objeción'),
    ('waiting', u'A la espera'),
    ('accepted', u'Aceptado'),
)

ACCEPTED_LEVEL = (('none', u'NONE'),) + SPONSOR_LEVELS

INVOICE_STATUS = (
    ('none', u'None'),
    ('sent', u'Enviada'),
    ('aceptada', u'Aceptada'),
    ('recibida', u'Recibida'),
)

class Prospect(models.Model):
    company = models.CharField(max_length=100)
    web = models.CharField(max_length=255, blank=True, null=True)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    email =  models.CharField(max_length=100)
    previous_interest = models.BooleanField(default=False)
    already_contacted = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=STATUS_LEVELS,
                        null=True, blank=True)
    user_in_charge = models.ForeignKey(User, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    accepted_level = models.CharField(max_length=100, choices=ACCEPTED_LEVEL, default=ACCEPTED_LEVEL[0])
    invoice_status = models.CharField(max_length=100, choices=INVOICE_STATUS, default=INVOICE_STATUS[0])

    class Meta:
        verbose_name = u'candidato'
        verbose_name_plural = u'candidatos'

    def __unicode__(self):
        return self.company


