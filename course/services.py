from django.core.mail import send_mail
from django.conf import settings
from course.models import SubscriptionCourse


def course_update(object):
    subscriptions = SubscriptionCourse.objects.filter(user=object.user)
    for obj in subscriptions:
        send_mail(
            subject="Курс обновлен",
            message="Курс обновлен",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[obj.user.email],
            fail_silently=False
        )