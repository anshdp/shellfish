from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt





# Create your views here.

def home(request):
    return render( request,'home.html')

def admin(request):
    return render(request,'admin_dashbord.html')
            
def signup(request):
    if request.method == "POST":
        phone=request.POST['no']
        email=request.POST['email']
        username=request.POST['email']
        password=request.POST['password_first']
        print(phone)
        try:
            user_info=User(phone_no=phone,Email=email)
            user_info.save()
            print(user_info.id)
            account_info=Account(username=email,Password=password,user_id_id=user_info.id)
            account_info.save()
            return redirect('signin')
        except:
            return render(request,'signup.html')
    return render(request,'signup.html')

#Login check----->
def user_login(request):
    if (request.method=='POST'):
        user_name=request.POST['email']
        password=request.POST['password']
        try:
            current_user=Account.objects.get(username=user_name)
            if(current_user.username==user_name and current_user.Password==password and current_user.user_type=="admin"):
                return redirect('/craft_admin/admin_dashboard')
            elif (current_user.username==user_name and current_user.Password==password and current_user.user_type=="user"):
                 print(current_user.user_id_id)
                 request.session['logged_user']=current_user.user_id_id #-->>create a session named loggedUser & user.id save to that session
                 return redirect('home')        
        except User.DoesNotExist:
            return render(request,'login.html',{'message' : 'login failed'})
    return render( request,'login.html')

def view_profile(request):
    try:
        if 'logged_user' in request.session: 
            active_session = request.session['logged_user']
            active_user = User.objects.get(id = active_session)
            return render(request, 'profile.html', {'user': active_user})
        else:
            return redirect('login')
    except Exception:
        return render(request,'login.html')
        
def user_logout(request): 
    try:
        logout(request)
        return redirect('login')
    except Account.DoesNotExist:
        return render(request,'login.html')

#adding a product
def products(request):
     return render( request, 'product.html')

#Displaying products
def Product_details(request, id):
    # product_object = products.objects.get(id=id)
    return render(request, 'Product_details.html')

# check exist or not   
@csrf_exempt
def check_exist(request):
    email=request.POST['Email1']
    existUser=Account.objects.filter(username=email).exists()
    print(existUser)
    return JsonResponse({'isExist':existUser})
    