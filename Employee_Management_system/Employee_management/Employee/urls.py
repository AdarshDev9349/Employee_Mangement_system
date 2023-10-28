
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewset,Departmentviewset
from . import views
router=DefaultRouter()
router.register(r'employees',EmployeeViewset)
router.register(r'department',Departmentviewset)
urlpatterns = [
    
    path('',include(router.urls)),
   
  
    
]
