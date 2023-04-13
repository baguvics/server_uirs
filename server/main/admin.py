from django.contrib import admin
from .models import Student, Teacher, Department, Group, Themes


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Group)
admin.site.register(Themes)
