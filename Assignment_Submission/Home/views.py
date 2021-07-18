from .models import *
from django.shortcuts import render, redirect


# Create your views here.

def home_page(request):
    return render(request, 'Home.html')

def About_Page(request):
    return render(request, 'About.html')

def Contact_Page(request):
    return render(request, 'Contact Us.html')


# ------------------Admin-------------
def Admin_Login(request):
    if request.POST:
        Email = request.POST['em']
        request.session['admin_email'] = Email
        Password = request.POST['pw']
        request.session['mypass'] = Password
        admin_obj = Admin.objects.filter(Emailid=Email, Password=Password)
        data_len = len(admin_obj)
        if data_len == 1:
            return redirect('Admin_')
        else:
            return render(request, 'Home.html', {'msg': 'Invalid Login Details'})
    else:
        return render(request, 'Home.html')


def Admin_(request):
    if request.session.has_key('admin_email'):
        a = request.session['admin_email']
        return render(request, 'Admin_Home.html', {'msg': a})
    else:
        return render(request, 'Home.html')


# -----------Admin Logout-----------------

def Admin_Logout(request):
    if request.session.has_key('admin_email'):
        del request.session['admin_email']
        return render(request, 'Home.html')
    else:
        return render(request, 'Home.html')


# -----------STUDENT--------------

def Save_signup(request):
    Name = request.POST['nm']
    Email = request.POST['email']
    Password = request.POST['password']
    Gender = request.POST['gen']
    Mobile = request.POST['mob']
    DOB = request.POST['dob']
    Course = request.POST['co']
    signup_obj = Student(Name=Name, Email=Email, Password=Password, Gender=Gender, Mobile=Mobile, DOB=DOB,
                         Course=Course)
    signup_obj.save()
    return render(request, 'Home.html', {"msgs": "Signup Successfully"})


# ------Student_Login-----------
def Student_Login(request):
    if request.POST:
        Email = request.POST['em']
        request.session['Student_email'] = Email
        Password = request.POST['pw']
        request.session['mypassword'] = Password
        signup_obj = Student.objects.filter(Email=Email, Password=Password)
        data_len = len(signup_obj)
        if data_len == 1:
            return redirect('Student_')
        else:
            return render(request, 'Home.html', {'msgg': 'Invalid Login Details'})

    else:
        return render(request, 'Home.html')


def Student_(request):
    if request.session.has_key('Student_email'):
        s = request.session['Student_email']
        S_obj = Student.objects.filter(Email=s)
        return render(request, 'Student_Dashboard.html', {'msgS': S_obj, 'Semail': s})
    else:
        return render(request, 'Home.html')


# ---------------Student Logout------------------
def Student_Logout(request):
    if request.session.has_key('Student_email'):
        del request.session['Student_email']
        return render(request, 'Home.html')
    else:
        return render(request, 'Home.html')


# ----------------------Teacher Signup--------------------

def Teacher_signup(request):
    Name = request.POST['nm']
    Email = request.POST['email']
    Password = request.POST['password']
    Gender = request.POST['gen']
    Mobile = request.POST['mob']
    DOB = request.POST['dob']
    Subject = request.POST['su']
    signup_obj = Teacher(Name=Name, Email=Email, Password=Password, Gender=Gender, Mobile=Mobile, DOB=DOB,
                         Subject=Subject)
    signup_obj.save()
    return render(request, 'Home.html', {"Tmsg": "Signup Successfully"})


# ------Teacher_Login-----------
def Teacher_Login(request):
    if request.POST:
        Email = request.POST['mail']
        request.session['Teacher_email'] = Email
        Password = request.POST['pwd']
        request.session['mypassword'] = Password
        signup_obj1 = Teacher.objects.filter(Email=Email, Password=Password)
        data_len = len(signup_obj1)
        if data_len == 1:
            return redirect('Teacher_')
        else:
            return render(request, 'Home.html', {'Mmsg': 'Invalid Login Details'})

    else:
        return render(request, 'Home.html')


def Teacher_(request):
    if request.session.has_key('Teacher_email'):
        t = request.session['Teacher_email']
        T_obj = Teacher.objects.filter(Email=t)
        return render(request, 'Teacher_Dashboard.html', {'msgT': T_obj, 'temail': t})
    else:
        return render(request, 'Home.html')


# ---------Teacher Logout------------

def Teacher_Logout(request):
    if request.session.has_key('Teacher_email'):
        del request.session['Teacher_email']
        return render(request, 'Home.html')
    else:
        return render(request, 'Home.html')

