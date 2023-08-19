from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course, Lesson
from users.models import User, UserRoles


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test1.com',
            is_superuser=True,
            is_active=True,
            role=UserRoles.MODERATOR, )
        self.course = Course.objects.create(

            name='Test',
            description='Test'
        )
        self.user.set_password('123')
        self.user.save()
        response = self.client.post('/api/token/', {"email": "test@test1.com", "password": "123"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_model_name = 'lesson_for_test'
        # self.response_course = self.client.post('/api/course/create/', {'name': self.test_model_name})

    def test_create_lesson(self):
        """Тест создания модели Lesson"""
        response = self.client.post('/api/lesson/create/', {
            'course': 1, 'name': self.test_model_name})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_lesson(self):
        """Тест деталей модели Lesson"""
        self.test_create_lesson()
        response = self.client.get(f'/api/lesson/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': 1, 'name': 'lesson_for_test', 'description': None, 'preview': None, 'url_video': None,
                          'course': 1, 'owner': None})

    def test_list_lesson(self):
        """Тест списка модели Lesson"""
        self.test_create_lesson()
        response = self.client.get('/api/lesson/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.json())
        self.assertEqual(response.json(), {'count': 2, 'next': None, 'previous': None, 'results': [
            {'id': 1, 'name': 'Lesson_for_test', 'description': None, 'preview': None, 'url_video': None, 'course': 1,
             'owner': None},
            {'id': 2, 'name': 'Lesson_for_test', 'description': None, 'preview': None, 'url_video': None, 'course': 1,
             'owner': None}]})
        self.assertEqual(Lesson.objects.all().count(), 2)

class SuperuserTestCase(APITestCase):
    """Тесты суперюзера"""

    def setUp(self) -> None:
        """Подготовка данных перед тестом"""
        self.superuser = User.objects.create(
                        email='superuser@user.com',
                        is_staff=False,
                        is_superuser=True,
                        is_active=True,
                        role=UserRoles.MEMBER,
                    )
        self.course = Course.objects.create(

            name='Test',
            description='Test'
        )
        self.superuser.set_password('123')
        self.superuser.save()
        response = self.client.post('/api/token/', {"email": "superuser@gmail.com", "password": "123"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_model_name = 'Lesson_for_test'
        self.response_course = self.client.post('/api/course/create/', {'name': self.test_model_name})

    def test_lesson_create(self):
        """Тест суперюзера"""
        response = self.client.post('/api/lesson/create/', {'course': 1, 'name': self.test_model_name, 'owner': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response2 = self.client.get('/api/lesson/')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)