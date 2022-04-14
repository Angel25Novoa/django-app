from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome Django course')

def date(request):
    return HttpResponse(f'La hora del servidor es {datetime.now()}')

def home(request):
    return render(request, 'home.html')