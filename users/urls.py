from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import *
urlpatterns = [
    path('users/', UsersListView.as_view(), name='users_list'),
    path('users/<int:pk>/', UsersDetailView.as_view(), name='users_list'),
    path('user/create/', UsersCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/update/', UsersUpdateView.as_view(), name='user_update'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]#
