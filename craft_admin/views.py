from django.shortcuts import render, redirect
from craft_seller.models import *
from craft.models import Account
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse




# Create your views here.
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def account_details(request):
    adminDetails = Account.objects.get(user_type='admin')
    return render(request, 'account_details.html', {'data':adminDetails})


def seller_details(request):

    seller_detail = SellerAccountDetails.objects.all()

    return render(request, 'seller_details.html', {"details": seller_detail})


@csrf_exempt
def change_password(request):

    try:
        oldPassword =  request.POST['oldPassword']
        newPassword = request.POST['newPassword']
        currentPassword = Account.objects.get(user_type='admin')


        if oldPassword in currentPassword:
            password_change = Account.objects.filter(Password=oldPassword).update(Password=newPassword)
            return JsonResponse({'message': 'Password changed'})

        else:
            return JsonResponse({'message': 'Incorrect Old password'})

    except Exception:
         return JsonResponse({'message': 'Incorrect Old password'})


def seller_permission(request, id):

    seller_detail = SellerAccountDetails.objects.get(id=id)

    if seller_detail.seller_status=="deactivate":
        SellerAccountDetails.objects.filter(id=id).update(seller_status='activate')

    else:
        SellerAccountDetails.objects.filter(id=id).update(seller_status='deactivate')

    return redirect('seller_details')


def show_product(request):

    try:

        products = FishDetails.objects.select_related('seller',)

        return render(request,'show_products.html',{"data":products})

    except Exception:
        return render(request,'show_products.html')


@csrf_exempt
def delete_product(request):
    try:

        productId = request.POST['productId']

        deleted_product = FishDetails.objects.filter(id=productId).delete()

        return JsonResponse({'message': 'Product deleted successfully'})

    except Exception:
        return JsonResponse({'message': 'An error occured'})
