from django.shortcuts import render,redirect,HttpResponse
from rest_framework import viewsets
from .models import Employee,Department
from .serializers import EmployeeSerializers,DepartmentSerializers
from .forms import EmployeeForm
# Create your views here.


class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class Departmentviewset(viewsets.ModelViewSet):
      queryset=Department.objects.all()
      serializer_class=DepartmentSerializers
def add_emp(request):
    form=EmployeeForm(request.POST or None)
    if form.is_valid():
	        form.save()                
    context = {
		        "form": form,
		         "title": "Name",
	    }
    return render(request,'Add_Emp.html',context)    
    
def all_emp(request):
      Emp=Employee.objects.all()
      context={
            'Emp':Emp
      }
      print(context)
      return render(request,'All_Emp.html',context)
      


def rem_emp(request,em_id=0):
      if em_id:
         try:
             
             em_remove =Employee.objects.get(id=em_id)
             em_remove.delete()
             return HttpResponse("Student removed successfully" )
             
         except:
             return HttpResponse("please enter a valid id")
              
      
      
      
      
      
      
      
      Emp= Employee.objects.all()
      context = {
           'Emp':Emp

    }
      

      return render(request,"Rem_Emp.html",context)
def Dash(request):
    return render(request,'Dash.html')