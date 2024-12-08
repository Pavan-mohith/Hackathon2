
# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
from django.db import models

class OfficeHour(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]

    day_of_week = models.CharField(max_length=9, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day_of_week}: {self.start_time} - {self.end_time}"

# models.py
from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()

    def _str_(self):
        return self.title













