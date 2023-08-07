
from django.contrib import admin

from .models import Course, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_date']
    list_filter = ['name', 'birth_date']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
