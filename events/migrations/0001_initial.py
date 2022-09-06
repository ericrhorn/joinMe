# Generated by Django 4.1 on 2022-09-02 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(max_length=55)),
                ('city', models.CharField(max_length=55)),
                ('zip_code', models.CharField(max_length=15)),
                ('web_address', models.URLField(blank=True, verbose_name='web address')),
                ('venue_notes', models.TextField(blank=True, max_length=500)),
                ('private_venue', models.BooleanField(default=False)),
                ('public_venue', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=55)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('description', models.TextField(max_length=500)),
                ('event_notes', models.TextField(blank=True, max_length=500)),
                ('private_event', models.BooleanField(default=False)),
                ('public_event', models.BooleanField(default=False)),
                ('event_img', models.ImageField(blank=True, default=events.models.get_default_event_image, max_length=255, null=True, upload_to=events.models.get_event_image_filepath)),
                ('guests', models.ManyToManyField(blank=True, related_name='guests', to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', to=settings.AUTH_USER_MODEL)),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue')),
            ],
        ),
    ]