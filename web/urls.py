from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<slug:collection_slug>/', views.products, name="poducts_by_collection"),
]
