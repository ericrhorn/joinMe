from multiprocessing import context
from django.shortcuts import render
from events.models import Event, Venue

# Create your views here.

def home_screen_view(request, *args, **kwargs):
    context={}
    event_list = Event.objects.all()
    context['event_list'] = event_list
    # attending = Event.objects.get('join_event')
    # context['attending'] = attending
    return render(request, "home.html", context)


# def dashboard_view(request, *args, **kwargs):
#     # context = {}
#     event_list = Event.objects.all()
#     return render(request, "users/dashboard.html", {'event_list' : event_list})
#     # return render(request, "users/dashboard.html")