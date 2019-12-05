from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

from .models import Destinations
# Create your views here.


def index(request):
    dests = Destinations.objects.all()
    return render(request, 'index.html', {'dests': dests})


def destination(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            name = request.GET["name"]
            print(name)
            return render(request, 'destination.html', {'name': name})
    else:
        messages.info(request, 'Please login first')
        return redirect('accounts/login')


