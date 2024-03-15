from django.urls import path
from . import views


urlpatterns = [
    path('register-user/', views.register_user, name='register-user'),
    path('register-vendor/', views.register_vendor, name='register-vendor'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('my-account/', views.my_account, name='my-account'),
    path('cust-dashboard/', views.cust_dashboard, name='cust-dashboard'),
    path('vendor-dashboard/', views.vendor_dashboard, name='vendor-dashboard'),
]