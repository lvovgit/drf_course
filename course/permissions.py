from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    """Заведите группу модераторов и опишите для нее права работы с любыми уроками или курсами, но без возможности их
    удалять и создавать новые. Заложите функционал такой проверки в контроллеры. Опишите права доступа для объектов
    таким образом, чтобы пользователи, которые не входят в группу модераторов, могли видеть и редактировать только
    свои курсы и уроки."""

    message = 'Вы являетесь модератором!'

    def has_permission(self, request, view):
        if request.user.is_staff or request.user.role == UserRoles.MODERATOR and request.method in ['POST', 'DELETE']:
            return False
        return True

# class IsOwner(BasePermission):
#
#     message = 'Вы не являетесь модератором или владельцем!'
#
#     def has_object_permission(self, request, view, obj):
#         if request.user == obj.owner:
#             return True
#         elif request.user.is_superuser:
#             return True
#         return False