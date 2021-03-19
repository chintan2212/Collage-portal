from loginmodule.views import assignment
from django.urls import path
from database.views import home, assignment
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    url(r'^home/$', home),
    url(r'^assignment/$', assignment)
]
