from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer, CategorySerializer, CourseDetailSerializer
from .models import Category, Course

class CategoryView(APIView):
    def get_queryset(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories)
        return Response(serializer.data)

class CourseList(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CourseDetail(APIView):
    def get(self, request, pk, format=None):
        course = Course.objects.get(pk=pk)
        serializer = CourseDetailSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
