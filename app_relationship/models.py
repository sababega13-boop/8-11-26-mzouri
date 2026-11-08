from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Course(models.Model):
    name = models.CharField(max_length=100)

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=100)

    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name



class StudentProfile(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE
    )

    age = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.student.name