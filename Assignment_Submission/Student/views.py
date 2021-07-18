from django.shortcuts import render, redirect
from Home.models import Student
from .models import Student_Assignment
from Admin.models import Subject, Assignment
import mimetypes
import os
from wsgiref.util import FileWrapper
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


# Create your views here.


def Student_dashboard(request):
    if request.session.has_key('Student_email'):
        ems = request.session['Student_email']
        return render(request, 'Student_Dashboard.html')
    else:
        return render(request, 'Home.html')


# -------Student UPDATE PASSWORD------------

def StudentUpdate_Password(request):
    if request.session.has_key('Student_email'):
        ems = request.session['Student_email']
        return render(request, 'StudentUpdatePassword.html', {'msg1': ems})
    else:
        return render(request, 'Home.html')


def change_pass_student(request):
    if request.session.has_key('Student_email'):
        Current_user = request.session['Student_email']
        Old_Password = request.POST['Old_p']
        New_Password = request.POST['New_p']
        Confirm_Password = request.POST['Confirm_p']
        signup_objk = Student.objects.filter(Email=Current_user, Password=Old_Password)
        data_len = len(signup_objk)
        if data_len == 1:
            if New_Password == Confirm_Password:
                for my in signup_objk:
                    Login_id = my.id
                    signup_obj1 = Student.objects.get(id=Login_id)
                    signup_obj1.Password = New_Password
                    signup_obj1.save()
                    return render(request, 'Home.html', {'set_msg1': 'Password Changed Successfully'})
            else:
                return render(request, 'StudentUpdatePassword.html',
                              {'msg11': 'New and Confirm Password does not match !'})
        else:
            return render(request, 'StudentUpdatePassword.html', {'msg22': 'Old Password Incorrect'})
    else:
        return render(request, 'Home.html')


# User Profile picture Data

def data_save(request):
    if request.session.has_key('Student_email'):
        ems = request.session['Student_email']
        Student_data = Student.objects.filter(Email=ems)
        return render(request, 'Studentpicture.html', {'Student_data': Student_data})
    else:
        return render(request, 'Home.html')


def Upload_image(request):
    if request.session.has_key('Student_email'):
        ems = request.session['Student_email']
        if request.method == 'POST' and request.FILES['img_stu']:
            Name = request.POST['nm']
            filedata = request.FILES['img_stu']
            st = FileSystemStorage()
            filename = st.save(filedata.name, filedata)
            my_file_uploaded_url = st.url(filename)

            data_obj = Student.objects.get(Name=Name)
            data_obj.Image = my_file_uploaded_url
            data_obj.save()
            return render(request, 'Studentpicture.html', {'pic': data_obj})
    else:
        return render(request, 'Home.html')


# ---------------------------------------------------------------------------

def Subject_List(request):
    if request.session.has_key('Student_email'):
        data_obj = request.session['Student_email']
        data_obj = Subject.objects.all()
        return render(request, 'Subject_List.html', {'data': data_obj})
    else:
        return render(request, 'Home.html')


# Assignment list---------------------

def Assignment_List(request):
    if request.session.has_key('Student_email'):
        a = request.session['Student_email']
        data_obj = Assignment.objects.all()
        return render(request, 'Assignment_list.html', {'data': data_obj})
    else:
        return render(request, 'Home.html')


# --------------------Assignment Download---------------------

def download_myfile(request):
    user_id = request.GET['ids']
    obj = Assignment.objects.get(id=user_id)
    file_name = obj.File_Name
    file_path = settings.MEDIA_ROOT + '/' + file_name
    file_wrapper = FileWrapper(open(file_path, 'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype)
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % str(file_name)
    return response


# Submit Assignment---------------------

def Submit_Assignment_P(request):
    if request.session.has_key('Student_email'):
        a = request.session['Student_email']
        return render(request, 'Submit_Assignment.html', {'data': a})
    else:
        return render(request, 'Home.html')

def Submit_Assignment(request):
    if request.session.has_key('Student_email'):
        ems = request.session['Student_email']
        if request.method == 'POST' and request.FILES['ass_stu']:
            Subject_Name = request.POST['SN']
            Assignment_Title = request.POST['AT']
            Assignment_Description = request.POST['AD']
            Submission_Date = request.POST['SD']

            filedata = request.FILES['ass_stu']
            st = FileSystemStorage()
            filename = st.save(filedata.name, filedata)
            my_file_uploaded_url = st.url(filename)

            data_obj = Student_Assignment(Subject_Name=Subject_Name, Assignment_Title=Assignment_Title,
                                  Assignment_Description=Assignment_Description, Submission_Date=Submission_Date,
                                  Assignment_File=my_file_uploaded_url, File_Name=filename)
            data_obj.save()
            return render(request, 'Submit_Assignment.html', {'ass': data_obj})
    else:
        return render(request, 'Home.html')


def my_account(request):
    if request.session.has_key('Student_email'):
        ems = request.session['Student_email']
        Student_data = Student.objects.filter(Email=ems)
        return render(request, 'My_account.html', {'Student_data': Student_data})
    else:
        return render(request, 'Home.html')