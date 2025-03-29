from django.shortcuts import render # type: ignore
from django.http import HttpResponse  # type: ignore



def index(request):     
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 
   
# Create your views here.


def drinks(request, drink_name):
    drinks_map = {
        "moca": "type of coffee",
        "tea": "type of beverage",
        "lemonade": "type of refreshment",
    }
    choice_of_drink = drinks_map.get(drink_name, "Drink not found")
    return render(request, 'coffee_types.html', {'choice_of_drink': choice_of_drink, 'drink_name': drink_name})