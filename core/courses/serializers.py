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
        fields = ['id', 'latitude', 'longtitude', 'address']

class ContactSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display", read_only=True)
    class Meta:
        model = Contact
        fields = ['id', 'type', 'value']


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    category = CategorySerializer()
    # category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    contacts = ContactSerializer(many=True)
    # address = BranchSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id', 'category', 'name', 'contacts']
        depth = 1

    def create(self, validated_data):
        contacts = validated_data.pop('contacts')
        # adrs = validated_data.pop('address')
        cat = validated_data.pop('category')
        category, created = Category.objects.get_or_create(**cat)
        course = Course.objects.create(category=category, **validated_data)
        # for ad in adrs:
        #     Branch.objects.get_or_create(course=course, **adrs)
        for con in contacts:
            Contact.objects.create(course=course, **con)
        return course

class CourseDetailSerializer(serializers.ModelSerializer):
    address = BranchSerializer(many=True, required=False)
    contacts = ContactSerializer(many=True)
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'logo', 'category', 'contacts', 'address']
