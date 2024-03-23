from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import CreateProductView, ListProductView, ProductMixinsViews, api_view, DetailProductView, UpdateProductView, DeleteProductView, ListCreateProductView

urlpatterns = [
    path("", api_view, name="api_view"),
    path("<int:pk>/detail", DetailProductView.as_view(), name="api_detailview"),
    path("create/", CreateProductView.as_view(), name="api_createview"),
    path("list/", ListCreateProductView.as_view(), name="api_listview"),
    path("list2/", ListProductView.as_view(), name="api_list2view"),
    path("update/<int:pk>/", UpdateProductView.as_view(), name="api_updateview"),
    path("delete/<int:pk>/", DeleteProductView.as_view(), name="api_deleteview"),
    path("auth/", obtain_auth_token),

    # ========Utilisation du mixins============

    path("mixins/create/", ProductMixinsViews.as_view()),
    path("mixins/list/", ProductMixinsViews.as_view()),
    path("mixins/update/<int:pk>/", ProductMixinsViews.as_view()),
    path("mixins/delete/<int:pk>/", ProductMixinsViews.as_view()),
    path("mixins/<int:pk>/", ProductMixinsViews.as_view()),
]
