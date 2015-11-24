import json
import requests

from django.shortcuts import render
from django.http import HttpResponse

from .models import RatingMismatchTest


def index(request):
    return render(request, 'index.html')


def review_mismatch(request):
    r = requests.get(
        'http://cms.uberated.zone/api/retailer-products/exported/ids')
    data = json.loads(r.content)
    data = data['variables'][0]['values']
    product_ids = [prod_id[0] for prod_id in data]
    
    print('get to here')
    RatingMismatchTest.objects.create(num_products=len(product_ids)).save()
    print('and to here')
    return HttpResponse('some data')
    
    
# route in  
# http://cms.uberated.zone/api/retailer-products/exported/ids
# http://scripts.uberated.zone/api/widgetdata/shopDirect/4XENF
# cms.uberated.zone/content/overview/55c4b5047b562e5509fd5b2a