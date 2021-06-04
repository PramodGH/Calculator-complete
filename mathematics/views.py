from django.shortcuts import render, HttpResponse
from django.contrib import messages
import math
from .unitConverter import power_raise
from . import triangle_law_of_cosines_calculations as tlc


# factorial function :
def fact(n):
    if n == 0 or n < 0:
        output = "1"
        return 1, output
    result = 1
    output = " "
    for i in range(n, 0, -1):
        result *= i
        if i == 1:
            output = output + str(i)
        else:
            output = output + str(i) + "✕"
    # print("----loop output is: ", result)
    return result, output


# factorial calculator
def factorial(request):
    if request.method == 'POST':
        value = int(request.POST['value'])

        # if value < 0:
        #     messages.error(request, 'Please enter vaild data, n must be > or = to 0')
        #     return render(request, 'mathematics/factorial.html')

        power = ''
        result, output = fact(value)
        if result > 1000:
            result, power = power_raise(result)  # converting long output into powers of 10

        context = {
            'result': result,
            'power_of_result': power,
            'value': value,
            'output': output,
            'flag': True
        }
        return render(request, 'mathematics/factorial.html', context)
    else:
        return render(request, 'mathematics/factorial.html', {'flag': False})


# combination calculator
def combinations(request):
    if request.method == 'POST':
        n = int(request.POST['n'])
        r = int(request.POST['r'])

        print("n ---", n, type(n))
        print("r ---", r, type(r))
        # for wrong inputs
        if r > n:
            messages.error(request, '"n" should be > than or = "r"')
            return render(request, 'mathematics/combinations.html')
        # elif n < 0 or r < 0:
        #     messages.error(request, 'Please enter vaild data, values should be non-negative')
        #     return render(request, 'mathematics/combinations.html')

        result1, output1 = fact(n)
        result2, output2 = fact(r)

        result3, output3 = fact(n - r)
        # print("reult1-------------", result1)

        power = ''
        result = result1 // (result2 * result3)  # Final answer
        if result > 10000000:
            result, power = power_raise(result)

        power1, power2, power3 = '', '', ''
        if result1 > 10000000:
            result1, power1 = power_raise(result1)
            print("reult1-------------", result1)
        if result2 > 10000000:
            result2, power2 = power_raise(result2)
        if result3 > 10000000:
            result3, power3 = power_raise(result3)
        # print("reult3-------------", result3)

        context = {
            'result': result,
            'power': power, 'power1': power1, 'power2': power2, 'power3': power3,
            'result1': result1, 'result2': result2, 'result3': result3,
            # 'r1':r1, 'r2':r2, 'r3':r3,

            'output1': output1,  # output to show each factorial value and how it's evaluated
            'output2': output2,
            'output3': output3,

            'n': n,  # Input values
            'r': r,
            'flag': True

        }
        return render(request, 'mathematics/combinations.html', context)

    else:
        return render(request, 'mathematics/combinations.html', {'flag': False})


# combinations replacement
def combinations_replacement(request):
    if request.method == 'POST':
        n = int(request.POST['n'])
        r = int(request.POST['r'])

        # for wrong inputs
        if n < 0 or r < 0:
            messages.error(request, 'inputs must be > or = to 0')
            return render(request, 'mathematics/combinationsReplacement.html')
        elif n + r - 1 < r:
            messages.error(request, 'n+r-1 must be > or = to r')
            return render(request, 'mathematics/combinationsReplacement.html')

        # calculations
        result1, output1 = fact(n + r - 1)
        result2, output2 = fact(r)
        result3, output3 = fact(n - 1)

        # result = result1 / (result2 * result3)  # Final answer

        power = ''
        result = result1 / (result2 * result3)  # Final answer
        if result > 10000000:
            result, power = power_raise(result)

        power1, power2, power3 = '', '', ''
        if result1 > 10000000:
            result1, power1 = power_raise(result1)
        if result2 > 10000000:
            result2, power2 = power_raise(result2)
        if result3 > 10000000:
            result3, power3 = power_raise(result3)

        context = {
            'result': result,
            'power': power, 'power1': power1, 'power2': power2, 'power3': power3,
            'result1': result1, 'result2': result2, 'result3': result3,

            'output1': output1,  # output to show each factorial value and how it's evaluated
            'output2': output2,
            'output3': output3,

            'in1': int(n + r - 1),  # intermediate values int1 = (n+r-1)
            'in2': int(n - 1),

            'n': n,  # Input values
            'r': r,
            'flag': True
        }
        return render(request, 'mathematics/combinationsReplacement.html', context)

    else:
        return render(request, 'mathematics/combinationsReplacement.html', {'flag': False})


# permutations - Replacement
def permutations_replacement(request):
    if request.method == 'POST':
        n = int(request.POST['n'])
        r = int(request.POST['r'])

        # for wrong inputs
        if n < 0 or r < 0:
            messages.error(request, 'Please enter vaild data, inputs must be > or = to 0')
            return render(request, 'mathematics/permutationsReplacement.html')

        # calculations
        if n == 0:
            result = 0
        elif r == 0:
            result = 1
        else:
            result = math.pow(n, r)
        power = ''
        if result > 10000000:
            result, power = power_raise(result)

        context = {
            'result': result,
            'power': power,
            'n': n,  # Input values
            'r': r,
            'flag': True
        }
        return render(request, 'mathematics/permutationsReplacement.html', context)

    else:
        return render(request, 'mathematics/permutationsReplacement.html', {'flag': False})


# odd Permutations
def evenPermutaions(request):
    if request.method == 'POST':
        n = int(request.POST['n'])

        # for wrong inputs
        if n <= 2:
            messages.error(request, 'Please enter vaild data, n must be > 2')
            return render(request, 'mathematics/evenpermutations.html')

        # calculations
        result1, output1 = fact(n)

        power, power1 = '', ''
        result = result1 / 2  # Final answer
        if result > 1000000:
            result, power = power_raise(result)
        if result1 > 1000000:
            result1, power1 = power_raise(result1)

        context = {
            'result': result, 'power': power,
            'result1': result1, 'power1': power1,  # Intermediate results -> resul1, result2, result3

            'output1': output1,  # output to show each factorial value and how it's evaluated

            'n': n,  # Input values
            'flag': True
        }

        return render(request, 'mathematics/evenpermutations.html', context)
    else:
        return render(request, 'mathematics/evenpermutations.html', {'flag': False})


# odd permutaions
def oddPermutaions(request):
    if request.method == 'POST':
        n = int(request.POST['n'])

        # for wrong inputs
        if n < 2:
            messages.error(request, 'Please enter vaild data, n must be > or = 2.')
            return render(request, 'mathematics/oddpermutations.html')

        # calculations
        result1, output1 = fact(n)

        power, power1 = '', ''
        result = result1 / 2  # Final answer
        if result > 1000000:
            result, power = power_raise(result)
        if result1 > 1000000:
            result1, power1 = power_raise(result1)

        context = {
            'result': result, 'power1': power1,
            'result1': result1, 'power': power,  # Intermediate results -> resul1, result2, result3

            'output1': output1,  # output to show each factorial value and how it's evaluated

            'n': n,  # Input values
            'flag': True
        }

        return render(request, 'mathematics/oddpermutations.html', context)
    else:
        return render(request, 'mathematics/oddpermutations.html', {'flag': False})


# def triangle_law_of_cosines(request):
#     if request.method == "POST":
#         side_a = request.POST.get('side_a')  # sides from form
#         side_b = request.POST.get('side_b')
#         side_c = request.POST.get('side_c')
#
#         angle_a = request.POST.get('angle_a')
#         angle_b = request.POST.get('angle_b')  # angle from form
#         angle_c = request.POST.get('angle_c')
#
#         angle_unit = request.POST.get('angle_unit')
#         length_unit = request.POST.get('length_unit')
#         print("Entry in post method-------")
#         print(side_a, side_b, side_c)
#         given = request.POST['given']
#
#         if (given == "form1" or given == "form2" or given == "form3"):
#             side_a = float(request.POST.get('side_a')) # sides from form
#             side_b = float(request.POST.get('side_b'))
#             side_c = float(request.POST.get('side_c'))
#
#             given = request.POST['given']
#             angle_unit = request.POST.get('angle_unit')
#             length_unit = request.POST.get('length_unit')
#
#             if given == 'form1':
#                 result = tlc.calculate_angle_A(side_a, side_b, side_c)
#                 print("result of angle A----------", result)
#             elif given == 'form2':
#                 result = tlc.calculate_angle_B(side_a, side_b, side_c)
#                 print("result of angle B----------", result)
#             elif given == 'form3':
#                 result = tlc.calculate_angle_C(side_a, side_b, side_c)
#                 print("result of angle C----------", result)
#
#             context = {
#                 'result': result,
#                 'side_a': side_a,
#                 'side_b': side_b,
#                 'side_c': side_c,
#                 'given': given,
#                 'flag1': True
#             }
#             return render(request, 'mathematics/triangleLawOfCosines.html', context)
#
#     else:
#         return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form1'})
