from django.urls import path
from employees.views import EmployeeDetailView
from employees.views import EmployeeListView


urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('employees/<slug:pk>',
         EmployeeDetailView.as_view(), name='employee-detail-view'),
]
