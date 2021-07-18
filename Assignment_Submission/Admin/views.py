from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from Home.models import Teacher, Student, Admin
from Home.views import *
from .models import Subject, Assignment


def Admin_Home(request):
    if request.session.has_key('admin_email'):
        a = request.session['admin_email']
        return render(request, 'Admin_Home.html', {'msg': a})
    else:
        return render(request, 'Home.html')


def Add_User(request):
    if request.session.has_key('admin_email'):
        a = request.session['admin_email']
        return render(request, 'Add_User.html', {'msg': a})
    else:
        return render(request, 'Home.html')


# ----------------------Add Student --------------------
def Student_Signup(request):
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
    return render(request, 'Add_User.html', {"msgs": "Signup Successfully"})


# ----------------------Add Teacher--------------------

def Teacher_Signup(request):
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
    return render(request, 'Add_User.html', {"Tmsg": "Signup Successfully"})


# ----------------Add Admin--
def Add_Admin(request):
    Emailid = request.POST['Aem']
    Password = request.POST['Apw']
    Add_obj = Admin(Emailid=Emailid, Password=Password)
    Add_obj.save()
    return render(request, 'Add_User.html', {"Amsg": "Signup Successfully"})


# -------Admin UPDATE PASSWORD------------

def Update_Password(request):
    if request.session.has_key('admin_email'):
        ems = request.session['admin_email']
        return render(request, 'UpdatePassword.html', {'msg1': ems})
    else:
        return render(request, 'Home.html')


def change_pass(request):
    if request.session.has_key('admin_email'):
        Current_user = request.session['admin_email']
        Old_Password = request.POST['Old_p']
        New_Password = request.POST['New_p']
        Confirm_Password = request.POST['Confirm_p']
        signup_objj = Admin.objects.filter(Emailid=Current_user, Password=Old_Password)
        data_len = len(signup_objj)
        if data_len == 1:
            if New_Password == Confirm_Password:
                for my in signup_objj:
                    Login_id = my.id
                    signup_obj1 = Admin.objects.get(id=Login_id)
                    signup_obj1.Password = New_Password
                    signup_obj1.save()
                    return render(request, 'Home.html', {'set_msg1': 'Password Changed Successfully'})
            else:
                return render(request, 'UpdatePassword.html', {'msg11': 'New and Confirm Password does not match !'})
        else:
            return render(request, 'UpdatePassword.html', {'msg22': 'Old Password Incorrect'})
    else:
        return render(request, 'Home.html')


# ---------------------------------------------------------------------------------------------------------------------------

# Student Report ------code--------------------------

def Student_Report(request):
    if request.session.has_key('admin_email'):
        data_obj = request.session['admin_email']
        data_obj = Student.objects.all()
        return render(request, 'Studentreport.html', {'data': data_obj})
    else:
        return render(request, 'Home.html')


# Record Delete
def Student_delete_selected_row(request):
    if request.session.has_key('admin_email'):
        signup_obj = request.session['admin_email']
        reg_id = request.GET['id']
        signup_obj = Student(id=reg_id)
        signup_obj.delete()
        signup_obj = Student.objects.all()
        return render(request, 'Studentreport.html', {'data': signup_obj})
    else:
        return render(request, 'Home.html')


# Update page
def Student_update(request):
    if request.session.has_key('admin_email'):
        signup_obj = request.session['admin_email']
        Login_id = request.GET['id']
        signup_obj = Student.objects.all().filter(id=Login_id)
        return render(request, 'Studentupdate.html', {'data': signup_obj})
    else:
        return render(request, 'Home.html')


# student record update
def Student_Record_update(request):
    if request.session.has_key('admin_email'):
        a = request.session['admin_email']

        reg_id = request.POST['id']
        Name = request.POST['nm']
        Email = request.POST['email']
        Gender = request.POST['gen']

        signup_obj1 = Student.objects.get(id=reg_id)
        signup_obj1.Name = Name
        signup_obj1.Gender = Gender
        signup_obj1.save()
        signup_obj1 = Student.objects.all()
        return render(request, 'Studentupdate.html', {'data': signup_obj1})
    else:
        return render(request, 'Home.html')


# ---------------------------------------------------------------------------


# Teacher Report ------code--------------------------

def Teacher_Report(request):
    if request.session.has_key('admin_email'):
        data_obj = request.session['admin_email']
        data_obj = Teacher.objects.all()
        return render(request, 'TeacherReport.html', {'data': data_obj})
    else:
        return render(request, 'Home.html')


#  Teacher Record Delete
def Teacher_delete_selected_row(request):
    if request.session.has_key('admin_email'):
        signup_obj = request.session['admin_email']
        reg_id = request.GET['id']
        signup_obj = Student(id=reg_id)
        signup_obj.delete()
        signup_obj = Teacher.objects.all()
        return render(request, 'TeacherReport.html', {'data': signup_obj})
    else:
        return render(request, 'Home.html')


# Teacher Update page
def Teacher_update(request):
    if request.session.has_key('admin_email'):
        signup_obj = request.session['admin_email']
        Login_id = request.GET['id']
        signup_obj = Teacher.objects.all().filter(id=Login_id)
        return render(request, 'Teacherupdate.html', {'data': signup_obj})
    else:
        return render(request, 'Home.html')


# Teacher record update
def Teacher_Record_update(request):
    if request.session.has_key('admin_email'):
        a = request.session['admin_email']

        reg_id = request.POST['id']
        Name = request.POST['nm']
        Email = request.POST['email']
        Gender = request.POST['gen']

        signup_obj1 = Teacher.objects.get(id=reg_id)
        signup_obj1.Name = Name
        signup_obj1.Gender = Gender
        signup_obj1.save()
        signup_obj1 = Teacher.objects.all()
        return render(request, 'Teacherreport.html', {'data': signup_obj1})
    else:
        return render(request, 'Home.html')


# -------------------------------------------------------------------------------------------------------

# Admin Report ------code--------------------------

def Admin_Report(request):
    if request.session.has_key('admin_email'):
        data_obj = request.session['admin_email']
        data_obj = Admin.objects.all()
        return render(request, 'AdminReport.html', {'data': data_obj})
    else:
        return render(request, 'Home.html')


#  Admin Record Delete
# def Admin_delete_selected_row(request):
#     if request.session.has_key('admin_email'):
#         signup_obj = request.session['admin_email']
#         reg_id = request.GET['id']
#         signup_obj = Admin(id=reg_id)
#         signup_obj.delete()
#         signup_obj = Admin.objects.all()
#         return render(request, 'Adminreport.html', {'data': signup_obj})
#     else:
#         return render(request, 'Home.html')


# Admin Update page
# def Teacher_update(request):
#     if request.session.has_key('admin_email'):
#         signup_obj = request.session['admin_email']
#         Login_id = request.GET['id']
#         signup_obj = Admin.objects.all().filter(id=Login_id)
#         return render(request, 'AdminUpdate.html', {'data': signup_obj})
#     else:
#         return render(request, 'Home.html')



# Add Subject--------------------
def Add_Subject_P(request):
    if request.session.has_key('admin_email'):
        subject = request.session['admin_email']
        return render(request, 'Add_Subject.html', {'data': subject})
    else:
        return render(request, 'Home.html')


def Add_Subject(request):
    Subject_Name = request.POST['sn']
    Subject_Description = request.POST['sd']
    signup_obj = Subject(Subject_Name=Subject_Name, Subject_Description=Subject_Description)
    signup_obj.save()
    return render(request, 'Add_Subject.html', {"msgs": "Subject Added Successfully"})


# Add Assignment-----------------------------------------

def Add_assignment_p(request):
    if request.session.has_key('admin_email'):
        subject = request.session['admin_email']
        return render(request, 'Add_Assignment.html', {'data': subject})
    else:
        return render(request, 'Home.html')


def Add_Assignment(request):
    if request.session.has_key('admin_email'):
        ems = request.session['admin_email']
        if request.method == 'POST' and request.FILES['ass_stu']:
            Subject_Name = request.POST['SN']
            Assignment_Title = request.POST['AT']
            Assignment_Description = request.POST['AD']
            Due_Date = request.POST['DD']

            filedata = request.FILES['ass_stu']
            st = FileSystemStorage()
            filename = st.save(filedata.name, filedata)
            my_file_uploaded_url = st.url(filename)

            data_obj = Assignment(Subject_Name=Subject_Name, Assignment_Title=Assignment_Title,
                                  Assignment_Description=Assignment_Description, Due_Date=Due_Date,
                                  Assignment_File=my_file_uploaded_url, File_Name=filename)
            data_obj.save()
            return render(request, 'Add_Assignment.html', {'ass': data_obj})
    else:
        return render(request, 'Home.html')
