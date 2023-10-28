from django.db import models

# Create your models here.
class Employee(models.Model):
    Employee_iD= models.CharField(max_length=12)
    Name=models.CharField(max_length=10)
    Email=models.EmailField()
    Contact_Number = models.IntegerField()
    date_of_joining=models.DateField()
    Year_experience= models.IntegerField()
 
 
    def __str__(self):
        return self.Name


class Department(models.Model):
    Department_ID=models.CharField(max_length=12) 
    Department_name=models.CharField(max_length=13)
    Department_location=models.CharField(max_length=13)
    Manager_ID=models.ForeignKey('Employee',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.Name