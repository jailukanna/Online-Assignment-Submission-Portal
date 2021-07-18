"""Teacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Teacher_Home', views.Teacher_Home, name='Teacher_Home'),

    # Teacher update password
    path('TeacherUpdate_Password', views.TeacherUpdate_Password, name='TeacherUpdate_Password'),
    path('change_pass_Teacher', views.change_pass_Teacher, name='change_pass_Teacher'),

    # Student Report
    path('StudentReport', views.StudentReport, name='Student_Report'),

    # User Profile Picture Data
    path('Teacher_image', views.Teacher_image, name='Teacher_image'),
    path('Teacher_Upload_img', views.Teacher_Upload_img, name='Teacher_Upload_img'),

    # Assignment_Add
    path('Assignment_Add_p', views.Assignment_Add_p, name='Assignment_Add_p'),
    path('Assignment_Add', views.Assignment_Add, name='Assignment_Add'),

    #  Subject_Add
    path('Subject_Add_P', views.Subject_Add_P, name='Subject_Add_P'),
    path('Subject_Add', views.Subject_Add, name='Subject_Add'),

    # Subject Report
    path('Subject_Report', views.Subject_Report, name='Subject_Report'),

    # Assignment Report
    path('Assignment_Report', views.Assignment_Report, name='Assignment_Report'),

    # Submitted Student Assignment
    path('View_Stu_Ass', views.View_Stu_Ass, name='View_Stu_Ass'),
    path('download_Assignment_S', views.download_Assignment_S, name='download_Assignment_S'),

    # my_acc------------
    path('my_account', views.my_acc, name='my_account'),

]
