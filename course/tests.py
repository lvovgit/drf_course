from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course
from users.models import User

class LessonTestCase(APITestCase):
    def setUP(self) -> None:
        self.user = User.objects.create(
            email='test@test1.com',
            is_superuser=True,
        )
        self.course = Course.objects.create(
            name='Test',
            description='Test'
        )
        self.user.set_password('123')
        self.user.save()
        response = self.client.post('/api/token/', {'email': 'test@test1.com', 'password': '123'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_model_name = 'lesson_for_test'

    def test_create_lesson(self):
        """Тест создания модели Lesson"""
        response = self.client.post('/api/lesson/create/', {
            'course': '1',
            'name': 'django',
            'desctiption': 'тема',
            'url_video': 'https://www.youtube.com/watch?v=5vVwjSIixuQ'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
