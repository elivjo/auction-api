from datetime import date, datetime
from django.db.models import query
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from rest_framework import status
from datetime import  datetime, timezone
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from ..models import Product, UserProfile, Bid
from .serializer import ListBidSerializer, ListProductSerializer, UserSerailizer
from .permissions import AuthorPermission, BidPermission

class ProductListAPIView(ListCreateAPIView):
    """ Create , list products """
    serializer_class = ListProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(name__istartswith=title)
        for a in queryset:
            a.product_winner()
        return queryset

    def perform_create(self, serializer):
        """ set seller when create products """""
        instance = serializer.save()
        #print(instance.id)
        instance.seller_id=self.request.user.id
        instance.save()

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    """ detajet , fshirja e produktit """
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    permission_classes = [AuthorPermission,]


class BidListAPIView(APIView):
    """ create, list bids """
    
    serializer_class = ListBidSerializer

    def get_queryset(self):
        queryset = Bid.objects.all()
        return queryset

    def get(self,request, format=None):
        queryset = self.get_queryset()
        serializer = ListBidSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        
        serializer = ListBidSerializer(data=request.data)
        if serializer.is_valid():
        #    if Product.objects.filter(is_active=False):
        #         return Response({'Error':'Auction has expired!' }, status.HTTP_400_BAD_REQUEST) 
            instance = serializer.save()
            instance.user_id = self.request.user.id
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BidDetailAPIView(RetrieveUpdateDestroyAPIView):
    """ details , delete bid """
    queryset = Bid.objects.all()
    serializer_class = ListBidSerializer
    permission_classes = [BidPermission,]

    def perform_create(self, serializer):
        """ set author when created bid """""
        serializer.save(user_id=self.request.user.id)