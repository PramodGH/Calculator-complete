from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.atomic_mass, name='atomic-mass'),
]
