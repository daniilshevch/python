from django.urls import path
from . import views

urlpatterns = [
    path('passenger_carriages/', views.passenger_carriage_list, name='passenger_carriage_list'),
    path('passenger_carriages/<int:pk>/', views.passenger_carriage_detail, name='passenger_carriage_detail'),
    path('passenger_carriages/add/', views.passenger_carriage_add, name='passenger_carriage_add'),
    path('passenger_carriages/<int:pk>/edit/', views.passenger_carriage_edit, name='passenger_carriage_edit'),
]
