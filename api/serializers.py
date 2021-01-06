from rest_framework.serializers import ModelSerializer
from Bill.models import ProductModel


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["product_name"]
