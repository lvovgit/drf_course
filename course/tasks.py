from celery import shared_task
from django.core.mail import send_mail

from datetime import datetime, timedelta
from course.models import SubscriptionCourse
from djangoProject4 import settings
from users.models import User

@shared_task
def send_updated_email(course):
    subscribers_list = SubscriptionCourse.objects.filter(course=course)
    for sub in subscribers_list:
        print('Отправлено сообщение об обновлении')
        send_mail(
            subject="Обновление курса!",
            message=f"У курса {course.name} появилось обновление!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[sub.user]

        )

@shared_task
def check_user():

    now_date = datetime.now()
    one_month_ago = now_date - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago)
    inactive_users.update(is_active=False)
    print(inactive_users)