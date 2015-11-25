import json
import requests

from django.shortcuts import render
from django.http import HttpResponse
from lxml import etree

from .models import RatingMismatchTest


def index(request):
    return render(request, 'index.html')


def review_mismatch(request):
    r = requests.get(
        'http://cms.uberated.zone/api/retailer-products/exported/ids')
    data = json.loads(r.content)
    data = data['variables'][0]['values']
    product_ids = [prod_id[0] for prod_id in data]
    
    test = RatingMismatchTest.objects.create(
        num_products=len(product_ids))
        
    for product_id in product_ids[:40]:
        try:
            r = requests.get(
                'http://scripts.uberated.zone/api/widgetdata/shopDirect/{}'.format(product_id))
            data = json.loads(r.content)
    
            
            tab_number_reviewers = data['ubNoReviewers']
            tab_rating = data['ubRating']
            r = requests.get('http://cms.uberated.zone/content/overview/{}'.format(data['ubProductId']))
            tree = etree.HTML(r.text)
    
            widget_number_reviewers = tree.xpath('//div[@class="r"]/p/text()')
            dud, widget_number_reviewers = widget_number_reviewers[0].strip().rsplit(' ', 1)
            widget_number_reviewers = int(widget_number_reviewers)
            widget_rating = tree.xpath('//div[@class="perc-h"]/h4/text()')
            widget_rating = int(widget_rating[0].strip().replace('%', ''))
            
            # TEST
            if tab_number_reviewers == widget_number_reviewers:
                test.number_reviewers_matches += 1
            else:
                test.number_reviewers_mismatches += 1
                print('mismatch {}'.format(product_id))
            
            # TEST 2
            if tab_rating == widget_rating:
                test.review_rating_matches += 1
            else:
                test.review_rating_mismatches += 1
                print('mismatch {}'.format(product_id))
                #raise ValueError('There was an error')
        except:
            print('#############################')
            print('#############################')
            print('#############################')
            print('#############################')
            print('#############################')
            print('error for product')
            print(product_id)
            print('#############################')
            print('#############################')
            print('#############################')
            print('#############################')
            print('#############################') 
        test.num_products_tested += 1
        test.save()
        
    # set test status to not active when finished
    test.is_active = False
    test.save()
    return HttpResponse('some data')

def view_tests(request):
    rating_mismatch_tests = RatingMismatchTest.objects.all().order_by('-datetime_started')
    print('get to here')
    context_dict = {
        'rating_mismatch_tests': rating_mismatch_tests,
    }
    
    return render(request, 'tests.html', context=context_dict)
 
# route in  
# http://cms.uberated.zone/api/retailer-products/exported/ids
# http://scripts.uberated.zone/api/widgetdata/shopDirect/4XENF
# cms.uberated.zone/content/overview/55c4b5047b562e5509fd5b2a