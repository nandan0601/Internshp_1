from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.get_all_products),
    path('api/products/<int:pk>/', views.get_product_by_id),
    path('api/products/add/', views.add_product),
    
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_form, name='product_form'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
]
