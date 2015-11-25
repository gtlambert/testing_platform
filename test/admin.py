from django.contrib import admin

from .models import RatingMismatchTest


class RatingMismatchTestAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'created_at',
                    'num_products_tested', 
                    'number_reviewers_matches',
                    'number_reviewers_mismatches',
                    'review_rating_matches',
                    'review_rating_mismatches',
                    ]

admin.site.register(RatingMismatchTest, RatingMismatchTestAdmin)