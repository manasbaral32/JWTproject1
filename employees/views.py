from django.shortcuts import render

# Create your views here.
from employees.models import Employee
from employees.forms import Employee_modelForm


from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employee_list'


class EmployeeDetailsView(DetailView):
    model = Employee
    template_name = 'employees/employee_details.html'
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = "__all__"
    # template_name = "employees/employee_form.html"
    # context_object_name = "form"

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = "__all__"
    # template_name = "employees/employee_form.html"
    # context_object_name = "form"


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/employee/'
    fields = "__all__"
    template_name = "employees/employee_confirm_delete.html"
    context_object_name = "employee"