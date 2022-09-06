from django.contrib import admin
from events.models import Venue, Event

# class EventAdmin(admin.ModelAdmin):
#     list_filter = ['host']
#     list_display = ['host']
#     search_fields = ['host']
#     readonly_fields = ['host']

#     class Meta:
#         model = Event

admin.site.register(Event)

# class EventInviteAdmin(admin.ModelAdmin):
#     list_filter = ['inviter', 'invitee']
#     list_display = ['inviter', 'invitee']
#     search_fields = ['inviter__username', 'inviter__email', 'invitee__username', 'invitee__email']
    
#     class Meta:
#         model = EventInvite

# admin.site.register(EventInvite)

admin.site.register(Venue)