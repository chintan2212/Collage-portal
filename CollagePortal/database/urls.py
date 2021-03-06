
from django.urls import path
from database.views import home, assignment ,openAssignment,addAssignment
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    url(r'^home/$', home),
    path('assignments/<class_name>',assignment),
    path('assignments/<class_name>/add', addAssignment),
    path('assignments/<class_name>/<lab_id>',openAssignment),
    path('assignments/<class_name>/<lab_id>/submit',openAssignment)
]
