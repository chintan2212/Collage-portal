from django.db import models


class Course(models.Model):
    Course_name = models.CharField(max_length=100)
    professor_name = models.CharField(max_length=100)
    department = models.CharField(max_length=20)


class Assignment(models.Model):
    professor_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    submitted = models.BooleanField()


class Class(models.Model):
    Courses = models.CharField(max_length=100)
    Professor = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
# Create your models here.
