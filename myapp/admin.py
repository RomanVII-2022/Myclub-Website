from django.contrib import admin
from .models import Event, Venue, MyClubUser

# Register your models here.
#admin.site.register(Event)
#admin.site.register(Venue)
admin.site.register(MyClubUser)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name', )
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'manager', 'description', 'attendees', 'approved')
    list_display = ('name', 'venue', 'event_date')
    ordering = ('event_date',)
    search_fields = ('name', 'venue')
    list_filter = ('event_date', 'venue')

