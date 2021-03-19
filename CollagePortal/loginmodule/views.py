from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth 
from django.template.context_processors import csrf
from django.contrib.auth.models import User



def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)




def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loginmodule/loggedin/')
    else:
        return HttpResponseRedirect('/loginmodule/invalidlogin/')

def signup(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    email = request.POST.get('email','') 
    if(request.POST.get('confirmpassword', '')!=password):
        return HttpResponseRedirect('/loginmodule/invalidlogin/')
    else:
        user = User.objects.create_user(username, email, password)

    


def loggedin(request):
    return HttpResponseRedirect('/database/home/')


def invalidlogin(request):
    return render(request, 'invalidlogin.html')


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')
# Create your views here.
