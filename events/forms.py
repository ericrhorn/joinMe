from django.forms import ModelForm
from django import forms

from events.models import Event, Venue

class newVenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'state', 'city', 'zip_code', 'web_address', 'venue_notes', 'private_venue', 'public_venue')



class newEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'price', 'start_date', 'end_date', 'start_time', 'end_time', 'description', 'event_notes', 'private_event', 'public_event', 'venue')


class eventUpdateForm(ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'price', 'start_date', 'end_date', 'start_time', 'end_time', 'description', 'event_notes', 'private_event', 'public_event', 'venue')
        labels = {
            'event_name' : 'Event Name',
            'price' : 'Price',
            'start_date' : 'Start Date',
            'end_date' : 'End Date',
            'start_time' : 'Start Time',
            'end_time' : 'End Time',
            'description' : 'Description',
            'event_notes' : 'Event Notes',
            'private_event' : 'Private Event',
            'public_event' : 'Public Event',
            'venue' : 'Venue',
        }
        widgets = {
            'event_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control'}),
            'start_date' : forms.TextInput(attrs={'class' : 'form-control'}),
            'end_date' : forms.TextInput(attrs={'class' : 'form-control'}),
            'start_time' : forms.TextInput(attrs={'class' : 'form-control'}),
            'end_time' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control', 'rows':3}),
            'event_notes' : forms.Textarea(attrs={'class' : 'form-control', 'rows':3}),
            # 'private_event' : forms.BooleanField(attrs={'class' : 'form-control'}),
            # 'public_event' : forms.BooleanField(attrs={'class' : 'form-control'}),
            'venue' : forms.Select(attrs={'class' : 'form-select'}),
        }