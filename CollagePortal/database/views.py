from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from .models import Class
# Create your views here.
def home(request):
    classes = Class.objects.all()
    return render(request,"index.html", {'classes': classes})

