from math import pow, acos, cos, sqrt

def calculate_angle_A(a, b, c):
    m = (pow(b,2)+pow(c,2)-pow(a,2))/(2*b*c)
    result = acos(m)
    return result

def calculate_angle_B(a, b, c):
    m = (pow(a,2)+pow(c,2)-pow(b,2))/(2*a*c)
    result = acos(m)
    return result

def calculate_angle_C(a, b, c):
    m = (pow(a,2)+pow(b,2)-pow(c,2))/(2*a*b)
    result = acos(m)
    return result

def calculate_side_a(b, A, c):
    a = sqrt(b**2 + c**2 + 2*b*c*cos(A))
    return a

def calculate_side_b(a, B, c):
    a = sqrt(a**2 + c**2 + 2*a*c*cos(B))
    return b

def calculate_side_c(a, C, b):
    a = sqrt(a**2 + b**2 + 2*a*b*cos(C))
    return c
