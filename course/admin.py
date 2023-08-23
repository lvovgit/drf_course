from django.contrib import admin
from course.models import *

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'preview', 'description', 'owner', 'price')
    list_filter = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'owner',)
    list_filter = ('name', )
@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'course', 'lesson', 'payment_sum', 'payment_type')
    list_filter = ('user', )