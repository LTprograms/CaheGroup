from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    ctx = {
        'cursos' : Curso.objects.all()
    }
    return render(request, "CaheUp/index.html", ctx)