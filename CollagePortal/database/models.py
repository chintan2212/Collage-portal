from django.db import models
from django.contrib import auth 
from django.contrib.auth.models import User 

from django.contrib.auth.models import Group,GroupManager , Permission

class Course(models.Model):
    Course_name = models.CharField(max_length=100)
    department = models.CharField(max_length=20)
    def getClasses(self):
        return self.classes_set.all()
    def getStudents(self):
        return self.student_set.all()

class Professor(models.Model):
    user = models.OneToOneField(User,default="", on_delete=models.CASCADE)
    def getClasses(self):
        return self.classes_set.all()
class Classes(models.Model):
    professor = models.ForeignKey(Professor,default="", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Course = models.ForeignKey(Course,default="", on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    def getAssignments(self):
        return self.assignment_set.all()

class Student(models.Model):
    user = models.OneToOneField(User,default="", on_delete=models.CASCADE)   
    Course = models.ManyToManyField(Course,default="")
    def getCourses(self):
        return self.Course.all()   
    def getClasses(self):
        course = self.getCourses()
        classes = []
        for cors in course:
            cl = cors.getClasses()
            classes.extend(cl)
        return classes
class Assignment(models.Model):# name= models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    Classes = models.ForeignKey(Classes,default="", on_delete=models.CASCADE)
    FILE = models.FileField(blank =True, null =True,upload_to="Assignments/")
    description = models.CharField(max_length=50,default="")
    @classmethod
    def add(cls,_name,_class,desc = 'NO Description',FILE = None):
        assignment=Assignment.objects.create(name=_name ,Classes= _class, description= desc,FILE= FILE)
        students_subscribed = _class.Course.getStudents()
        for student in students_subscribed:
            '''
            creates a submission link for all students and assignment
            '''
            submission=Submission.objects.create(assignment = assignment,student = student)
        return 
    
    
    def getNotSubmitted(self):
        submissions = self.submission_set.all()
        not_submitted=[]
        for submission in submissions:
            if(submission.submitted==False):
                not_submitted.append(submission.student)
        return not_submitted

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment,default="", on_delete=models.CASCADE) 
    student = models.ForeignKey(Student,default="", on_delete=models.CASCADE) 
    submitted = models.BooleanField(default=False)
    date = models.DateTimeField(null=True)
    FILE = models.FileField(blank =True, null =True,upload_to="Submissions/")
    remarks = models.TextField(max_length=255,default="None")
