from django.shortcuts import render
from django.http import JsonResponse
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
    SearchFilterBackend,
    DefaultOrderingFilterBackend,
)

def import_data_from_file():
    file = open("./data.json")
    items = json.load(file)
    for item in items['users']:
        ElasticDemo.objects.create(
            customers_id = item['customers_id'],
            customers_vat_id_status = item['customers_vat_id_status'],
            customers_status = item['customers_status'],
            customers_firstname = item['customers_firstname'],
            customers_lastname = item['customers_lastname'],
            customers_dob = item['customers_dob'],
            customers_email_address = item['customers_email_address'],
            customers_default_address_id = item['customers_default_address_id'],
            customers_telephone = item['customers_telephone'],
            customers_password = item['customers_password'],
            customers_newsletter = item['customers_newsletter'],
            customers_newsletter_mode = item['customers_newsletter_mode'],
            member_flag = item['member_flag'],
            delete_user = item['delete_user'],
            account_type = item['account_type'],
            refferers_id = item['refferers_id'],
            customers_date_added = item['customers_date_added'],
            customers_last_modified = item['customers_last_modified'],
            login_tries = item['login_tries'],
            login_time = item['login_time'],
            customers_personal_discount = item['customers_personal_discount']
        )
    file.close()

def index(request):
    import_data_from_file()
    return JsonResponse({'status' : 200})




class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    lookup_field = 'id'
    fielddata=True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
   
    search_fields = (
        # 'customers_id',
        'customers_firstname',
        'customers_lastname',
        'customers_dob',
        'customers_email_address',
        'customers_telephone',
    )
    
    multi_match_search_fields = ()

    filter_fields = {
        # 'customers_id': 'customers_id',
        'customers_firstname': 'customers_firstname.raw',
        'customers_lastname': 'customers_lastname.raw',
        'customers_dob': 'customers_dob.raw',
        'customers_email_address': 'customers_email_address.raw',
        'customers_telephone': 'customers_telephone.raw',
    }

    ordering_fields = {
        'id': None,
        'customers_id': None,
        'customers_firstname': None,
        'customers_lastname': None,
        'customers_dob': None,
        'customers_email_address': None,
        'customers_telephone': None,
    }

    ordering = ('id')
