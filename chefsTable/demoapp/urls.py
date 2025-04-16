from django.urls import path 
from . import views 

urlpatterns = [  
    path('', views.index, name='index'),
    path('drinks/<str:drink_name>/', views.drinks, name='drinks'), 
    path('form/', views.form_view, name='form_view'),
    path('model-form/', views.modelForm_view, name='model_form_view'),

    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path("home/", views.home, name="home"),
    path("contact", views.contact, name="contact"),

    path('create/', views.EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('show/<int:pk>', views.EmployeeDetail.as_view(), name = 'EmployeeDetail'),
    path('update/<int:pk>', views.EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),
    path('delete/<int:pk>', views.EmployeeDelete.as_view(), name = 'EmployeeDelete') ,
    path('list/', views.EmployeeList.as_view(), name = 'EmployeeList'),
   
   
]