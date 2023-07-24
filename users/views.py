from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
# from users.serializers.serializers import UsersSerializers, ForAuthUserSerializers, ForCreateUserSerializers


# class UsersListView(generics.ListAPIView):
#     serializer_class = ForAuthUserSerializers
#     queryset = User.objects.all()
#     permission_classes = [IsAuthenticated]