from django.forms import ModelForm

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