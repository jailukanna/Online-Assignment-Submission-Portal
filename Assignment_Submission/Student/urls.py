"""Student URL Configuration

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
from . import views
from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('Student_dashboard', views.Student_dashboard, name='Student_dashboard'),

    # Student update password
    path('StudentUpdate_Password', views.StudentUpdate_Password, name='Update_Password'),
    path('change_pass_student', views.change_pass_student, name='change_pass'),

    # User Profile Picture Data
    path('data_save', views.data_save, name='data_save'),
    path('Upload_image', views.Upload_image, name='Upload_image'),

    #  Subject List
    path('Subject_List', views.Subject_List, name='Subject_List'),

    # Assignment List-------------------------------
    path('Assignment_List', views.Assignment_List, name='Assignment_List'),

    # Assignment Download-----------------------
    path('download_myfile', views.download_myfile, name='download_myfile'),

    # Submit_Assignment---------------
    path('Submit_Assignment_P', views.Submit_Assignment_P, name='Submit_Assignment_P'),
    path('Submit_Assignment', views.Submit_Assignment, name='Submit_Assignment'),

    # my account-----------------
    path('my_account', views.my_account, name='my_account')

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
