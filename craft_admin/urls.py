from django.urls import path,include
from.import views

urlpatterns = [
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('accountDetails',views.account_details,name='accountDetails'),
    path('changePassword',views.change_password,name='changePassword'),

    path('seller_details',views.seller_details,name='seller_details'),
    path('show_product',views.show_product,name='show_product'),
    path('seller_permission/<int:id>',views.seller_permission,name='seller_permission'),
    path('deleteProduct',views.delete_product,name='deleteProduct'),
    
    
]                                                   