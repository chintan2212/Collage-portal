from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from .models import Classes , Course ,Student
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.





        



@login_required
def home(request):
   user = request.user
   classes=[]
   course=user.student.Course.all()
   for cors in course:
       cl= cors.classes_set.all()
       for c in cl:
           classes.append(c)
    
   return render(request,"index.html", {'classes': classes})

def classOpen(request,cl:Classes):
    assignments=[]
    assign=cl.assignment.all()
    for c in assign:
        assignments.append(c)
    return assignments



#request.user.details.get().favourites.add(article)