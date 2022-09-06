from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import os
import cv2
import json
import base64
# import requests
from django.core import files

# from friend.utils import get_friend_request_or_false
# from friend.friend_request_status import FriendRequestStatus

from users.forms import AccountAuthenticationForm, RegistrationForm, AccountUpdateForm
from users.models import Account
from events.models import Event, Venue
from django.conf import settings

# from friend.models import FriendList, FriendRequest

TEMP_PROFILE_IMAGE_NAME = "temp_profile_image.png"


# Create your views here.

def register_view(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.email))

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request, *args, **kwargs):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect('home')
                
        else: 
            context['login_form'] = form
    return render(request, 'login.html', context)

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect 

def dashboard_view(request, *args, **kwargs):
    # context = {}
    event_list = Event.objects.all()
    # attending = Event.objects.get('join_event')
    # context['attending'] = attending
    return render(request, "users/dashboard.html", {'event_list' : event_list})
    # return render(request, "users/dashboard.html")