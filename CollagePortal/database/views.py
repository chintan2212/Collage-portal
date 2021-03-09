from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from .models import Classes
# Create your views here.
def home(request):
   user = User.objects.get()
   classes=[]
   if(user.student):
       course=user.student.Course.all()
       for cors in course:
           cl= cors.classes_set.all()
           for c in cl:
               classes.append(c)
   return render(request,"index.html", {'classes': classes})


#request.user.details.get().favourites.add(article)