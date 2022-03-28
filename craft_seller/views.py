from django.shortcuts import render, redirect
from .models import *
from random import random
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
def become_seller(request):
    return render(request, 'become_seller.html')


def seller_login(request):

    if (request.method=="POST"):
        seller_username=request.POST['sellerEmail']
        seller_password=request.POST['sellerPass']

        try:

            seller_data=SellerAccountDetails.objects.get(seller_email=seller_username)
       
            if (seller_data.seller_email == seller_username and seller_data.seller_Password == seller_password and seller_data.seller_status == "activate"):
                request.session['logged_seller'] = seller_data.id #-->>create a session named loggedUser & user.id save to that session
                return redirect('seller_dashboard')

            else:
                return redirect('seller_login')

        except SellerAccountDetails.DoesNotExist:
            return render(request, 'seller_login.html',{"message":"Login Failed"})

    return render(request, 'seller_login.html')


def seller_signup(request):

    try:
        
        if(request.method=="POST"):
            seller_phone = request.POST['sellerNumber']
            seller_email = request.POST['sellerEmail']
            seller_password = request.POST['sellerPassword']
            sellerDetails = SellerAccountDetails(seller_mobile_no=seller_phone,seller_email=seller_email,seller_Password=seller_password)
            sellerDetails.save()

    except Exception:
        return render(request, 'seller_signup.html')

    return render(request, 'seller_signup.html')


def seller_dashboard(request):
    return render(request, 'seller_dashboard.html')


def seller_profile(request):
    
    try:

        if 'logged_seller' in request.session: 
            current_user = request.session['logged_seller']
            print(current_user)
            seller_detail=SellerAccountDetails.objects.get(id = current_user)
            return render(request, 'seller_profile.html', {"user_data": seller_detail})

        else:
            return redirect('seller_login')

    except Exception:
        return render(request, 'seller_login.html')


def seller_logout(request):

    try:
        logout(request)
        return redirect('seller_login')

    except Account.DoesNotExist:
        return render(request, 'seller_login.html')

    return render(request, 'seller_login.html')


def add_product(request):

    try:

        sellerId = request.session['logged_seller']
        if request.method == 'POST':
            fish_name = request.POST['name']
            fish_category = request.POST['category']
            fish_price = request.POST['price']
            fish_discount_price = request.POST['discount_price']
            fish_color = request.POST['color']
            fish_quantity = request.POST['quantity']
            fish_description = request.POST['description']
            image = request.FILES['image']
            fish_image = str(random())+image.name
            addImage=FileSystemStorage()
            addImage.save(fish_image, image)
            seller_id = sellerId
            fish_details = FishDetails(fishName=fish_name, fishCatogory=fish_category, fishPrice=fish_price, fishDiscountPrice=fish_discount_price, fishColor=fish_color, fishQuantity=fish_quantity, fishDescription=fish_description, fishImage=fish_image, seller_id=seller_id)
            fish_details.save()
            return render(request, 'add_product.html')
        return render(request, 'add_product.html')

    except Exception:
        return render(request, 'seller_login.html')



def view_product(request):

    try:

        user_id = request.session['logged_seller']

        currentUserProducts = FishDetails.objects.filter(seller_id=user_id)

        example_data = FishDetails.objects.select_related('seller')

    except Exception:
        return redirect(seller_login)

    return render(request, 'view_products.html', {'products': currentUserProducts})


def seller_orders(request):
    return render(request, 'seller_orders.html')



@csrf_exempt
def update_product(request):
    return JsonResponse({'message':'Product updated Successfully'})