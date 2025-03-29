from django.urls import path
from . import views

urlpatterns = [
    path('get-holidays', views.get_holidays, name='get_holidays'),
    path('', views.chose_country, name='chose_country'),
]