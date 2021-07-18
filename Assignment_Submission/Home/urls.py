"""Home URL Configuration

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
    path('', views.home_page, name='home'),
    path('About', views.About_Page, name='About'),
    path('Contact Us', views.Contact_Page, name='Contact Us'),

    # Admin------------
    path('Admin_Login', views.Admin_Login, name='Admin_Login'),
    path('Admin_', views.Admin_, name='Admin_'),
    path('Admin_Logout', views.Admin_Logout, name='Admin_Logout'),

    # Student--------
    path('Student_Signup', views.Save_signup, name='Student_Signup'),
    path('Student_Login', views.Student_Login, name='Student_Login'),
    path('Student_', views.Student_, name='Student_'),
    path('Student_Logout', views.Student_Logout, name='Student_Logout'),

    # Teacher-------
    path('Teacher_Signup', views.Teacher_signup, name='Teacher_Signup'),
    path('Teacher_Login', views.Teacher_Login, name='Teacher_Login'),
    path('Teacher_', views.Teacher_, name='Teacher_'),
    path('Teacher_Logout', views.Teacher_Logout, name='Teacher_Logout'),


]
