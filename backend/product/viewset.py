from .models import Product
from .serializer import ProductSerializer
from rest_framework import mixins, viewsets


class ProductViewset(viewsets.ModelViewSet):

    """ 
    Les Methode dont nous aurons besoin et que supporte cette vue

    get    -> list -> queryset
    get    -> retrieve(detail)
    post   -> create
    put    -> update
    patch  -> partial update
    delete -> destroy

    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListRetrieveViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
