# Generated by Django 4.1 on 2022-09-02 21:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='join_event',
            field=models.ManyToManyField(related_name='attend_event', to=settings.AUTH_USER_MODEL),
        ),
    ]