from django.shortcuts import render

from .models import *

def hello(request):
    return render(request, '')