from django.db import models

from symposion.newsletter.managers import ArticleManager

class Newsletter(models.Model):
    create_date = models.DateTimeField(editable=False, auto_now_add=True)
    path = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    update_date = models.DateTimeField(editable=False, auto_now=True)
    visible = models.BooleanField(unique=True,default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["update_date","create_date"]

class Article(models.Model):
    create_date = models.DateTimeField(editable=False, auto_now_add=True)
    path = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    text = models.TextField()
    title = models.CharField(max_length=100)
    update_date = models.DateTimeField(editable=False, auto_now=True)
    visible = models.BooleanField(default=False)
    newsletter = models.ForeignKey(Newsletter)

    objects = ArticleManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["create_date"]


