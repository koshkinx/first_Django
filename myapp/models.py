from django.db import models

# Create your models here.


class ChoiceRate(models.Model):
    choice_rate = models.IntegerField(default=1)


class Student(models.Model):
    name = models.CharField(max_length=70)


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student)


class Enrollment(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    enroll_date = models.DateField(auto_now=True)
