from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('drinks/<str:drink_name>/', views.drinks, name='drinks'), 
] 