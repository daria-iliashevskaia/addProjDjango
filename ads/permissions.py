from rest_framework.permissions import BasePermission

from ads.models import Selections, User, Ads


class SelectionsUpdatePermission(BasePermission):
    message = "It is not your selection"

    def has_permission(self, request, view):

        obj = Selections.objects.get(pk=view.kwargs["pk"])

        if obj.owner_id == request.user.id:
            return True
        return False


class AdsUpdatePermission(BasePermission):

    message = "It is not your ad or you are not ADMIN/MODERATOR"

    def has_permission(self, request, view):

        if request.user.role in [User.MODERATOR, User.ADMIN]:
            return True

        obj = Ads.objects.get(pk=view.kwargs["pk"])

        if obj.author_id == request.user.id:
            return True
        return False
    