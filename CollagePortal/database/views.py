
import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse , Http404
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from .models import Classes, Course, Student, Assignment , Submission
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
# Create your views here.



def home(request):
    user = request.user
    classes = []
    try:
        profile=user.professor
    except ObjectDoesNotExist:
        try :
            profile= user.student
        except ObjectDoesNotExist:
            return HttpResponseRedirect("/loginmodule/invalidlogin")
    classes = profile.getClasses()
    return render(request, "index.html", {'classes': classes})


def assignment(request,class_name):
    assignments = []
    _class = Classes.objects.get(name=class_name)     
    assign = _class.assignment_set.all()
    for c in assign:
        assignments.append(c)
    #return HttpResponse("<h1>{}.</h1>".format(assignments[1].name))
    return render(request, 'assignment_card.html',{'assignments': assignments,'classes':_class})
# request.user.details.get().favourites.add(article)

def openAssignment(request,class_name,lab_id):
    assignment= Assignment.objects.get(id=lab_id)
    return render(request, 'assignment.html',{'assignment': assignment})

def submit(request,class_name,lab_id):
    try:
        student = request.user.student
        assignment= Assignment.objects.get(id = lab_id)
    except ObjectDoesNotExist:
        return Http404("youre not a student")
    FILE = request.FILES['myfile']
    if (FILE  != None):
        submitted = True
        Submission.add(assignment,student ,submitted,FILE)
    return HttpResponseRedirect('/database/assignments/'+class_name+'/'+lab_id)

def addAssignment(request,class_name):
    try :
       pass
    #request.user.professor
    except ObjectDoesNotExist:
        return Http404("you are not a proffessor")
    _name=request.POST['assignment_name'] #input name
    _class = Classes.objects.get(name=class_name)
    desc=request.POST['assignment_disc'] 
    FILE =request.FILES['file']
    Assignment.add(_name,_class,desc,FILE)
    return HttpResponseRedirect('/database/assignments/'+class_name)
    
def removeAssignment(request,class_name,lab_id):
    try :
        request.user.professor
    except ObjectDoesNotExist:
        return Http404("you are not a proffessor")
    assignment= Assignment.objects.get(id = lab_id).delete()
    return HttpResponseRedirect('/database/assignments/'+class_name)
# imcomplete


def list_students(request,class_name,lab_id): # left to be implemented
    assignment= Assignment.objects.get(id = lab_id)
    not_submitted = assignment.getNotSubmitted()
    submitted = assignment.getSubmitted()
    return render(request, 'table_submission.html',{'submitted': submitted,'not_submitted': not_submitted})
