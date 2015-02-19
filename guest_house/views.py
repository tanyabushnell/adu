from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from models import Reservation
from json import dumps, loads
from django.http import HttpResponse
# from guest_house.forms import ReservationForm
from datetime import date
from dateutil import parser

def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    reservation_list = Reservation.objects.all()
    context_dict = {'reservations': reservation_list}

    # Render the response and send it back!
    return render_to_response('index.html', context_dict, context)

def thank_you(request):
    return render_to_response( 'thank_you.html')

def test(request):
    return render_to_response( 'test.html')

def dom(request):
    if request.method =="POST":
        print request.POST
        reservation = Reservation()
        reservation.contact_first_name = request.POST["contact_first_name"]
        reservation.contact_last_name = request.POST["contact_last_name"]
        reservation.contact_email_address = request.POST["contact_email_address"]
        reservation.contact_phone_number = request.POST["contact_phone_number"]

        reservation.check_in_date = parser.parse(request.POST["check_in_date"])

        reservation.check_out_date = parser.parse(request.POST["check_out_date"])

        reservation.number_of_nights  = int(request.POST["number_of_nights"])
        reservation.number_of_adults = int(request.POST["number_of_adults"])
        reservation.number_of_children = int(request.POST["number_of_children"])

        reservation.message_to_hosts = request.POST["message_to_hosts"]

        reservation.calculated_rate = float(request.POST["calculated_rate"])
        reservation.cleaning_fee = float(request.POST["cleaning_fee"])
        reservation.tax = float(request.POST["tax"])
        reservation.payment_total = float(request.POST["payment_total"])
        reservation.save()
        return redirect("thank_you")

    return render(request, 'dom.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ajax(request):
    if request.method == "POST":
        event = Reservation()
        event.contact_first_name = request.POST["name"]
        event.contact_last_name = request.POST["name"]
        event.check_in_date = date.today()
        event.save()

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    reservation_list = Reservation.objects.all()

    reservation = list(Reservation.objects.all())
    reservation_list = []
    for r in reservation:
        reservation_list.append({

            "first_name": r.contact_first_name
        })
    # Render the response and send it back!
    return HttpResponse(dumps(reservation_list, indent=4), content_type="application/json")

def add_reservation(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = ReservationForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)

        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ReservationForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('guest_house/add_reservation.html', {'form': form}, context)
