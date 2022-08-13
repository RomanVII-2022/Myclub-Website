from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import AddVenueForm, AddEventForm, AddEventAdminForm
from django.contrib import messages
from django.http import HttpResponse, FileResponse
import csv
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.paginator import Paginator


def venuepdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append("===================================")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue.pdf')




def venuecsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=venues.csv'
    
    writer = csv.writer(response)
    venues = Venue.objects.all()
    writer.writerow(['Venue Name', 'Address', 'Zip Code', 'Phone', 'Website', 'Email Address'])
    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email_address])
    
    return response


def venuetext(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition']='attachment; filename=venues.txt'
    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(f'{venue.name}\n {venue.address}\n {venue.zip_code}\n {venue.phone}\n {venue.web}\n {venue.email_address}\n\n\n')
    
    response.writelines(lines)
    return response


# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'John'
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    

    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )

    now = datetime.now()
    current_year = now.year

    time = now.strftime('%H:%M:%S')
    
    return render(request, 'home.html', {
        'name':name, 
        'year':year, 
        'month':month, 
        'month_number':month_number,
        'cal':cal,
        'current_year':current_year,
        'time':time,
        })


def eventview(request):
    events = Event.objects.all().order_by('name')
    return render(request, 'events.html', {'events':events})


def addvenueview(request):
    form = AddVenueForm()
    if request.method == 'POST':
        form = AddVenueForm(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner = request.user.id
            venue.save()
            #form.save()
            messages.success(request, "Venue has been added successfully")
            return redirect('addvenue')
            
    else:
        form =AddVenueForm()

    return render(request, 'addvenue.html', {'form':form})


def venuelistview(request):
    p = Paginator(Venue.objects.all(), 1)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = "a" * venues.paginator.num_pages
    return render(request, 'venuelist.html', {'venues':venues, 'nums':nums})


def venuedetailview(request, venue_id):
    venues = Venue.objects.get(pk=venue_id)
    return render(request, 'venuedetail.html', {'venues':venues})


def eventdetailview(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'eventdetail.html', {'event':event})


def searchvenueview(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
    return render(request, 'searchvenue.html', {'searched':searched, 'venues':venues})


def updatevenueview(request, venue_id):
    venues = Venue.objects.get(pk=venue_id)
    form = AddVenueForm(request.POST or None, request.FILES or None, instance=venues)
    if form.is_valid():
        form.save()
        return redirect('venuelist')
    return render(request, 'updatevenue.html', {'form':form})


def deletevenueview(request, venue_id):
    venues = Venue.objects.get(pk=venue_id)
    if request.method == "POST":
        venues.delete()
        return redirect('venuelist')

    return render(request, 'deletevenue.html', {'venues':venues})


def addeventview(request):
    if request.method == "POST":
        if request.user.is_superuser:
            form = AddEventAdminForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('addevent')
        else:
            form = AddEventForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.manager = request.user
                event.save()
                return redirect('addevent')
    else:
        if request.user.is_superuser:
            form = AddEventAdminForm()
        else:
            form = AddEventForm()
    return render(request, 'addevent.html', {'form':form})


def editeventview(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user.is_superuser:
        form = AddEventAdminForm(request.POST or None, instance=event)
    else:
        form = AddEventForm(request.POST or None, instance=event)
    
    if form.is_valid():
        form.save()
        return redirect('events')
        
    return render(request, 'editevent.html', {'form':form})


def searcheventview(request):
    if request.method == "POST":
        searched = request.POST['searched']
        events = Event.objects.filter(name__contains=searched)
        
    return render(request, 'searchevent.html', {'events':events})


def adminpprovalview(request):
    events = Event.objects.all()
    venues = Venue.objects.all()
    venue_number = len(venues)
    event_number = len(events)

    if request.method == "POST":
        id_list = request.POST.getlist('boxes')
        events.update(approved=False)
        for x in id_list:
            Event.objects.filter(pk=int(x)).update(approved=True)
        return redirect('events')
    return render(request, 'adminapproval.html', {'events':events, 'venue_number':venue_number, 'event_number':event_number})



def eventvenuecategoryview(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    events = Event.objects.filter(venue = venue)
    return render(request, 'eventvenuecategory.html', {'events':events})