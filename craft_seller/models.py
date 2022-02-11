from django.db import models

# Create your models here.
class SellerAccountDetails(models.Model):  

    seller_mobile_no=models.CharField(max_length=100)
    seller_email=models.CharField(max_length=100)
    seller_Password=models.CharField(max_length=100)
    seller_status=models.CharField(max_length=100,default="deactivate")