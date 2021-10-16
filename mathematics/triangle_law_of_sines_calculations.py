from math import pow, acos, cos, sqrt, pi, asin, sin

def calculate_angle(s1, a, s2):
    result = asin((s1*sin(a))/s2)
    return result

