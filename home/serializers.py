import json
from .models import ElasticDemo

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *


class NewsDocumentSerializer(DocumentSerializer):

    class Meta(object):
        """Meta options."""
        model = ElasticDemo
        document = NewsDocument
        fields = (
            'customers_id',
            'customers_vat_id_status',
            'customers_status',
            'customers_firstname',
            'customers_lastname',
            'customers_dob',
            'customers_email_address',
            'customers_default_address_id',
            'customers_telephone',
            'customers_password',
            'customers_newsletter',
            'customers_newsletter_mode',
            'delete_user',
            'account_type',
            'refferers_id',
            'customers_date_added',
            'customers_last_modified',
            'login_tries',
            'login_time',
            'customers_personal_discount',
        )
        def get_location(self, obj):
            """Represent location value."""
            try:
                return obj.location.to_dict()
            except:
                return {}