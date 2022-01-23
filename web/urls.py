from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('collection/<slug:collection_slug>/', views.products, name="poducts_by_collection"),
    path('<slug:collection_slug>/<slug:product_slug>/', views.product_detail, name="product_detail"),
]
