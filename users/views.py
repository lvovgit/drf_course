from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers.serializers import UsersSerializers
from users.serializers.serializers import UsersSerializers, ForAuthUserSerializers


class UsersListView(generics.ListAPIView):
    serializer_class = UsersSerializers
    queryset = User.objects.all()


class UsersDetailView(generics.RetrieveAPIView):
    serializer_class = ForAuthUserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(user=user)