from .models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


# Methode2 de Validation de donner
# def validate_product_name(value):
#     qs = Product.objects.filter(name__iexact=value)
#     if qs.exists():
#         raise serializers.ValidationError(
#             f"le produi '{value}' existe deja dans la base de donner")
#     return value


validators_unique_product_name = UniqueValidator(
    queryset=Product.objects.all())
