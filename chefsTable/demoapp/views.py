from django.shortcuts import render # type: ignore
from django.http import HttpResponse  # type: ignore
from demoapp.forms import InputForms  # type: ignore
from demoapp.forms import LoggerForm  # type: ignore
from demoapp.models import Drinks, DrinksCategory, Employee  # Ensure you have a MenuItem model in your app
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


def index(request):     
    return render(request, 'home.html')
   
# Create your views here.

def modelForm_view(request):
    form = LoggerForm()
    context = {'form': form}

    if request.method == 'POST':
        # Handle form submission
        form = LoggerForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
        return HttpResponse(f"Form submitted successfully!")

    return render(request, 'form.html', context)


def drinks(request, drink_name):

    drinks_map = {
        "moca": "type of coffee",
        "tea": "type of beverage",
        "lemonade": "type of refreshment",
    }
    choice_of_drink = drinks_map.get(drink_name, "Drink not found")
    return render(request, 'coffee_types.html', {'choice_of_drink': choice_of_drink, 'drink_name': drink_name})
    

def form_view(request):
    form  = InputForms()
    context = {'form': form}

    if request.method == 'POST':
        # Handle form submission
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        shift = request.POST.get('shift')
        time_logged = request.POST.get('time_logged')

        # Process the data as needed
        # For example, you can save it to the database or perform other actions

        return HttpResponse(f"Form submitted successfully! First Name: {first_name}, Last Name: {last_name}, Shift: {shift}, Time Logged: {time_logged}")

    return render(request, 'form.html', context)

def menu(request):  
    categories = DrinksCategory.objects.all()   

    menu = {
        category.category: list(Drinks.objects.filter(category_id=category))
        for category in categories
    }  
    context = {'categories': categories ,'menu': menu, 'title': 'Menu'}     
   
    return render(request, 'menu.html', context)

def about(request):
    return render(request, 'demoapp/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'contact.html', {'title': 'Contact Us'})

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

class EmployeeCreate(CreateView):   
    model = Employee   
    fields = '__all__' 
   
    success_url = "/employees/success/"
class EmployeeList(ListView):   
    model = Employee
    success_url = "/employees/success/"

class EmployeeUpdate(UpdateView):   
    model = Employee
    fields = '__all__'   
    success_url = "/employees/success/" 
class EmployeeDetail(DetailView):   
    model = Employee
    fields = '__all__'   
    success_url = "/employees/success/" 

class EmployeeDelete(DeleteView):   
    model = Employee  
    success_url = "/employees/success/"  