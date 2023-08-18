from rest_framework import serializers
from course.models import Course, Lesson, Payments, SubscriptionCourse
from course.validators import UrlValidator


# class LessonCourseSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Lesson
#         fields = ['id', 'name', 'description', 'preview', 'url_video', 'course']


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field='url')]


class CourseSerializers(serializers.ModelSerializer):
    """
Для сериализатора для модели курса реализуйте поле вывода уроков."""
    all_lessons = LessonSerializers(many=True, read_only=True, source='lesson_set')
    number_of_lesson = serializers.SerializerMethodField()
    subscribers = serializers.SerializerMethodField()

    def get_number_of_lesson(self, course):
        """
Для модели курса добавьте в сериализатор поле вывода количества уроков."""
        lesson = Lesson.objects.filter(course=course)
        if lesson:
            return lesson.count()
        return 0

    def get_subscribers(self, instance):
        user = self.context['request'].user

        if SubscriptionCourse.objects.filter(user=user, course=instance).exists():
            return True
        else:
            return False

    class Meta:
        model = Course
        fields = ('id', 'name', 'preview', 'description', 'all_lessons', 'number_of_lesson', 'subscribers')


class PaymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class SubscriptionCourseSerialisers(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionCourse
        fields = "__all__"
