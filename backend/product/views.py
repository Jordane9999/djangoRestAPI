from django.http import JsonResponse
from .models import Product

from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ProductSerializer

# Utilisation d'un token personnaliser
from .authentication import TokenAuthentication

# Utilisation du concepte de mixins pour eviter la repetition des codes de permission
from api.mixins import StaffEditorPermissionsMixin, UserQuerySetProductMixins


# Utilisation des vue gerique dans django rest framework
from rest_framework import authentication, generics, mixins, permissions

# Permission personaliser
from .permissions import IsStaffPermission


# Create your views here.

# ici on as utiliser du django pure pour ecrire une api

"""
def api_view(request):
    # request != requests
    # "request" est une instance de la class HttpRequest
    # "requests" est une librairie
    # c'est ce qu'ont appelle la serialisation(transformer les dans un autre format) et c'est sur json ici
    query = Product.objects.all().order_by('?').first()
    data = {}
    # Ce sont deux methode recuperation de donner dans la base de donner
    # if query:
    # data['name'] = query.name
    # data['content'] = query.content
    # data['price'] = query.price
    # Serialization : Mettre des donner sous forme de dictionnaire en python
    if query:
        data = model_to_dict(query)
    return JsonResponse(data)
"""

# Maintenant ici on va le faire avec django rest framework


# @api_view(["GET"]) permet de reccuperrer les donner de la base de donner
@api_view(["POST"])
def api_view(request):
    # request != requests
    # "request" est une instance de la class HttpRequest
    # "requests" est une librairie
    # c'est ce qu'ont appelle la serialisation(transformer les dans un autre format) et c'est sur json ici
    # if request.method != "POST":
    #     return Response({'detail': 'method "GET" not allowed'}, status=405)
    # query = Product.objects.all().order_by('?').first() # cette requete permet de reccuperer les donner aleatoirement de la base de donner
    # data = {}
    # if query:
    #     # data = model_to_dict(query, fields=(
    #     #     'name', 'price', 'content', 'get_discount'))
    #     data = ProductSerializer(query).data

    ## Envoie des donner dans la base de donner
    # convertion des donner en dictionnaire avec la class ProductSerializer
    serializer = ProductSerializer(data=request.data)
    # print(serializer)
    # raise_exception=True elle permet d'afficher les erreur lors de l'envoie des donner
    # verrifie la validiter des donner et l'enregistre
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'detail': 'invalid data'})

# ============Utilisation des class dans djans rest framework============

# == Vue de detaille


class DetailProductView(StaffEditorPermissionsMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# == Vue de Creation


class CreateProductView(StaffEditorPermissionsMixin, generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)


# == Permet de creer et de lister les element du model
class ListCreateProductView(UserQuerySetProductMixins, StaffEditorPermissionsMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Celle ci nous permet de metre en place des type d'authentification
    # authentication_classes = [authentication.SessionAuthentication]
    """ 
    Du fait qu'on a definir des parametre par defaut dans le seting et l'authentication_classes en fait partire on peut l'enlever 
    """
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     # authentication.TokenAuthentication # ceci est l'authentification par defaut
    #     TokenAuthentication  # ceci c'est l'authentification perssonnaliser
    # ]
    # Ceci nous permet de mettre en place des permission pour l'exploitation de notre api par un tierce
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.DjangoModelPermissions]
    # Utilisation des permission personnaliser, il faut savoire que les permission sont mise par ordre de prioriter et c'est commme cela qu'elle sera gerer par django
    """ 
    Pour eviter la repetition des codes de permission nous avons utiliser le concept de mixins pour redure la quantiter de code a ecrire, et à envoyer la class comme un parametre donc nous avons plus besoin de mettre le permission_classes
    """
    # permission_classes = [
    #     permissions.IsAdminUser,  # verrifie si l'utilisateur est admin ou simple
    #     IsStaffPermission
    # ]
    user_field = 'user'

    def perform_create(self, serializer):
        # methode pour metre en place le champ email sans l'envoyer dans la base de donner
        email = serializer.validated_data.pop('email')
        print(email)
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content, user=self.request.user)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     user = self.request.user
    #     return queryset.filter(user=user)


# == Cette class permet de mettre ajour un produit deja existant


class UpdateProductView(StaffEditorPermissionsMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    """ pour realiser le performe update il faut le faire sur un  "put" pour qu'elle se realise et elle ne marche pas sur un "patch"
    """

    # def perform_update(self, serializer):
    #     name = serializer.validated_data.get('name')
    #     content = serializer.validated_data.get('content') or None
    #     if content is None:
    #         content = name
    #     serializer.save(content=content)

# == Supprimer un produit


class DeleteProductView(StaffEditorPermissionsMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


# == Il permet de faire une liste des elements du models et aussi la pagination c'est la seconde methode de listage et elle n'est a utiliser en car d'estreme neccessiter
class ListProductView(StaffEditorPermissionsMixin, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return super().get_queryset().filter(name__icontains='past')


# =========Creation des actions precedente en utilisant une seule class=============

class ProductMixinsViews(
        generics.GenericAPIView,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        mixins.DestroyModelMixin,
        mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)

    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
