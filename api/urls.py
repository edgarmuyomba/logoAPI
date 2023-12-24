from django.urls import path 
from . import views

app_name = 'api'

urlpatterns = [
    path('categories/', views.categories, name='categories'),
    path('category/<str:cat_name>/', views.category, name='category'),
    path('random/<int:num>/', views.random, name='random'),
    path('<str:company_name>/', views.company, name='company'),
]