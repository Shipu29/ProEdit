from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('callback/', views.callback, name='callback'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/',
         views.product_detail, name='product_detail'),
    path('products/<int:product_id>/edit',
         views.product_edit, name='product_edit'),
]
