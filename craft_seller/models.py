from django.db import models

# Create your models here.
class SellerAccountDetails(models.Model):
      
    seller_mobile_no = models.CharField(max_length=100)
    seller_email = models.CharField(max_length=100)
    seller_Password = models.CharField(max_length=100)
    seller_status = models.CharField(max_length=100, default="deactivate")


class FishDetails(models.Model):

    fishName = models.CharField(max_length=100)
    fishCatogory = models.CharField(max_length=100)
    fishPrice = models.IntegerField()
    fishDiscountPrice = models.IntegerField()
    fishColor = models.CharField(max_length=100)
    fishQuantity = models.IntegerField()
    fishDescription = models.TextField()
    fishImage = models.CharField(max_length=100)
    seller = models.ForeignKey(SellerAccountDetails, on_delete = models.CASCADE)

