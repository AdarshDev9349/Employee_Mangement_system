from .models import Employee
from django import forms


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Employee_iD','Name','Email','Contact_Number','date_of_joining','Year_experience']
    