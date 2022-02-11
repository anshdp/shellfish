from django.shortcuts import render, redirect
from craft_seller.models import *


# Create your views here.
def adminDash(request):
    return render(request, 'admin_dashboard.html')

def seller_details_fun(request):
    seller_detail=SellerAccountDetails.objects.all()
    return render(request, 'seller_details.html',{"details":seller_detail})

def seller_permission_fun(request, id):
    seller_detail=SellerAccountDetails.objects.get(id=id)
    if seller_detail.seller_status=="deactivate":
        SellerAccountDetails.objects.filter(id=id).update(seller_status='activate')
    else:
        SellerAccountDetails.objects.filter(id=id).update(seller_status='deactivate')
    return redirect('seller_details')

    