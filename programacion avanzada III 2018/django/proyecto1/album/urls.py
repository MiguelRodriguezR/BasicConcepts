from django.contrib import admin
from album import views
from django.urls import include, path

urlpatterns = [
    path('', views.first_view, name='first-view'),
    path('category/', views.category, name='category-list'),
]
