from django.urls import path,include
from . import views

urlpatterns = [
    # path('dash',views.dashFn,name='dash')
    path('home',views.home, name ='home'),
    path('signup',views.signup, name ='signup'),
    path('login',views.user_login,name ='login'),
    path('profile',views.view_profile, name ='profile'),
    path('admin_dashbord',views.admin, name ='admin_dashbord'),
    path('logout',views.user_logout, name ='logout'),
    path('product',views.products, name ='product'),
    path('product_details/<int:id>',views.view_product, name = 'product_details'),
    path('checkExist',views.check_exist, name ='checkExist'),
    path('wishlist',views.add_to_wishlist, name ='wishlist'),
    path('wishlist_page',views.show_wishlist, name ='wishlist_page'),
    path('remove_wishlist',views.remove_wishlist, name ='remove_wishlist'),
    path('cart',views.show_cart, name ='cart'),
    path('add_to_cart',views.add_to_cart, name ='add_to_cart'),
    path('orderProduct',views.order_product, name ='orderProduct'),
    path('updatePayment',views.update_payment, name ='updatePayment')

]