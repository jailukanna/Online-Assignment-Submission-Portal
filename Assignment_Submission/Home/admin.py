from django.contrib import admin

# Register your models here.
from .models import Admin, Student, Teacher

admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Teacher)
