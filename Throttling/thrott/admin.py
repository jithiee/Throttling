from django.contrib import admin
from .models import Teachers

@admin.register(Teachers)
class TeacherAdmin(admin.ModelAdmin):
    list_display =  ['id','name','city','subj']

