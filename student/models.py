
from django.db import models


class Student(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    DOB = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)
    address = models.TextField()
    branch = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    java = models.CharField(max_length=50)
    python = models.CharField(max_length=50)
    sql = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='', blank=True)

    def __str__(self) -> str:
        return (self.first_name + self.last_name)
