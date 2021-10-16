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

    path('triangle-law-of-cosines/', views.triangle_law_of_cosines, name='triangle_law_of_cosines'),
    path('triangle-law-of-sines/', views.triangle_law_of_sines, name='triangle_law_of_sines'),

    path('arctan/', views.arctan, name='arctan'),
    path('cofunction/', views.cofunction, name='cofunction'),

    path('cosecant/', views.cosecant , name='cosecant'),

    path('double-angle-formula/', views.double_angle_formula , name='double-angle-formula'),
    path('sum-of-linear-number-sequence/', views.sum_of_linear_number_sequence , name='sum-of-linear-number-sequence'),

    path('angle-between-two-vectors/', views.angle_between_two_vectors , name='angle-between-two-vectors'),
    path('gradient/', views.gradient , name='gradient'),

    path('parabola/', views.parabola , name='parabola'),

    path('parallel-line/', views.parallel_line , name='parallel-line'),
    path('linear-interpolation/', views.linear_interpolation , name='linear-interpolation'),
    path('midpoint/', views.midpoint , name='midpoint'),

    path('cartesian-to-polar/', views.cartesian_to_polar , name='cartesian-to-polar'),
    path('slope-intercept-form/', views.slope_intercept_form , name='slope-intercept-form'),

    path('dot-product/', views.dot_product , name='dot-product'),
    path('cross-product/', views.cross_product , name='cross-product'),

    path('spherical-coordinates/', views.spherical_coordinates, name='spherical-coordinates'),

    path('average-rate-of-change/', views.average_rate_of_change , name='average-rate-of-change'),

    path('cylindrical-coordinates/', views.cylindrical_coordinates , name='cylindrical-coordinates'),

    path('3d-distance/', views.distance_3d, name='3d-distance'),
    path('work-combine/', views.work_combine, name='work-combine'),

    path('hyperbola/', views.hyperbola, name='hyperbola'),

    path('parallel-resistor/',  views.parallel_resistor, name="parallel-resistor"),

    path('velocity-addition/', views.velocity_addition, name='velocity-addition'),
    path('spherical-capacitor/', views.spherical_capacitor, name='spherical-capacitor'),
    path('resonant-frequecy/', views.resonant_frequecy, name='resonant-frequecy'),

    path('quarter-mile/', views.quarter_mile, name='quarter-mile'),

    path('affine-cipher/', views.affine_cipher, name='affine-cipher'),

    path('find-both-numbers/', views.find_both_numbers, name='find-both-numbers'),
    path('cross-partition/', views.cross_partition, name='cross-partition'),

    path('markup/', views.markup, name='markup'),
    path('variation-eq/', views.variation_eq, name='variation-eq'),
    path('equivalent-annual-cost/', views.eq_annual_cost, name='equivalent-annual-cost'),

    path('power-with-displacement/', views.powerWithDisplacement, name='power-with-displacement'),
    path('moment-of-inertia/', views.momentOfInertia, name='moment-of-inertia'),
]
