from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from .models import Classes, Course, Student, Assignment
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
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
    return render(request, 'assignment_card.html',{'assignments': assignments})
# request.user.details.get().favourites.add(article)
def openAssignment(request,class_name,lab_id):
    assignment= Assignment.objects.get(id=lab_id)
    return render(request, 'assignment.html',{'assignment': assignment})

def submit(request,class_name,lab_id):
    temp_file = ContentFile()
    assignment= Assignment.objects.get(id = lab_id)
    submission = Assignment.submission_set.get(student = request.user.student)
    submission.FILE.save(f'{request.user+assignment.name}.pdf', temp_file)