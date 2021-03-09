from django.db import models


class Course(models.Model):
    Course_name = models.CharField(max_length=100)
   # Course_ID = models.CharField(max_length = 10 , primary_key=True )
    professor_name = models.CharField(max_length=100)
    department = models.CharField(max_length=20)   



   # ID_NO = models.CharField(max_length=100, primary_key=True)
    
    
class Class(models.Model):
    name = models.CharField(max_length=100)
    Professor_name = models.CharField(max_length=100)
    description = models.CharField(max_length=50, default="", editable=True)
# Create your models here.

class Assignment(models.Model):
   # name= models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    #ofClass = models.ForeignKey(Class, on_delete=models.CASCADE)
    submitted = models.BooleanField()

class User(models.Model):
    Name = models.CharField(max_length=100)
    #ID = models.CharField(max_length=100)
   # Prof = models.BooleanField()
    #email = models.CharField(max_length=100)
    #enrolled = models.ManyToManyField(Class)