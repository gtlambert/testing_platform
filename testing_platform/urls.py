"""testing_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'test.views.index', name='home'),
    url(r'^tests$', 'test.views.view_tests', name='tests'),
    
    
    # run tests with post requests
    url(r'^review-mismatch$', 'test.views.review_mismatch'),
    url(r'^content$', 'test.views.content'),
    
    # view tests
    url(r'^review-mismatch-test/(?P<test_identifier>\d+)$', 
        'test.views.view_rating_mismatch_test', name='review-mismatch-test'),

]
