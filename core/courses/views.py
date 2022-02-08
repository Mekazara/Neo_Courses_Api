from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CourseSerializer
from .models import Course


class CourseList(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
