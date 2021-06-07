from . import views
from django.urls import path, include

urlpatterns = [

    # path('', views.home, name='home'),
    path('factorial/', views.factorial, name='factorial'),
    path('combinations/', views.combinations, name='combinations'),
    path('permutations/', views.permutations, name='permutations'),

    path('even-permutations/', views.evenPermutaions, name='even-permutations'),
    path('odd-permutations/', views.oddPermutaions, name='odd-permutations'),

    path('combinations-replacement/', views.combinations_replacement, name='combinations-replacement'),
    path('permutations-replacement/', views.permutations_replacement, name='permutations-replacement'),

    # path('triangle-law-of-cosines/', views.triangle_law_of_cosines, name='triangle_law_of_cosines'),
]
