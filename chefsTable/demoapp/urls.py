from django.urls import path 
from . import views 

urlpatterns = [  
    path('drinks/<str:drink_name>/', views.drinks, name='drinks'), 
    path('form/', views.form_view, name='form_view'),
    path('model-form/', views.modelForm_view, name='model_form_view'),

    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path("home", views.home, name="home"),
    path("contact", views.contact, name="contact"),

   
]