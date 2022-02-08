from dataclasses import fields
from operator import concat
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'imgpath']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['latitude', 'longtitude', 'address']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['type', 'value']

class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    category = CategorySerializer()
    address = BranchSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id', 'name', 'logo', 'category', 'contacts', 'address']