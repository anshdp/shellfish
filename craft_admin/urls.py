from django.urls import path,include
from.import views

urlpatterns = [
    path('admin_dashboard',views.adminDash,name='admin_dashboard'),
    path('seller_details',views.seller_details_fun,name='seller_details'),
    path('seller_permission/<int:id>',views.seller_permission_fun,name='seller_permission'),
]