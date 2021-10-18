from . import views
from django.urls import path, include

urlpatterns = [
   
    path('mass-to-energy/', views.mass_to_energy, name='mass-to-energy'),
    
]
