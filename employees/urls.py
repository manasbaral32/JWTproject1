from django.urls import path
from employees import views


urlpatterns = [
    path('', views.EmployeeListView.as_view(), name = "employees"),
    path('<int:pk>/detail/', views.EmployeeDetailsView.as_view(), name = "employee_detail"),
    path('create', views.EmployeeCreateView.as_view(), name = "employee_create"),
    path('<int:pk>/update/',views.EmployeeUpdateView.as_view(), name="employee_update"),
    path('<int:pk>/delete/',views.EmployeeDeleteView.as_view(), name="employee_delete"),
]