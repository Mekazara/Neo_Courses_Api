from django.test import SimpleTestCase, TestCase, Client

from django.urls import reverse, resolve
from courses.views import CourseList, CourseDetail
from courses.models import Course
import json

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func.view_class, CourseList)

    def test_detail_url_is_resolved(self):
        url = reverse('course_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, CourseDetail)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.test = Course.objects.create(
            name='test',
            description='test test',
            category=None
        )
        self.test.save()
        self.detail = reverse('course_detail', args=[1])
    
    def test_courses_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_detail_GET(self):
        response2 = self.client.get(self.detail)
        self.assertEquals(response2.status_code, 200)

