from django.contrib import admin
from .models import ChoiceRate, Student, Course, Enrollment

admin.site.register(ChoiceRate)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
