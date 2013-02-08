from django.db import models
from django.shortcuts import get_object_or_404

class ArticleManager(models.Manager):
    def get_article_by_path(self,article_path):
        """
        Method to get an article or entry by path field.
        If path is not exist 404Exception will be raised
        """
        article_queryset = super(ArticleManager,self).get_query_set()
        article = article_queryset.get_object_or_404(
                    path__iexact=article_path,
                    visible=True,
                    newsletter__active=True)
        return article

    def get_last_articles(self):
        """
        Method to get last 5 articles added to active newsletter
        """
        article_queryset = super(ArticleManager,self).get_query_set()
        articles = article_queryset.filter(
                    visible=True,
                    newsletter__visible=True
                    ).order_by('-create_date')[:5]
        return articles

    def get_articles_per_page(self,page_number):
        """
        Method to get 5 articles per page number( 5 articles per page )
        For example:
            if page=1 articles 6-10
            if page=2 articles 11-15
        To calculate first article we use: 5 * page_number + 1
        To calculate last article we use: first_article + 4
        """
        first_article = (page_number * 5 + 1)
        last_article = (first_article + 4)
        article_queryset = super(ArticleManager,self).get_query_set()
        articles = article_queryset.filter(
                    visible=True,
                    newsletter__visible=True
                    ).order_by('-create_date')[first_article:last_article]
        return articles

    def get_articles_per_year(self,year):
        """
        Method to get articles per year
        """
        article_queryset = super(ArticleManager,self).get_query_set()
        articles = article_queryset.filter(
                    visible=True,
                    newsletter__visible=True,
                    create_date__year=year
                    ).order_by('-create_date')
        return articles

    def get_articles_per_month(self):
        """
        Method to get articles per year and month
        """
        article_queryset = super(ArticleManager,self).get_query_set()
        articles = article_queryset.filter(
                    visible=True,
                    newsletter__visible=True,
                    create_date__year=year,
                    create_date__month=month
                    ).order_by('-create_date')
        return articles


