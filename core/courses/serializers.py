from dataclasses import fields
from operator import concat
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
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
    id = serializers.IntegerField(required=False)
    # contacts = ContactSerializer(many=True, required=False)
    category = CategorySerializer(read_only=True)
    # address = BranchSerializer(many=True, required=False)
    class Meta:
        model = Course
        fields = ['id', 'name', 'logo', 'category']

    def create(self, validated_data):
        categories = validated_data.pop('category')
        new = Course.objects.create(**validated_data)
        # for category in categories:
        #     Category.objects.create(**category)
        return new
