from django.urls import path

from shop.views import ProductListAPIView

urlpatterns = [
    path('list/', ProductListAPIView.as_view(), name='product-list'),
]

