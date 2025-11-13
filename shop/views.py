
from rest_framework.generics import ListAPIView

from shop.models import Product
from shop.serializers import ProductSerializer


# Create your views here.



class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



