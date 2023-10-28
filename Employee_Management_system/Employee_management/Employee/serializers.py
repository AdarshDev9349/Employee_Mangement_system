from rest_framework import serializers
from .models import Employee,Department

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
         model=Department
         fields='__all__'