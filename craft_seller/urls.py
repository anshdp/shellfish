from django.urls import path,include
from.import views

urlpatterns = [
    path('become_seller', views.become_seller_fun, name = 'become_seller'),
    path('seller_login', views.seller_login_fun, name = 'seller_login'),
    path('seller_signup', views.seller_signup_fun, name = 'seller_signup'),
    path('seller_dashboard', views.seller_dashboard_fun, name = 'seller_dashboard'),
    path('add_product', views.add_product_fun, name = 'add_product')

]