"""Admin URL Configuration

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
from django.conf import settings
from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('Admin_Home', views.Admin_Home, name='Admin_Home'),

    # Add User
    path('Add_User', views.Add_User, name='Add_User'),
    # Add Student---------------------------------------------
    path('Student_Signup', views.Student_Signup, name='Student_Signup'),
    # Add Teacher------------------------------------------
    path('Teacher_Signup', views.Teacher_Signup, name='Teacher_Signup'),
    # Add Admin-------------------------------------------
    path('Add_Admin', views.Add_Admin, name='Add_Admin'),

    # ------------------------------------------------------------------------------------------------------------------------------
    # Admin update password
    path('Update_Password', views.Update_Password, name='Update_Password'),
    path('change_pass', views.change_pass, name='change_pass'),

    # ------------------------------------------------------------------------------------------------------------------------------
    # Student Report
    path('Student_Report', views.Student_Report, name='Student_Report'),
    # Student record delete
    path('Student_delete_selected_row', views.Student_delete_selected_row, name='Student_delete_selected_row'),
    # Student record update Page
    path('Student_update', views.Student_update, name='Student_update'),
    # student record update
    path('Student_Record_update', views.Student_Record_update, name='Student_Record_update'),

    # ------------------------------------------------------------------------------------------------------------------------------
    # Teacher Report
    path('Teacher_Report', views.Teacher_Report, name='Teacher_Report'),
    # Teacher record delete
    path('Teacher_delete_selected_row', views.Teacher_delete_selected_row, name='Teacher_delete_selected_row'),
    # Teacher record update Page
    path('Teacher_update', views.Teacher_update, name='Teacher_update'),
    # Teacher record update
    path('Teacher_Record_update', views.Teacher_Record_update, name='Teacher_Record_update'),

    # -----------------------------------------------------------------------------------------------------------

    # Admin Report
    path('Admin_Report', views.Admin_Report, name='Admin_Report'),
    # Admin record delete
    # path('Admin_delete_selected_row', views.Admin_delete_selected_row, name='Admin_delete_selected_row'),

    #  Add Subject
    path('Add_Subject_P', views.Add_Subject_P, name='Add_Subject_P'),
    path('Add_Subject', views.Add_Subject, name='Add_Subject'),

    # Add Assignment
    path('Add_assignment_p', views.Add_assignment_p, name='Add_assignment_p'),
    path('Add_Assignment', views.Add_Assignment, name='Add_Assignment'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
