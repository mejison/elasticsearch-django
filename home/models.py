from django.db import models

class ElasticDemo(models.Model):
    customers_id = models.IntegerField()
    customers_vat_id_status = models.IntegerField()
    customers_status = models.IntegerField()
    customers_firstname = models.CharField(max_length=255)
    customers_lastname = models.CharField(max_length=255)
    customers_dob = models.CharField(max_length=255)
    customers_email_address = models.CharField(max_length=255)
    customers_default_address_id = models.IntegerField()
    customers_telephone = models.CharField(max_length=255)
    customers_password = models.CharField(max_length=255)
    customers_newsletter =models.CharField(max_length=255)
    customers_newsletter_mode = models.IntegerField()
    member_flag = models.CharField(max_length=1)
    delete_user = models.CharField(max_length=1)
    account_type = models.CharField(max_length=1)
    refferers_id = models.CharField(max_length=1)
    customers_date_added = models.CharField(max_length=255)
    customers_last_modified = models.CharField(max_length=255)
    login_tries =  models.CharField(max_length=255)
    login_time = models.CharField(max_length=255)
    customers_personal_discount = models.CharField(max_length=255)