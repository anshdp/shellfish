from django.db import models

  
# Create your models here.
class User(models.Model):
    Email=models.CharField(max_length=100)
    phone_no=models.BigIntegerField()
    status=models.CharField(max_length=100,default="deactive") 
    created_date=models.DateField(auto_now_add=True)

class Account(models.Model):
    username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    user_type=models.CharField(max_length=100,default="user")
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)



