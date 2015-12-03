import json
import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lxml import etree

from .models import RatingMismatchTest, MismatchTestProduct


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def review_mismatch(request):
    content_type = request.POST['contentType']
    print('get to here')
    r = requests.get(
        'http://test.uberated.zone:8443/api/retailer-products/exported/ids')
    print('made the first request')
    print('######################')
    print('######################')
    print('######################')
    print('######################')
    print('######################')
    print('######################')
    print('######################')
    print('######################')
    print('######################')
    print('######################')
    print('the status code is')
    data = json.loads(r.content)
    data = data['variables'][0]['values']
    product_ids = [prod_id[0] for prod_id in data]
    
    test = RatingMismatchTest.objects.create(
        num_products=len(product_ids),
        content_type=content_type
    )
        
    for product_id in product_ids[:200]: # slice to limit server calls
        test_product = MismatchTestProduct.objects.create(
            parent_test=RatingMismatchTest.objects.get(id=test.id),
            product_id=product_id,
        )
        try:
            r = requests.get(
                'http://test.uberated.zone:8443/api/widgetdata/live/shopDirect/{}'.format(product_id))
            data = json.loads(r.content)
    
            tab_number_reviewers = data['ubNoReviewers']
            tab_rating = data['ubRating']
            r = requests.get(
                'http://test.uberated.zone:8443/content/overview/{}'.format(data['ubProductId']))
            tree = etree.HTML(r.text)
    
            widget_number_reviewers = tree.xpath('//div[@class="r"]/p/text()')
            dud, widget_number_reviewers = widget_number_reviewers[0].strip().rsplit(' ', 1)
            widget_number_reviewers = int(widget_number_reviewers)
            widget_rating = tree.xpath('//div[@class="perc-h"]/h4/text()')
            widget_rating = int(widget_rating[0].strip().replace('%', ''))
            
            # assign data to MismatchTestProduct model
            test_product.tab_number_reviewers = tab_number_reviewers
            test_product.widget_number_reviewers = widget_number_reviewers
            test_product.tab_rating = tab_rating
            test_product.widget_rating = widget_rating
            
            # TEST
            if tab_number_reviewers == widget_number_reviewers:
                test.number_reviewers_matches += 1
            else:
                test.number_reviewers_mismatches += 1
                test_product.result=False
            
            # TEST 2
            if tab_rating == widget_rating:
                test.review_rating_matches += 1
            else:
                test.review_rating_mismatches += 1
                test_product.result=False
        except:
            print(product_id)
        test_product.save() 
        test.num_products_tested += 1
        test.save()
        
    # set test status to not active when finished
    test.is_active = False
    test.save()
    return HttpResponse('some data')

def content(request):
    content_type = request.POST['contentType']
    r = requests.get(
        'http://test.uberated.zone:8443/api/admin/testing/exported/all')
    return HttpResponse('this is some data from the content test')
    

def view_tests(request):
    rating_mismatch_tests = RatingMismatchTest.objects.all().order_by('-created_at')
    print('get to here')
    context_dict = {
        'rating_mismatch_tests': rating_mismatch_tests,
    }
    
    return render(request, 'tests.html', context=context_dict)

def view_rating_mismatch_test(request, test_identifier):
    rating_mismatch_test = RatingMismatchTest.objects.get(id=test_identifier)
    test_products_pass = MismatchTestProduct.objects.filter(
        parent_test=rating_mismatch_test,
        result=True,
    )
    test_products_fail = MismatchTestProduct.objects.filter(
        parent_test=rating_mismatch_test,
        result=False,
    )
    context_dict = {
        'rating_mismatch_test': rating_mismatch_test,
        'test_products_pass': test_products_pass,
        'test_products_fail': test_products_fail,
    }
    return render(request, 'test.html', context=context_dict)
 
# route in  
# http://cms.uberated.zone/api/retailer-products/exported/ids
# http://scripts.uberated.zone/api/widgetdata/shopDirect/4XENF
# cms.uberated.zone/content/overview/55c4b5047b562e5509fd5b2a