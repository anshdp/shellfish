from django.db import models
from craft_seller.models import FishDetails

# Create your models here.
class User(models.Model):

    Email = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    status = models.CharField(max_length=100,default="  ") 
    created_date = models.DateField(auto_now_add=True)


class Account(models.Model):

    username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100,default="user")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Wishlist(models.Model):

    class Meta:
        unique_together = (('user', 'product'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(FishDetails, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):

    class Meta:
        unique_together = (('user', 'product'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(FishDetails, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    # p_quantity = models.IntegerField()


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_status = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=50)
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    payment_amount = models.IntegerField()
    

    

