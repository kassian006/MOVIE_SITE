from rest_framework import permissions


class CheckStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status == 'simple' and  obj.status_movie == "simple":
            return True
        elif request.user.status == 'pro':
            return True
        return False


class CheckAuthorHistory(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class CheckStatusActor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'pro':
            return True
        return False
