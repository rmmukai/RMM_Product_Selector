from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('products', views.all_product),
    path('products/add_prepreg', views.add_prepreg),
    path('products/create_prepreg', views.create_prepreg),
    path('products/add_carbon_fiber', views.add_carbon_fiber),
    path('products/create_carbon_fiber', views.create_carbon_fiber),
    path('products/<prepreg_id>/edit_prepreg', views.edit_prepreg),
    path('products/<prepreg_id>/update_prepreg', views.update_prepreg),
    path('products/<carbon_fiber_id>/edit_carbon_fiber', views.edit_carbon_fiber),
    path('products/<carbon_fiber_id>/update_carbon_fiber', views.update_carbon_fiber),
    path('products/<prepreg_id>/delete_prepreg', views.delete_prepreg),
    path('products/<carbon_fiber_id>/delete_carbon_fiber', views.delete_carbon_fiber),
    path('product_selector', views.product_selector),
]