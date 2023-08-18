from rest_framework import serializers

from course.models import Payments
from users.models import User


class UserPaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class UsersSerializers(serializers.ModelSerializer):
    """* Дополнительное задание
Для профиля пользователя сделайте вывод истории платежей, расширив сериализатор для вывода списка платежей."""
    all_payments = UserPaymentSerializers(many=True, read_only=True, source='payments_set')

    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'city', 'all_payments', 'role')


class ForAuthUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'city')


class ForCreateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
