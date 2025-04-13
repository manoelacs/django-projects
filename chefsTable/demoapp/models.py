from django.db import models

# Create your models here.

class DrinksCategory(models.Model):
    category = models.CharField(max_length=200)

class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, null=True, blank=True)

class Logger(models.Model):     
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    log_time = models.DateTimeField('date logged')

class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField() 

    def __str__(self): 
        return f"{self.last_name}, {self.first_name}" 
    
""" class Employee(models.Model): 
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self): 
        return f"{self.last_name}, {self.first_name} - {self.role}" """

""" class Employee(models.Model):   
    name = models.CharField(max_length=100)   
    email = models.EmailField()   
    contact = models.CharField(max_length=15, null=True)
    class Meta:   
        db_table = "Employee"  """