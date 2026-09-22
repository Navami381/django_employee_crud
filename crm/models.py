from django.db import models
#Employee(id,name,department,salary,location,email)

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()
    location=models.CharField(max_length=200)
    email=models.EmailField(unique=True)

#then make it as query file and then execute
#python manage.py makemigrations
#python manage.py migrate