from django import forms
from django.forms import ModelForm
from guest_house.models import Reservation

# create the form class
class ReservationForm(forms.ModelForm):
    contact_first_name = forms.CharField(max_length=128)
    contact_last_name = forms.CharField(max_length=128)
    contact_email_address = forms.CharField(max_length=128)
    contact_phone_number = forms.CharField(max_length=128)
    check_in_date = forms.DateField()
    check_out_date = forms.DateField()
    number_of_nights = forms.IntegerField(max_length=30)
    number_of_adults = forms.IntegerField()
    number_of_children = forms.IntegerField()
    message_to_hosts = forms.Textarea()
    calculated_rate = forms.IntegerField()
    cleaning_fee = forms.IntegerField()
    tax = forms.IntegerField()
    payment_total = forms.IntegerField()

# An inline class to provide additional information on the form.
    class Meta:
# Provide an association between the ModelForm and a model
        model = Reservation
        fields = ["contact_first_name", "contact_last_name", "contact_email_address", "contact_phone_number",
                  "check_in_date", "check_out_date", "number_of_nights","number_of_adults", "number_of_children",
                  "message_to_hosts", "calculated_rate", "cleaning_fee", "tax", "payment_total"]


