from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def become_seller_fun(request):
    return render(request, 'become_seller.html')

def seller_login_fun(request):
    if (request.method=="POST"):
        seller_username=request.POST['sellerEmail']
        seller_password=request.POST['sellerPass']
        try:
            user_data=SellerAccountDetails.objects.get(seller_email=seller_username)
            if (user_data.seller_email == seller_username and user_data.seller_Password == seller_password and user_data.seller_status == "activate"):
                return redirect('seller_dashboard')
            else:
                return redirect('seller_login')
        except SellerAccountDetails.DoesNotExist:
            return render(request, 'seller_login.html',{"message":"Login Failed"})
    return render(request, 'seller_login.html')


def seller_signup_fun(request):
    if(request.method=="POST"):
        seller_phone = request.POST['sellerNumber']
        seller_email = request.POST['sellerEmail']
        seller_password = request.POST['sellerPassword']
        sellerDetails = SellerAccountDetails(seller_mobile_no=seller_phone,seller_email=seller_email,seller_Password=seller_password)
        sellerDetails.save()
    return render(request, 'seller_signup.html')

def seller_dashboard_fun(request):
    return render(request, 'seller_dashboard.html')

def add_product_fun(request):
    return render(request, 'add_product.html')