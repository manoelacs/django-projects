from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User 

from .models import  DrinksCategory, Drinks, Employee, Logger, Person 
# Unregister the provided model admin:  

admin.site.register(DrinksCategory)
admin.site.register(Drinks)
admin.site.register(Logger)

admin.site.register(Employee) 


admin.site.unregister(User) 
@admin.register(User) 
class NewAdmin(UserAdmin): 
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form 

@admin.register(Person) 
class PersonAdmin(admin.ModelAdmin): 
    list_display = ("last_name", "first_name") 
    search_fields = ("first_name__startswith", ) 