from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from database.models import Course, Student


def login(request):
    courses = Course.objects.all()
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', {'c': c, 'courses': courses})

    # messages.warning(request,"Invalid Username or Password")


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loginmodule/loggedin/')
    else:
        return HttpResponseRedirect('/loginmodule/invalidlogin/')


def signup(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password1', '')
    email = request.POST.get('email', '')
    user = User.objects.create_user(username, email, password)
    student = Student.objects.create(user=user)
    courses: Course
    for c in Course.objects.all():
        if(request.POST.get(c.Course_name), False):
            student.Course.add(c)
    return HttpResponseRedirect('/loginmodule/login/')


def loggedin(request):
    return HttpResponseRedirect('/database/home/')


def invalidlogin(request):
    return render(request, 'invalidlogin.html')


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')


def assignment(request):
    return render(request, 'assignment.html')
# Create your views here.
