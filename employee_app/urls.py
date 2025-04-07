from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    
    # 👇 Create route with BOTH names for backward compatibility
    path('create/', views.employee_create, name='employee_create'),
    path('create/', views.employee_create, name='add_employee'),  # <== This fixes your template error

    path('update/<int:id>/', views.employee_update, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
]
