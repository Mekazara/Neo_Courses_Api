from statistics import mode
from django.db import models
from django.forms import ModelChoiceField

class Category(models.Model):
    name = models.CharField(max_length=50, default='Not choosen')
    imgpath = models.CharField(max_length=20, default='imgpath')

    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    logo = models.CharField(max_length=30, default='LOGO')

    def __str__(self) -> str:
        return self.name

class Branch(models.Model):
    latitude = models.CharField(max_length=50)
    longtitude = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True,
                                related_name='address')

    def __str__(self) -> str:
        return self.address

class Contact(models.Model):
    types = (
        ('Phone', 'Phone'),
        ('Facebook', 'Facebook'),
        ('E-mail', 'E-mail')
        )
    type = models.CharField(max_length=30, choices=types)
    value = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, 
                                null=True, related_name='contacts')

    def __str__(self) -> str:
        return self.type



