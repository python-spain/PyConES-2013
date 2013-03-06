# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404


def get_or_create_active_newsletter():
    current_active_nl = getattr(settings, 'ACTIVE_NEWSLETTER', '2013')
    try:
        newsletter = Newsletter.objects.get(name=current_active_nl)
    except Newsletter.DoesNotExist:
        newsletter = Newsletter.objects.create(name=current_active_nl)

    return newsletter


class ArticleManager(models.Manager):
    def get_article_by_path(self, article_path):
        """
        Method to get an article or entry by path field.
        If path is not exist 404Exception will be raised
        """
        queryset = super(ArticleManager,self).get_query_set()

        article = queryset.get_object_or_404(
                    path__iexact=article_path, visible=True,
                    newsletter=get_or_create_active_newsletter())

        return article

    def get_last_articles(self):
        """
        Method to get last 5 articles added to active newsletter
        """
        article_queryset = super(ArticleManager,self).get_query_set()
        articles = article_queryset\
            .filter(visible=True,newsletter=get_or_create_active_newsletter())\
            .order_by('-create_date')[:5]

        return articles

    def get_articles_per_page(self, page_number):
        """
        Method to get 5 articles per page number( 5 articles per page )
        For example:
            if page=1 articles 6-10
            if page=2 articles 11-15
        To calculate first article we use: 5 * page_number + 1
        To calculate last article we use: first_article + 4
        """

        # FIXME: use django pagination instead of manual pagination
        first_article = (page_number * 5 + 1)
        last_article = (first_article + 4)

        queryset = super(ArticleManager,self).get_query_set()

        articles = queryset\
            .filter(visible=True, newsletter=get_or_create_active_newsletter())\
            .order_by('-create_date')[first_article:last_article]

        return articles

    def get_articles_per_year(self,year):
        """
        Method to get articles per year
        """
        queryset = super(ArticleManager,self).get_query_set()

        articles = queryset.filter(
                    visible=True, newsletter=get_or_create_active_newsletter(),
                    create_date__year=year).order_by('-create_date')

        return articles

    def get_articles_per_month(self):
        """
        Method to get articles per year and month
        """
        queryset = super(ArticleManager,self).get_query_set()
        articles = queryset.filter(
                        visible=True, newsletter=get_or_create_active_newsletter(),
                        create_date__year=year, create_date__month=month
                    ).order_by('-create_date')

        return articles


class Newsletter(models.Model):
    name = models.CharField(max_length=255, unique=True)
    create_date = models.DateTimeField(editable=False, auto_now_add=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    create_date = models.DateTimeField(editable=False, auto_now_add=True)

    path = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()

    update_date = models.DateTimeField(editable=False, auto_now=True)
    publish_date = models.DateTimeField()
    visible = models.BooleanField(default=False)

    objects = ArticleManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["create_date"]


class Subscription(models.Model):
    user = models.ForeignKey("auth.User", related_name="subscriptions")
    newsletter = models.ForeignKey("Newsletter", related_name="subscriptions")

    class Meta:
        unique_together = ('user', 'newsletter')
