from django.contrib import admin

from .models import RatingMismatchTest, ContentTest


class RatingMismatchTestAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'created_at',
                    'num_products_tested',
                    'number_reviewers_matches',
                    'number_reviewers_mismatches',
                    'review_rating_matches',
                    'review_rating_mismatches',
                    ]


class ContentTestAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'created_at',
                    'num_products_tested',
    ]

admin.site.register(RatingMismatchTest, RatingMismatchTestAdmin)
admin.site.register(ContentTest, ContentTestAdmin)
