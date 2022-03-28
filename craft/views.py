from django.shortcuts import render, redirect
from .models import Account, User, Wishlist, Cart, Orders
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from craft_seller.models import FishDetails
from traceback import format_exc
import razorpay


# Create your views here.

def home(request):
    return render(request, 'home.html')


def admin(request):
    return render(request, 'admin_dashbord.html')


def signup(request):

    if request.method == "POST":
        phone = request.POST['no']
        email = request.POST['email']
        password = request.POST['password_first']

        try:
            user_info = User(phone_no=phone, Email=email)
            user_info.save()
            account_info = n(
                username=email, Password=password, user_id_id=user_info.id)
            account_info.save()
            return redirect('signin')

        except Exception:
            return render(request, 'signup.html')

    return render(request, 'signup.html')


# check exist or not
@csrf_exempt
def check_exist(request):

    email = request.POST['Email1']

    existUser = Account.objects.filter(username=email).exists()

    return JsonResponse({'isExist': existUser})


# Login check----->
def user_login(request):

    if (request.method == 'POST'):
        user_name = request.POST['email']
        password = request.POST['password']

        try:
            current_user = Account.objects.get(username=user_name)

            if(current_user.username == user_name and current_user.Password == password and current_user.user_type == "admin"):
                return redirect('/craft_admin/admin_dashboard')

            elif (current_user.username == user_name and current_user.Password == password and current_user.user_type == "user"):
                request.session['logged_user'] = current_user.user_id_id
                return redirect('home')

        except User.DoesNotExist:
            return render(request, 'login.html', {'message': 'login failed'})

    return render(request, 'login.html')


def view_profile(request):

    try:

        if 'logged_user' in request.session:
            active_session = request.session['logged_user']
            active_user = User.objects.get(id=active_session)
            return render(request, 'profile.html', {'user': active_user})

        else:
            return redirect('login')

    except Exception:
        return render(request, 'login.html')


def user_logout(request):

    try:
        logout(request)
        return redirect('login')
    except Account.DoesNotExist:
        return render(request, 'login.html')


# adding a product
def products(request):

    userId = None

    if 'logged_user' in request.session:
        userId = request.session['logged_user']

    productsDb = FishDetails.objects.all()

    products = []

    if userId:
        for product in productsDb:
    
            productObj = {  
                'id': product.id,
                'fishImage': product.fishImage,
                'fishName': product.fishName,
                'fishDiscountPrice': product.fishDiscountPrice,
                'fishPrice': product.fishPrice
            }

            wishListObj = None
            try:
                wishListObj = Wishlist.objects.get(
                    user_id=userId, product_id=product.id)
            except Wishlist.DoesNotExist:
                pass

            if wishListObj:
                productObj['wishListId'] = wishListObj.id

            products.append(productObj)
    else:
        products = productsDb

    return render(request, 'product.html', {'data': products})


# Displaying products
def view_product(request, id):

    productDetails = FishDetails.objects.get(id=id)
 
    return render(request, 'Product_details.html', {"details": productDetails})


def show_wishlist(request):

    try:
        current_user = request.session['logged_user']

        wishlist_item = Wishlist.objects.select_related(
            'user', 'product').filter(user_id=current_user)

        return render(request, 'wishlist.html', {"item": wishlist_item})

    except Exception:
        return render(request, 'wishlist.html')


@csrf_exempt
def add_to_wishlist(request):

    try:

        productId = request.POST.get('productId')

        if productId is None:
            return JsonResponse({'statusCode': 400, 'message': 'bad request - product Id'})

        if 'logged_user' not in request.session:
            return JsonResponse({'statusCode': 401, 'message': 'Please login to add product to wishlist'})

        userId = request.session['logged_user']

        wishlistItem = Wishlist(user_id=userId, product_id=productId)
        wishlistItem.save()

        return JsonResponse({'statusCode': 200, 'wishlistItemId': wishlistItem.id, 'message': 'Successfully added to wishlist'})

    except Exception:
        error = format_exc()
        print(error)
        return JsonResponse({'statusCode': 500, 'message': 'An error occured', 'error': str(error)})


@csrf_exempt
def remove_wishlist(request):

    productId = request.POST.get('productId')

    userId = request.session['logged_user']

    if 'logged_user' not in request.session:
        return JsonResponse({'statusCode': 401, 'message': 'Please login to delete product to wishlist'})

    Wishlist.objects.get(user_id=userId, product_id=productId).delete()

    return JsonResponse({'statusCode': 200, 'message': 'Removed from wishlist'})


def show_cart(request):

    try:

        currentUser = request.session['logged_user']

        if currentUser:
            cart_item = Cart.objects.filter(user=currentUser)

            returnData = {
                "totalAmount": 0,
                "totalDiscountAmount": 0,
                "totalCount": 0,
                'items': cart_item
            }

            for i in cart_item:
                returnData['totalAmount'] += i.product.fishPrice
                returnData['totalDiscountAmount'] += i.product.fishDiscountPrice
                returnData['totalCount'] += 1

            return render(request, 'cart.html', returnData)
        else:
            print("work else")
            return render(request, 'cart.html')
    except Exception:
        print("work exception")
        error = format_exc()
        print(error)
        return render(request, 'login.html')


@csrf_exempt
def add_to_cart(request):

    try:

        productId = request.POST.get("productId")
        # quantity = request.POST.get("quantity")
        # print(quantity)

        if productId is None:
            return JsonResponse({'message': 'An error occured.'})

        if 'logged_user' not in request.session:
            return JsonResponse({'message': 'You need to Login first '})

        userId = request.session['logged_user']

        cartItem = Cart(user_id=userId, product_id=productId)
        cartItem.save()

    except Exception:
        error = format_exc()
        print(error)
        return JsonResponse({'message': 'Already in cartlist'})

    return JsonResponse({'message': 'Product added to cart'})


@csrf_exempt
def order_product(request):

    userid=request.session['logged_user']
    order_amount = request.POST['totalAmount']
    print(order_amount, userid)
    
    products_orderdata = Orders.objects.filter(user=userid, delivery_status='added_to_bag')

    order_amount = request.POST['totalAmount']
    order_currency = 'INR'
    order_receipt = 'order_receipt_id_11'
    notes = {'Shipping address': 'Jayanagar, Bangalore'}

    client = razorpay.Client(auth=('rzp_test_8QBbmYcRc73Nly','eMi0lcgeGNYR5oKz37sWPYjF'))

    payment = client.order.create({"amount": order_amount, "currency": order_currency, "receipt": order_receipt, 'notes': notes})

    return JsonResponse(payment)


@csrf_exempt
def update_payment(request):

    userid = User.objects.get(id=request.session['logged_user'])
    orderId = request.POST['orderId']
    paymentId = request.POST['paymentId']
    paymentId = request.POST['orderId']
    paymentAmount = request.POST['paymentAmount']
    print(paymentAmount)

    order_details = Orders(user=userid, delivery_status='order placed', payment_type='Online payment', order_id=orderId, payment_id=paymentId, payment_amount=paymentAmount)
    order_details.save()

    Cart.objects.filter(user=userid).delete()

    return JsonResponse({'resp': "success"})
