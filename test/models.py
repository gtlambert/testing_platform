from django.db import models
import requests
from pyquery import PyQuery
import json
import datetime

####################################
######### TESTS ####################
####################################


class BaseTest(models.Model):
    num_products = models.IntegerField(blank=True, default=0)
    num_products_tested = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    datetime_finished = models.DateTimeField(blank=False, null=True)
    is_active = models.BooleanField(default=True)
    content_type = models.CharField(blank=True, max_length=100)

    class Meta:
        abstract = True


class ContentTest(BaseTest):
    external_links_test = models.CharField(blank=True, max_length=100)


class ProductContentTest(BaseTest):
    parent_test = models.ForeignKey(ContentTest)
    product_id = models.CharField(max_length=10)
    content_url = models.CharField(blank=True, max_length=300)
    brand = models.CharField(blank=True, max_length=100)
    model = models.CharField(blank=True, max_length=300)
    number_reviews = models.IntegerField(blank=True, default=-1)
    rating = models.IntegerField(blank=True, default=-1)
    article_ids = models.TextField(blank=True, max_length=10000)
    overview_html = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        r = requests.get(self.content_url)
        pq = PyQuery(r.content)
        self.brand = self.get_brand(pq)
        self.model = self.get_model(pq)
        self.number_reviews = self.get_number_reviews(pq)
        self.rating = self.get_rating(pq)
        self.article_ids = self.get_article_ids(pq)
        self.overview_html = self.get_overview_html(pq)
        super(ProductContentTest, self).save(*args, **kwargs)

    def get_article_ids(self, pq):
        article_ids = [article.attrib['data-id'] for article in pq('.article')]
        return json.dumps(article_ids)

    def get_brand(self, pq):
        return pq('.articles').attr('data-brand')

    def get_model(self, pq):
        return pq('.articles').attr('data-model')

    def get_number_reviews(self, pq):
        return int(pq('.articles').attr('data-length'))

    def get_overview_html(self, pq):
        return pq('.articles').html()

    def get_rating(self, pq):
        return int(pq('.articles').attr('data-ub-rating'))


class ProductArticleTest(models.Model):
    product_content_test = models.ForeignKey(ProductContentTest)
    product_id = models.CharField(max_length=30, blank=True)
    article_id = models.CharField(max_length=30)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    article_url = models.CharField(blank=True, max_length=200)
    overview_html = models.TextField(blank=True)
    body_html = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.overview_html = self.get_overview_html()
        r = requests.get(self.article_url)
        pq = PyQuery(r.content)
        self.body_html = self.get_body_html(pq)
        super(ProductArticleTest, self).save(*args, **kwargs)

    def get_overview_html(self):
        d = PyQuery(self.product_content_test.overview_html)
        return d('.article[data-id="{}"]'.format(self.article_id)).html()

    def get_body_html(self, pq):
        return pq('.ub-content-body').html()


# need to understand blank, null, default etc
class RatingMismatchTest(BaseTest):

    # TEST 1
    number_reviewers_matches = models.IntegerField(blank=False, default=0)
    number_reviewers_mismatches = models.IntegerField(blank=False, default=0)

    # TEST 2
    review_rating_matches = models.IntegerField(blank=False, default=0)
    review_rating_mismatches = models.IntegerField(blank=False, default=0)

    # need a notes field which can be updated by user


class MismatchTestProduct(models.Model):
    parent_test = models.ForeignKey(RatingMismatchTest)
    result = models.BooleanField(default=True)
    product_id = models.CharField(max_length=10)

    tab_number_reviewers = models.IntegerField(default=0)
    widget_number_reviewers = models.IntegerField(default=0)

    tab_rating = models.IntegerField(default=0)
    widget_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.product_id
