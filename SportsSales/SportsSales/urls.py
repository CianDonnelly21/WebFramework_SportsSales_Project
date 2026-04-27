"""
URL configuration for SportsSales project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from SportsSalesApp import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name = 'home'),
    path('admin/', admin.site.urls),
    path('order/', views.order),
    path('orderItem/', views.OrderItem),
    path('item/', views.items),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user = False), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(http_method_names=['get', 'post']), name='logout'),    path('all-orders/', views.all_orders, name = 'all_orders'),
path('update-order/<int:order_id>/', views.update_order_status, name='update_order')
]
