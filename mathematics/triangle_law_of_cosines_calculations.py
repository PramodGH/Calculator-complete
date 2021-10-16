from math import pow, acos, cos, sqrt, pi

def calculate_angle_A(a, b, c):
    m = (pow(b,2)+pow(c,2)-pow(a,2))/(2*b*c)
    print(" mid value of result=----------",m)
    result = acos(m)
    print(" Last value  of result=----------", result)
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
    a = sqrt(pow(b,2) + pow(c,2) - 2*b*c*cos(A))
    print("a-----------",a)
    return a

def calculate_side_b(a, B, c):
    b = sqrt(pow(a,2) + pow(c,2) - 2*a*c*cos(B))
    return b

def calculate_side_c(a, C, b):
    c = sqrt(pow(a,2) + pow(b,2) - 2*a*b*cos(C))
    return c

# def convert_to_degree(value):
#     return value * (180/pi)
