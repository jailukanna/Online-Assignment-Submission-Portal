from django.db import models

# Create your models here.

class Subject(models.Model):
    Subject_Name = models.CharField(max_length=200)
    Subject_Description = models.CharField(max_length=200)

class Assignment(models.Model):
    Subject_Name = models.CharField(max_length=200)
    Assignment_Title = models.CharField(max_length=200)
    Assignment_Description = models.CharField(max_length=200)
    File_Name = models.CharField(max_length=200)
    Assignment_File = models.CharField(max_length=200)
    Due_Date = models.CharField(max_length=200)