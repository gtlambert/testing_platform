import datetime

from django.db import models


class ExportedContentTest(models.Model):
    pass


class ApprovedContentTest(models.Model):
    pass
    

# need to understand blank, null, default etc
class RatingMismatchTest(models.Model):
    num_products = models.IntegerField(blank=True)
    num_products_tested = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    datetime_finished = models.DateTimeField(blank=False, null=True)
    is_active = models.BooleanField(default=True)

    # TEST 1
    number_reviewers_matches = models.IntegerField(blank=False, default=0)
    number_reviewers_mismatches = models.IntegerField(blank=False, default=0)
    
    
    # TEST 2
    review_rating_matches = models.IntegerField(blank=False, default=0)
    review_rating_mismatches = models.IntegerField(blank=False, default=0)
    
    # need a notes field which can be updated by user
