from math import pow, acos

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