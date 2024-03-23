from rest_framework import permissions


class IsStaffPermission(permissions.DjangoModelPermissions):

    """
        cette permission perssonaliser ne nous permet pas d'avoire la 
        mains totale sur et pour ça nous allons utiliser le perm_map pour 
        resoudre ce problem
    """
    # def has_permission(self, request, view):
    #     user = request.user
    #     if user.is_staff:
    #         # print("je fait partir du staff")
    #         # app_name.perm_name_model_name(add, delete, view, change) sachet que ces nom sont en minuscule
    #         print(user.has_perm)
    #         if user.has_perm('product.add_product'):
    #             return True
    #         if user.has_perm('product.change_product'):
    #             return True
    #         if user.has_perm('product.delete_product'):
    #             return True
    #         if user.has_perm('product.view_product'):
    #             return True

    #     return False

    # == La methode pour avoire le controle total sur nos permission

    # Nous pouvons laisser django gerer cette methode nativement et pour ça nous devons ajouter certain permission dans le permission_class et c'est pour quoi nous avons commenter notre  methode
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
