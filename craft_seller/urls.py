from django.urls import path,include
from.import views

urlpatterns = [
    path('become_seller', views.become_seller, name = 'become_seller'),
    path('seller_login', views.seller_login, name = 'seller_login'),
    path('seller_signup', views.seller_signup, name = 'seller_signup'),
    path('seller_profile', views.seller_profile, name = 'seller_profile'),
    path('seller_dashboard', views.seller_dashboard, name = 'seller_dashboard'),
    path('add_product', views.add_product, name = 'add_product'),
    path('view_products', views.view_product, name = 'view_products'),
    path('seller_logout', views.seller_logout, name = 'seller_logout'),
    path('UpdateProduct', views.update_product, name = 'UpdateProduct'),
    path('sellerOrders', views.seller_orders, name = 'sellerOrders'),

    
]