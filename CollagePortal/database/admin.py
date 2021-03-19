from django.contrib import admin
from .models import Assignment, Classes,Course,Student,Submission

# Register your models here.
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(Classes)
admin.site.register(Student)
admin.site.register(Submission)
