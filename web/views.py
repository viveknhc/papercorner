from django.shortcuts import render
from multiprocessing import context

from .models import *

def index(request):
    return render(request,'web/index.html')

def base(request):
    return render(request,'web/partials/base.html')