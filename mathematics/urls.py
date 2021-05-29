from . import views
from django.urls import path, include

urlpatterns = [

    # path('', views.home, name='home'),
    path('factorial/', views.factorial, name='factorial'),
    path('combination/', views.combination, name='combination'),
]
