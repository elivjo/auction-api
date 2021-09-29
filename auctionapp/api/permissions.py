from rest_framework import permissions
from ..models import Product, UserProfile

class AuthorPermission(permissions.BasePermission):
    """ Seller that has his product can edit and the winner are read only"""
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj: Product):
        if obj.seller == request.user:
            return True
        if obj.winner.id == request.user.id and request.method in permissions.SAFE_METHODS:
            return True
        return False


class BidPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj: Product):
        if obj.user.id == request.user.id:
            return True
        return False
