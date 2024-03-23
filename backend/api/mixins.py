from product.permissions import IsStaffPermission
from rest_framework import permissions


class StaffEditorPermissionsMixin():
    permission_class = [
        permissions.IsAdminUser,  # verrifie si l'utilisateur est admin ou simple
        IsStaffPermission
    ]


class UserQuerySetProductMixins():
    user_field = 'owner'

    def get_queryset(self):
        queryset = super().get_queryset()
        """ 
        l'action de decompage fait sur le dictionnaire est:
        dic={'user':'antoine'}
        **dic -> user=antoine latransformation fait par le double etoile
        """
        query_data = {}
        query_data[self.user_field] = self.request.user
        return queryset.filter(**query_data)
