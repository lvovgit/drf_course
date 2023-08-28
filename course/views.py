import stripe
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import viewsets, generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from course.paginators import LessonPaginator
from course.permissions import IsModerator
from course.serializers.serializers import *
from course.services import create_payment, checkout_session
from djangoProject4 import settings
from users.models import UserRoles
from course.tasks import send_updated_email
stripe.api_key = settings.STRIPE_SECRET_KEY


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator



    def perform_create(self, serializer) -> None:
        serializer.save(owner=self.request.user)  # Сохраняет новому объекту владельца

    def update(self, request, *args, **kwargs):
        send_updated_email(kwargs['pk'])

        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return Course.objects.all()
        else:
            return Course.objects.filter(owner=user)


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]#, IsModerator]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Course.objects.all()
        else:
            return Course.objects.filter(owner=user)

    def perform_create(self, serializer) -> None:
        """Сохраняет новому объекту владельца"""
        serializer.save(owner=self.request.user)


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=user)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()

    # permission_classes = [IsAuthenticated]  # , IsOwner]

    #
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=user)


class LessonDetailView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

    #
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=user)


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

    #
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=user)


class LessonDeleteView(generics.DestroyAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]  # , IsOwner]

    #
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=user)


class PaymentsListView(generics.ListAPIView):
    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['payment_type', 'course', 'lesson']
    filterset_class = FilterSet
    ordering_fields = ['payment_date']
    permission_classes = [IsAuthenticated]


"""Фильтрация для эндпоинтов вывода списка платежей с возможностями:
менять порядок сортировки по дате оплаты,
фильтровать по курсу или уроку,
фильтровать по способу оплаты."""


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionCourseSerialisers
    queryset = SubscriptionCourse.objects.all()
    permission_classes = [IsAuthenticated]


class SubscriptionUpdateView(generics.UpdateAPIView):
    serializer_class = SubscriptionCourseSerialisers
    queryset = SubscriptionCourse.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializers
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        session = checkout_session(
            course=serializer.validated_data['payed_course'],
            user=self.request.user
        )
        serializer.save()
        create_payment(course=serializer.validated_data['payed_course'],
                       user=self.request.user)
        return Response(session['id'], status=status.HTTP_201_CREATED)


class GetPaymentView(APIView):
    """Получение информации о платеже"""

    def get(self, request, payment_id):
        payment_intent = stripe.PaymentIntent.retrieve(payment_id)
        return Response({
            'status': payment_intent.status, })

