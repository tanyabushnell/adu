from django.db import models

class Reservation(models.Model):
    contact_first_name = models.CharField(max_length=128)
    contact_last_name = models.CharField(max_length=128)
    contact_email_address = models.CharField(max_length=128)
    contact_phone_number = models.CharField(max_length=128)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_adults = models.IntegerField(default=2)
    number_of_children = models.IntegerField(default=2)
    calculated_rate = models.IntegerField(default=0)