from django.db import models

class Reservation(models.Model):
    contact_first_name = models.CharField(max_length=128)
    contact_last_name = models.CharField(max_length=128)
    contact_email_address = models.CharField(max_length=128)
    contact_phone_number = models.CharField(max_length=128)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_nights = models.IntegerField(max_length=30, default=1)
    number_of_adults = models.IntegerField(max_length=2, default=1)
    number_of_children = models.IntegerField(max_length=2, default=0)
    message_to_hosts = models.TextField(max_length=2000, default="")
    calculated_rate = models.FloatField(default=0.0)
    cleaning_fee = models.FloatField(default=0.0)
    tax = models.FloatField(default=0.0)
    payment_total = models.FloatField(default=0.0)
