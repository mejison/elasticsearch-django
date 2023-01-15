from django_elasticsearch_dsl import (
    Document ,
    fields,
    Index,
)
from .models import ElasticDemo
PUBLISHER_INDEX = Index('elastic_demo')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

@PUBLISHER_INDEX.doc_type
class NewsDocument(Document):

    id = fields.IntegerField(attr='id')

    fielddata=True

    customers_id = fields.IntegerField(attr='customers_id')
    
    customers_vat_id_status = fields.IntegerField()

    customers_status = fields.IntegerField()

    customers_firstname = fields.KeywordField(
        fields={
            'raw': {
                "type": "keyword",
            }
        }
    )

    customers_lastname = fields.KeywordField(
        fields={
            'raw': {
                "type": "keyword",
            }
        }
    )

    customers_dob = fields.KeywordField(
        fields={
            'raw': {
                "type": "keyword",
            }
        }
    )

    customers_email_address = fields.KeywordField(
        fields={
            'raw': {
                "type": "keyword",
            }
        }
    )

    customers_default_address_id = fields.IntegerField(
        fields={
            'raw':{
                'type': 'keyword',
            }
        }
    )

    customers_telephone = fields.KeywordField(
        fields={
            'raw': {
                "type": "keyword",
            }
        }
    )

    customers_password = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
        }
    )

    customers_newsletter = fields.IntegerField()

    customers_newsletter_mode = fields.IntegerField()

    member_flag = fields.IntegerField()

    account_type = fields.IntegerField()

    refferers_id = fields.IntegerField()

    customers_date_added = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
        }
    )
    
    customers_last_modified = fields.DateField()

    login_tries = fields.IntegerField()

    login_time = fields.DateField()

    customers_personal_discount = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
        }
    )

    class Django(object):
        model = ElasticDemo