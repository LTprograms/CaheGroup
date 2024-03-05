from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    form = ContactForm()
    return render(request, 'Refrimotors/index.html', {"form" : form})