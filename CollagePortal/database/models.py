from django.db import models
from django.contrib import auth 
from django.contrib.auth.models import User 

from django.contrib.auth.models import Group,GroupManager , Permission

class Course(models.Model):
    Course_name = models.CharField(max_length=100)
   #Course_ID = models.CharField(max_length = 10 , primary_key=True )
    professor_name = models.CharField(max_length=100)
    department = models.CharField(max_length=20)


   # ID_NO = models.CharField(max_length=100, primary_key=True
class Classes(models.Model):
    name = models.CharField(max_length=100)
    Course = models.ForeignKey(Course,default="", on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
# Create your models here.

class Professor(models.Model):
    user = models.OneToOneField(User,default="", on_delete=models.CASCADE)
    department = models.CharField(max_length=100) 
    Course = models.ManyToManyField(Course,default="")
    

class Student(models.Model):
    user = models.OneToOneField(User,default="", on_delete=models.CASCADE)   
    Course = models.ManyToManyField(Course,default="")   

class Assignment(models.Model):
   # name= models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    submitted = models.BooleanField(default=False)
    Classes = models.ForeignKey(Classes,default="", on_delete=models.CASCADE)
    FILE = models.FileField(blank =True, null =True,upload_to="Assignments/")
    description = models.CharField(max_length=50,default="")
     

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment,default="", on_delete=models.CASCADE) 
    student = models.ForeignKey(Student,default="", on_delete=models.CASCADE) 
    date = models.DateTimeField()
    FILE = models.FileField(blank =True, null =True,upload_to="Submissions/")



    #email = models.CharField(max_length=100)
    #enrolled = models.ManyToManyField(Class)