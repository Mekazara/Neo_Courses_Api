import imp
from django.contrib import admin
from .models import Category, Course, Branch, Contact

# Register your models here.
admin.site.register([Category, Course, Branch, Contact])
