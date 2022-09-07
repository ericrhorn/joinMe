from multiprocessing import context
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from events.forms import eventUpdateForm, newEventForm, newVenueForm
from events.models import Event, Venue
from users.models import Account




def new_event_view(request, *args, **kwargs):
    submitted = False
    venue_list = Venue.objects.all()
    if request.method == "POST":
        form = newEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            user = request.user
            event.host = user
            event.save()
            return HttpResponseRedirect('/event/new_event?submitted=True')
    else:
        form = newEventForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "new_event.html", {'venue_list' : venue_list, 'form' : form, 'submitted' : submitted})



def new_venue_view(request, *args, **kwargs):
    submitted = False
    if request.method == "POST":
        form = newVenueForm(request.POST)
        if form.is_valid():
            venue = form.save(commit=False)
            user = request.user
            venue.owner = user
            venue.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = newVenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "new_venue.html", {'form' : form, 'submitted' : submitted})


def update_event(request, event_id):
    # updated = False
    # context = {}
    venue_list = Venue.objects.all()
    # context['venue_list'] = venue_list
    event = Event.objects.get(pk=event_id)
    # context['eevnt'] = event
    form =eventUpdateForm(request.POST or None, instance=event,
        initial={
            'id' : event.pk,
            'event_name' : event.event_name,
            'price' : event.price,
            'star_date' : event.start_date,
            'end_date' : event.end_date,
            'start_time' : event.start_time,
            'end_time' : event.end_time,
            'description' : event.description,
            'event_notes' : event.event_notes,
            'private_event' : event.private_event,
            'public_event' : event.public_event,
            'venue' : event.venue,
        }
    )
    # context['form'] = form
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "update_event.html", {'event' : event, 'form' : form , 'venue_list' : venue_list})



# like, add user info
def join_event_view(request, pk):
    event = get_object_or_404(Event, id=request.POST.get('event_id'))
    event.join_event.add(request.user.id)
    return redirect('/account/dashboard')


def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('/')