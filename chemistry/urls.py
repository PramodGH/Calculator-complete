from . import views
from django.urls import path, include

urlpatterns = [
    # path('atomic-mass/', views.atomic_mass, name='atomic_mass'),
    path('neutralization/', views.neutralization, name='neutralization'),
    # path('', views.home, name='home'),
    # path('factorial/', views.factorial, name='factorial'),
]
