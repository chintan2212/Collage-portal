from django.urls import path
from database.views import home
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    url(r'^home/$', home)
    
]
