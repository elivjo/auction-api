from django.db import models
from datetime import timedelta, datetime, timezone
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """ Users profile """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Product(models.Model):
    """ Products attributes  """
    seller = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True) 
    name = models.CharField(max_length= 100)
    description = models.CharField(max_length = 200)
    price = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    photo = models.ImageField(null=True, blank=True, upload_to = "images/")
    final_bid = models.IntegerField(blank=True,null=True)
    winner = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True, related_name='auction_winner')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def has_expired(self):
        """ if a product has expiried or not  """
        now = datetime.now(timezone.utc)
        expired = self.end_date
        if now > expired:
            return True
        else:
            return False 
    
        
    def product_winner(self):
        """ define winner and amount for a product """
        if self.is_active:
            if self.has_expired():
                highest_bid = Bid.objects.filter(product=self).order_by('-bid').first()
                if highest_bid:
                    self.winner = highest_bid.user
                    self.final_bid = highest_bid.bid
                self.is_active = False
                self.save()
        

class Bid(models.Model):
    """ Bid for products by users """
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    bid = models.IntegerField()

    def __str__(self):
        return self.user.username 


