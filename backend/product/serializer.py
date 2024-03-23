from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializer import UserPublicSerializer
from .models import Product
from .validators import validators_unique_product_name


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    # owner = serializers.SerializerMethodField(read_only=True)
    owner = UserPublicSerializer(source="user", read_only=True)

    # Redirection des lien a traver le serializer avec la premierre et deuxieme method
    # url = serializers.SerializerMethodField(read_only=True)

    # Troisieme method de redirection des liens
    url = serializers.HyperlinkedIdentityField(
        view_name='api_detailview', lookup_field='pk')

    email = serializers.EmailField(write_only=True)

    # Validation de donner champ de validation
    # name = serializers.CharField()

    # Validation de donner champ de validation
    name = serializers.CharField(validators=[validators_unique_product_name])

    # permet d'eviter l'affichage du champt user
    user_name = serializers.CharField(source='user', read_only=True)

    class Meta:
        model = Product
        # fields = ('owner', 'user_name', 'email', 'url', 'pk', 'name', 'price', 'content',
        #           'my_discount', 'get_discount')
        fields = ('user_name', 'email', 'url', 'pk', 'name', 'price', 'content',
                  'my_discount', 'get_discount')

    # Methode1 de Validation de donner
    # def validate_name(self, value):
    #     qs = Product.objects.filter(name__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(
    #             f"le produi '{value}' existe deja dans la base de donner")
    #     return value

    # Methode2 de Validation de donner

    # premierer methode pour metre en place le mail

    # def create(self, validated_data):
    #     print(validated_data)
    #     # cette methode permet d'enlever l'element passer en parametre danas la liste
    #     email = validated_data.pop('email')
    #     print(email)
    #     print(validated_data)
    #     return Product.objects.create(**validated_data)

    # deuxieme methode pour metre en place le mail
    # def create(self, validated_data):
    #     print(validated_data)
    #     # cette methode permet d'enlever l'element passer en parametre danas la liste
    #     email = validated_data.pop('email')
    #     print(email)
    #     print(validated_data)
    #     obj = super().create(validated_data)
    #     return obj

    # premire method pour afficher le chemin des produit de detail
    # def get_url(self, obj):
    #     return f"/product/{obj.pk}/deatil"

    # Deuxiemme methode pour afficher le chemin des produit de detail
    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("api_detailview", kwargs={'pk': obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount

    # ceci permet de metre ajour un champ
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name')
    #     return instance

    # ceci permet de metre ajour un champ et c'est la deuxieme methode

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        return super().update(instance, validated_data)

    # dfffg
    def get_owner(self, obj):
        return {'username': obj.user.username, 'id': obj.user.id}
