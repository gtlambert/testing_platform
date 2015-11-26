import datetime

from django import forms
from django.db import models

####################################
######### TESTS ####################
####################################

class ContentTest(models.Model):
    num_products = models.IntegerField(blank=True)
    num_products_tested = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    datetime_finished = models.DateTimeField(blank=False, null=True)
    is_active = models.BooleanField(default=True)
    content_type = models.CharField(blank=True, max_length=100)


class ContentTestProduct(models.Model):
    pass
    

# need to understand blank, null, default etc
class RatingMismatchTest(models.Model):
    num_products = models.IntegerField(blank=True)
    num_products_tested = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    datetime_finished = models.DateTimeField(blank=False, null=True)
    is_active = models.BooleanField(default=True)
    content_type = models.CharField(blank=True, max_length=100)

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
    