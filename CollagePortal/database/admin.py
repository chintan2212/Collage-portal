from django.contrib import admin
from .models import Assignment, Class,Course

# Register your models here.
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(Class)