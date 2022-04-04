from django import forms

from employees.models import Employee

class Employee_modelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"