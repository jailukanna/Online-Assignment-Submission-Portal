from django.db import models


# Create your models here.

# Admin Login
class Admin(models.Model):
    Emailid = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)


class Student(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    Mobile = models.CharField(max_length=200)
    DOB = models.CharField(max_length=200)
    Course = models.CharField(max_length=200)
    Image = models.CharField(max_length=200)


class Teacher(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    Mobile = models.CharField(max_length=200)
    DOB = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Image = models.CharField(max_length=200)
