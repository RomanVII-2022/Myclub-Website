from django import forms
from .models import Venue, Event


class AddVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address', 'image')


        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'web':forms.URLInput(attrs={'class':'form-control'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control'}),

        }



class AddEventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'description', 'attendees')


        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'event_date':forms.TextInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD HH:MM:SS'}),
            'venue':forms.Select(attrs={'class':'form-control'}),
            'manager':forms.Select(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control'}),

        }


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'description', 'attendees')


        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'event_date':forms.TextInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD HH:MM:SS'}),
            'venue':forms.Select(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control'}),

        }


