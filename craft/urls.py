from django.urls import path,include
from.import views

urlpatterns = [
    # path('dash',views.dashFn,name='dash')
    path('home',views.home, name ='home'),
    path('signup',views.signup, name ='sign'),
    path('login',views.user_login,name ='login'),
    path('profile',views.view_profile, name ='profile'),
    path('admin_dashbord',views.admin, name ='admin_dashbord'),
    path('logout',views.user_logout, name ='logout'),
    path('product',views.products, name ='product'),
    path('product_details/<int:id>',views.Product_details, name = 'product_details'),
    path('checkExist',views.check_exist, name ='checkExist'),


]