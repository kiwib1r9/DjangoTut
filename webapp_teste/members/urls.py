from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('teste/', views.teste, name='teste'),
    path('members/details/<int:id>', views.details, name='details'),
]