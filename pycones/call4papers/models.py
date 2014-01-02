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
        ordering = ['name',]

    def __unicode__(self):
        return self.name

TALK_LEVELS = (
    ('basic', u'Básico'),
    ('advanced', u'Avanzado'),
    ('scientific', u'Científico'),
)
SC_DAY = (('s', u'Sábado'), ('d', u'Domingo'))
SC_TRACK = (('b', u'Básico'), ('a', u'Avanzado'), ('c', u'Científico'))
SC_HOUR = (
    ('9', u'9'),
    ('10', u'10'),
    ('11', u'11:30'),
    ('12', u'12:30'),
    ('15', u'15'),
    ('16', u'16'),
    ('17', u'17:30'),
    ('18', u'18:30'),
)

class Talk(models.Model):
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=100, choices=TALK_LEVELS,
                        blank=True, null=True)
    speakers = models.ManyToManyField(Speaker, related_name='talks')
    abstract = models.TextField(blank=True, null=True)
    selected = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    sc_hour = models.CharField(max_length=2,
                        blank=True, null=True,
                        choices=SC_HOUR)
    sc_track = models.CharField(max_length=1,
                        blank=True, null=True,
                        choices=SC_TRACK)
    sc_day = models.CharField(max_length=1,
                        blank=True, null=True,
                        choices=SC_DAY)
    slot = models.CharField(max_length=10,
                        blank=True, null=True,
                        unique=True)
    video_url = models.CharField(max_length=255,
                        blank=True, null=True)

    def _slot(self):
        return u'{}{}{}'.format(self.sc_track, self.sc_day, self.sc_hour)

    class Meta:
        verbose_name = u'charla'
        unique_together = ['sc_track', 'sc_day', 'sc_hour']

    def __unicode__(self):
        return self.title

    def save(self):
        if self.sc_day != None and self.sc_track != None and self.sc_hour != None:
            self.slot = self._slot()
        super(Talk, self).save()



