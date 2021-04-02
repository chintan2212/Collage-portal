
from django.urls import path
from database.views import home, assignment ,openAssignment,addAssignment,removeAssignment,list_students,submit
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^home/$', home),
    path('assignments/<class_name>',assignment),
    path('assignments/<class_name>/add', addAssignment),
    path('assignments/<class_name>/<lab_id>',openAssignment),
    path('assignments/<class_name>/<lab_id>/submit',submit),
    path('assignments/<class_name>/<lab_id>/delete',removeAssignment),
    path('assignments/<class_name>/<lab_id>/list',list_students)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
