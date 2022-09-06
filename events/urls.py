from django.urls import path
from events.views import (
    delete_event,
    update_event,
    new_event_view,
    new_venue_view,
)

app_name = 'events'

urlpatterns = [
    path('<int:event_id>/delete', delete_event, name='delete_event'),
    path('<int:event_id>/edit', update_event, name='update_event'),
    path('new_event/', new_event_view, name='new_event'),
    path('new_venue/', new_venue_view, name='new_venue'),
    # path('new_venue/', new_venue_view, name='new_venue'),
]