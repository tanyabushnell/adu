from django.db import models

class Reservation(models.Model):
    contact_first_name = models.CharField(max_length=128)
    contact_last_name = models.CharField(max_length=128)
    contact_email_address = models.CharField(max_length=128)
    contact_phone_number = models.CharField(max_length=128)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_nights = models.IntegerField(max_length=30)
    number_of_adults = models.IntegerField(max_length=2)
    number_of_children = models.IntegerField(max_length=2)
    message_to_hosts = models.TextField(max_length=2000)
    calculated_rate = models.IntegerField()
    cleaning_fee = models.IntegerField()
    tax = models.IntegerField()
    payment_total = models.IntegerField()
