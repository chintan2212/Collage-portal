from django.db import models


class Course(models.Model):
    Course_name = models.CharField(max_length=100)
   # Course_ID = models.CharField(max_length = 10 , primary_key=True )
    professor_name = models.CharField(max_length=100)
    department = models.CharField(max_length=20)   

class Assignment(models.Model):
   # name= models.CharField(max_length=100)
    professor_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
   # description = models.CharField(max_length = 200)
    submitted = models.BooleanField()
class User(models.Model):
    Name = models.CharField(max_length=100)
   # ID_NO = models.CharField(max_length=100, primary_key=True)
    
    
class Class(models.Model):
    Courses = models.CharField(max_length=100)
    Professor = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
# Create your models here.


