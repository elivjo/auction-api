from rest_framework import serializers 
from auctionapp.models import Product , UserProfile, Bid


class UserSerailizer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ['name', 'last_name']


class ListProductSerializer(serializers.ModelSerializer):
    winner = serializers.CharField(read_only=True)
    seller_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        exclude = [ 'seller'] 
        read_only_fields = ['final_bid',]   

    
    @staticmethod
    def get_seller_name(obj):
        return obj.seller.username if obj.seller else None 

    # @staticmethod
    # def get_photo(obj):
    #     image_url = ""
    #     if obj.photo:
    #         image_url = obj.photo.url
    #     return image_url
    

class ListBidSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bid
        exclude = ['user']
        #fields = '__all__'
  
    