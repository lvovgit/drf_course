from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from course.models import Course, Lesson, Payments
# from course.permissions import IsModerator
from course.serializers.serializers import CourseSerializers, LessonSerializers, PaymentsSerializers
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
# from users.models import UserRoles


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()
    # permission_classes = [IsAuthenticated]
    #
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
    #         return Course.objects.all()
    #     else:
    #         return Course.objects.filter(owner=user)


# class CourseCreateAPIView(generics.CreateAPIView):
#     serializer_class = CourseSerializers
#     queryset = Course.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator]
    #
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return Course.objects.all()
    #     else:
    #         return Course.objects.filter(owner=user)


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated]
    #
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
    #         return Lesson.objects.all()
    #     else:
    #         return Lesson.objects.filter(owner=user)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator]
    #
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return Lesson.objects.all()
    #     else:
    #         return Lesson.objects.filter(owner=user)


class LessonDetailView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated]
    #
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
    #         return Lesson.objects.all()
    #     else:
    #         return Lesson.objects.filter(owner=user)


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated]
    #
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
    #         return Lesson.objects.all()
    #     else:
    #         return Lesson.objects.filter(owner=user)


class LessonDeleteView(generics.DestroyAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator]
    #
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return Lesson.objects.all()
    #     else:
    #         return Lesson.objects.filter(owner=user)


class PaymentsListView(generics.ListAPIView):
    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['payment_type', 'course', 'lesson']
    # filterset_class = FilterSet
    ordering_fields = ['payment_date']
    # permission_classes = [IsAuthenticated]

"""Фильтрация для эндпоинтов вывода списка платежей с возможностями:
менять порядок сортировки по дате оплаты,
фильтровать по курсу или уроку,
фильтровать по способу оплаты."""