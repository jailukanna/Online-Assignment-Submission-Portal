from django.contrib import admin


# Register your models here.
from .models import Subject, Assignment

admin.site.register(Subject)
admin.site.register(Assignment)
