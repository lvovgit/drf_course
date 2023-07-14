from rest_framework import serializers
from course.models import Course, Lesson, Payments

class LessonCourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'preview', 'url_video', 'course']

class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

class CourseSerializers(serializers.ModelSerializer):
    """Задание 3
Для сериализатора для модели курса реализуйте поле вывода уроков."""
    all_lessons = LessonCourseSerializers(many=True, read_only=True, source='lesson_set')
    number_of_lesson = serializers.SerializerMethodField()

    def get_number_of_lesson(self, course):
        """Задание 1
Для модели курса добавьте в сериализатор поле вывода количества уроков."""
        lesson = Lesson.objects.filter(course=course)
        if lesson:
            return lesson.count()
        return 0

    class Meta:
        model = Course
        fields = ('id', 'name', 'preview', 'description', 'all_lessons', 'number_of_lesson')


class PaymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"