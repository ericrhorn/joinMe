from django.conf import settings
from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=55)
    address = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    zip_code = models.CharField(max_length=15)
    web_address = models.URLField('web address', blank=True)
    venue_notes = models.TextField(max_length=500, blank=True)

    private_venue = models.BooleanField(default=False)
    public_venue = models.BooleanField(default=False)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


def get_event_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_event_image():
    return "default_img/profile-picture.png"


class Event(models.Model):
    event_name = models.CharField(max_length=55)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    start_date = models.DateField()
    end_date = models.DateField()

    start_time = models.TimeField()
    end_time = models.TimeField()

    description = models.TextField(max_length=500)
    
    event_notes = models.TextField(max_length=500, blank=True)

    private_event = models.BooleanField(default=False)

    public_event = models.BooleanField(default=False)

    event_img = models.ImageField(max_length=255, upload_to=get_event_image_filepath, null=True, blank=True, default=get_default_event_image)


    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='event_planned', on_delete=models.CASCADE)

    venue = models.ForeignKey(Venue, blank=True, on_delete=models.CASCADE, null=True) #call events.venue or events.venue.name for name

        
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='host')
    guests = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='guests')

    join_event = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="attend_event", blank=True)

    # def total_attending(self):
    #     return self.join_event.count()

    def __str__(self):
        return self.event_name

    # change image filename to filename i set 
    def get_event_image_filename(self):
        return str(self.profile_img)[str(self.profile_img).index(f'profile_images/{self.pk}/'):]
