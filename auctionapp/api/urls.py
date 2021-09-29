from django.urls import include,path
from rest_framework.routers import DefaultRouter
from .views import ProductListAPIView, BidListAPIView,ProductDetailAPIView,BidDetailAPIView


router = DefaultRouter()

urlpatterns = [
            path("", include(router.urls)),
            path('products/', ProductListAPIView.as_view(), name= "products-list"),
            path('products/<int:pk>', ProductDetailAPIView.as_view(), name= "products-detail"),
            path('bids/', BidListAPIView.as_view(), name= "bids-list"),
            path('bids/<int:pk>', BidDetailAPIView.as_view(), name= "bids-detail"),

            
]