from rest_framework.routers import DefaultRouter
from product.viewset import ProductListRetrieveViewset, ProductViewset

router = DefaultRouter()

# ce router permet de faire tous les actions du CRUD
# router.register('product-b', ProductViewset, basename='product-a')

# tandisque celui ci ne fait que trois(03) List Retieve(detail)
router.register('product-b', ProductListRetrieveViewset, basename='product-a')

print(router.urls)

urlpatterns = router.urls
