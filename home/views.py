from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests
import json
from home.models import *

from .documents import *
from .serializers import *

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)

def generate_random_data():
    url = 'https://newsapi.org/v2/everything?q=apple&from=2023-01-01&to=2023-01-10&sortBy=popularity&apiKey=2dcac28a33614cb998ca80c8f512a204'
    r = requests.get(url)
    payload = json.loads(r.text)
    for data in payload.get('articles'):
        ElasticDemo.objects.create(
            title = data.get('title'),
            content = data.get('description')
        )

def index(request):
    generate_random_data()
    return JsonResponse({'status' : 200})




class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    lookup_field = 'first_name'
    fielddata=True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
   
    search_fields = (
        'title',
        'content',
    )
    multi_match_search_fields = (
       'title',
        'content',
    )
    filter_fields = {
       'title' : 'title',
        'content' : 'content',
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ( 'id'  ,)
        
  

