from django.shortcuts import render, HttpResponse
from django.contrib import messages
import math
from math import pi
from .unitConverter import power_raise
from . import triangle_law_of_cosines_calculations as tlc
from . import triangle_law_of_sines_calculations as tls

from .unit import Unit, Type


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

        # print("n ---", n, type(n))
        # print("r ---", r, type(r))

        # for wrong inputs
        if r > n:
            messages.error(request, 'n should be > than or = r')
            return render(request, 'mathematics/combinations.html')

        result1, output1 = fact(n)
        result2, output2 = fact(r)
        result3, output3 = fact(n - r)

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

        context = {
            'result': result,
            'power': power, 'power1': power1, 'power2': power2, 'power3': power3,
            'result1': result1, 'result2': result2, 'result3': result3,

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


# permutations
def permutations(request):
    if request.method == 'POST':
        n = int(request.POST['n'])
        r = int(request.POST['r'])

        # for wrong inputs
        if r > n:
            messages.error(request, 'n should be > than or = r')
            return render(request, 'mathematics/permutations.html')

        result1, output1 = fact(n)
        result3, output3 = fact(n - r)

        power = ''
        result = result1 / result3  # Final answer
        if result > 10000000:
            result, power = power_raise(result)

        power1, power3 = '', ''
        if result1 > 10000000:
            result1, power1 = power_raise(result1)

        if result3 > 10000000:
            result3, power3 = power_raise(result3)

        context = {
            'result': result,
            'power': power, 'power1': power1, 'power3': power3,
            'result1': result1, 'result3': result3,

            'output1': output1,  # output to show each factorial value and how it's evaluated
            'output3': output3,

            'n': n,  # Input values
            'r': r,
            'flag': True

        }
        return render(request, 'mathematics/permutations.html', context)
    else:
        return render(request, 'mathematics/permutations.html')


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
        return render(request, 'mathematics/permutationsReplacement.html')


# even Permutations
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


def triangle_law_of_cosines(request):
    if request.method == "POST":
        side_a = request.POST.get('side_a')  # sides from form
        side_b = request.POST.get('side_b')
        side_c = request.POST.get('side_c')

        angle_a = request.POST.get('angle_a')
        angle_b = request.POST.get('angle_b')  # angle from form
        angle_c = request.POST.get('angle_c')

        angle_unit = request.POST.get('angle_unit')
        length_unit = request.POST.get('length_unit')
        significant_figures = int(request.POST.get('significant_figures'))

        given = request.POST['given']
        # print('which form request--------',given)

        # Form1, form2 , form3
        if (given == "form1" or given == "form2" or given == "form3") and side_a and side_b and side_c:
            if '.' in side_a:
                side_a = float(request.POST['side_a'])
            else:
                side_a = int(request.POST['side_a'])
            if '.' in side_b:
                side_b = float(request.POST['side_b'])
            else:
                side_b = int(request.POST['side_b'])
            if '.' in side_c:
                side_c = float(request.POST['side_c'])
            else:
                side_c = int(request.POST['side_c'])
            # print('entered in form1, 2, 3------', side_a, side_b, side_c)
            # given = request.POST['given']
            # angle_unit = request.POST.get('angle_unit')
            # length_unit = request.POST.get('length_unit')

            # Error check
            if side_a >= (side_b + side_c) or side_b >= (side_a + side_c) or side_c >= (side_a + side_b):
                messages.error(request, '1 side is too long to form a closed regular triangle!')
                context = {
                    'given': given, 'side_a': side_a, 'side_b': side_b, 'side_c': side_c,
                }
                return render(request, 'mathematics/triangleLawOfCosines.html', context)

            result = None
            if given == 'form1':
                result = tlc.calculate_angle_A(side_a, side_b, side_c)

            elif given == 'form2':
                result = tlc.calculate_angle_B(side_a, side_b, side_c)

            elif given == 'form3':
                result = tlc.calculate_angle_C(side_a, side_b, side_c)

            if angle_unit == 'degree':
                result = math.degrees(result)

            result = round(result, significant_figures)

            context = {
                'result': result,
                'side_a': side_a,
                'side_b': side_b,
                'side_c': side_c,
                'angle_unit': angle_unit,
                'given': given,
                'length_unit': length_unit,
                'significant_figures': significant_figures,
                'flag123': True
            }
            print('before context send-------given', given)
            return render(request, 'mathematics/triangleLawOfCosines.html', context)

        # form4
        elif given == "form4" and angle_a and side_b and side_c:
            if '.' in side_b:
                side_b = float(request.POST['side_b'])
            else:
                side_b = int(request.POST['side_b'])

            if '.' in side_c:
                side_c = float(request.POST['side_c'])
            else:
                side_c = int(request.POST['side_c'])

            if '.' in angle_a:
                angle_a = float(request.POST['angle_a'])
            else:
                angle_a = int(request.POST['angle_a'])

            # print("ange a, and angl unit -----",angle_a, angle_unit)

            # Error check
            if angle_unit == 'degree':
                if angle_a == 0:
                    messages.error(request, "Enter value greater than 0")
                    return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form4'})
                elif angle_a >= 180:
                    messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
                    return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form4'})
            elif angle_unit == 'radian':
                if angle_a == 0:
                    messages.error(request, "Enter value greater than 0")
                    return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form4'})
                elif angle_a >= pi:
                    messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
                    return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form4'})

            result = None
            if angle_unit == 'degree':
                angle_A = math.radians(angle_a)
                result = tlc.calculate_side_a(side_b, angle_A, side_c)
                # print("walked inside degree------", result)
            else:
                result = tlc.calculate_side_a(side_b, angle_a, side_c)
                # print("walked inside radians-------", result)

            result = round(result, significant_figures)
            context = {
                'result': result,
                'side_b': side_b,
                'side_c': side_c,
                'angle_a': angle_a,
                'given': given,
                'angle_unit': angle_unit,
                'length_unit': length_unit,
                'significant_figures': significant_figures,
                'flag4': True
            }
            return render(request, 'mathematics/triangleLawOfCosines.html', context)

        # form5
        elif given == "form5" and angle_b and side_a and side_c:
            if '.' in side_a:
                side_a = float(request.POST['side_a'])
            else:
                side_a = int(request.POST['side_a'])

            if '.' in side_c:
                side_c = float(request.POST['side_c'])
            else:
                side_c = int(request.POST['side_c'])

            if '.' in angle_b:
                angle_b = float(request.POST['angle_b'])
            else:
                angle_b = int(request.POST['angle_b'])

            # Error check
            if angle_unit == 'degree':
                if angle_b == 0:
                    messages.error(request, "Enter value greater than 0")
                    return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form5'})
                elif angle_b >= 180:
                    messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
                    return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form5'})
            elif angle_unit == 'radian':
                if angle_b == 0:
                    messages.error(request, "Enter value greater than 0")
                    return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form5'})
                elif angle_b >= pi:
                    messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
                    return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form5'})

            # print("Inside form5->>>>>")
            result = None
            if angle_unit == 'degree':
                angle_B = math.radians(angle_b)
                result = tlc.calculate_side_b(side_a, angle_B, side_c)
                # print("walked inside degree------", result)
            else:
                result = tlc.calculate_side_a(side_b, angle_b, side_c)
                # print("walked inside radians-------", result)

            result = round(result, significant_figures)
            # print("Inside form5->>>>Result>",result)

            context = {
                'result': result,
                'side_a': side_a,
                'side_c': side_c,
                'angle_b': angle_b,
                'given': given,
                'angle_unit': angle_unit,
                'length_unit': length_unit,
                'significant_figures': significant_figures,
                'flag5': True
            }
            # print("Inside form5->>Before context render >>>")
            return render(request, 'mathematics/triangleLawOfCosines.html', context)

        # form6 :
        elif given == "form6" and angle_c and side_a and side_b:
            if '.' in side_a:
                side_a = float(request.POST['side_a'])
            else:
                side_a = int(request.POST['side_a'])

            if '.' in side_b:
                side_b = float(request.POST['side_b'])
            else:
                side_b = int(request.POST['side_b'])

            if '.' in angle_c:
                angle_c = float(request.POST['angle_c'])
            else:
                angle_c = int(request.POST['angle_c'])

                # Error check
            if angle_unit == 'degree':
                if angle_c == 0:
                    messages.error(request, "Enter value greater than 0")
                    return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form6'})
                elif angle_c >= 180:
                    messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
                    return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form6'})
            elif angle_unit == 'radian':
                if angle_c == 0:
                    messages.error(request, "Enter value greater than 0")
                    return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form6'})
                elif angle_c >= pi:
                    messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
                    return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form6'})

            result = None
            if angle_unit == 'degree':
                angle_C = math.radians(angle_c)
                result = tlc.calculate_side_b(side_a, angle_C, side_c)
                print("walked inside degrees------", result)
            else:
                result = tlc.calculate_side_c(side_a, angle_c, side_b)
                print("walked inside radians-------", result)

            result = round(result, significant_figures)

            context = {
                'result': result,
                'side_a': side_a,
                'side_b': side_b,
                'angle_c': angle_c,
                'given': given,
                'angle_unit': angle_unit,
                'length_unit': length_unit,
                'significant_figures': significant_figures,
                'flag6': True
            }
            return render(request, 'mathematics/triangleLawOfCosines.html', context)
        return render(request, 'mathematics/triangleLawOfCosines.html', {'given': given})
    else:
        print("hit get  request---------------")
        return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form1'})


def triangle_law_of_sines(request):
    if request.method == "POST":
        a = request.POST.get('side_a')  # sides from form
        b = request.POST.get('side_b')
        c = request.POST.get('side_c')

        A = request.POST.get('angle_a')
        B = request.POST.get('angle_b')  # angle from form
        C = request.POST.get('angle_c')

        angle_unit = request.POST.get('angle_unit')
        length_unit = request.POST.get('length_unit')
        significant_figures = int(request.POST.get('significant_figures'))

        given = request.POST['given']

        # and side_a and side_b and side_c
        if given == "form1":
            a = float(request.POST['side_a'])  # sides from form
            B = float(request.POST['angle_b'])
            b = float(request.POST['side_b'])

            # Error check
            # if side_a >= (side_b + side_c) or side_b >= (side_a + side_c) or side_c >= (side_a + side_b):
            #     messages.error(request, '1 side is too long to form a closed regular triangle!')
            #     context = {
            #         'given':given, 'side_a':side_a, 'side_b':side_b, 'side_c':side_c,
            #     }
            #     return render(request, 'mathematics/triangleLawOfCosines.html', context)

            result = None
            if given == 'form1':
                print("check befor entrting fun ")
                checkError(request, angle_unit, a, B, b, 'a', 'B', 'b', given)

                if angle_unit == 'degree':
                    angle_B = math.radians(B)
                    result = tls.calculate_angle(a, angle_B, b)
                else:
                    result = tls.calculate_angle(a, B, b)

                result = round(result, significant_figures)
                context = {
                    'result': result,
                    'side_a': a,
                    'angle_b': B,
                    'side_b': b,
                    'angle_unit': angle_unit,
                    'given': given,
                    'length_unit': length_unit,
                    'significant_figures': significant_figures,
                    'flag1': True
                }
                return render(request, 'mathematics/triangleLawOfSines.html', context)

        #     elif given == 'form2':
        #         print('in form2-------------')
        #         result = tlc.calculate_angle_B(side_a, side_b, side_c)
        #
        #     elif given == 'form3':
        #         print('in forrm3------------')
        #         result = tlc.calculate_angle_C(side_a, side_b, side_c)
        #
        #
        #
        #     if angle_unit == 'degree':
        #         result = math.degrees(result)
        #
        #
        #     result = round(result, significant_figures)
        #
        #     context = {
        #         'result': result,
        #         'side_a': side_a,
        #         'side_b': side_b,
        #         'side_c': side_c,
        #         'angle_unit':angle_unit,
        #         'given': given,
        #         'length_unit':length_unit,
        #         'significant_figures':significant_figures,
        #         'flag123': True
        #     }
        #     print('before context send-------given', given)
        #     return render(request, 'mathematics/triangleLawOfCosines.html', context)
        #
        # # and angle_a and side_b and side_c:
        # elif given == "form4" and angle_a and side_b and side_c:
        #     side_b = float(request.POST['side_b'])
        #     side_c = float(request.POST['side_c'])
        #
        #     angle_a = float(request.POST['angle_a'])
        #     print("ange a, and angl unit -----",angle_a, angle_unit)
        #     # Error check
        #     if angle_unit == 'degree':
        #         if angle_a == 0:
        #             messages.error(request, "Enter value greater than 0")
        #             return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form4'})
        #         elif angle_a >= 180:
        #             messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
        #             return render(request, 'mathematics/triangleLawOfCosines.html',{'given':'form4'})
        #     elif angle_unit == 'radian':
        #         if angle_a == 0:
        #             messages.error(request, "Enter value greater than 0")
        #             return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form4'})
        #         elif angle_a >= pi:
        #             messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
        #             return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form4'})
        #
        #
        #     result = None
        #     if angle_unit == 'degree':
        #         angle_A = math.radians(angle_a)
        #         result = tlc.calculate_side_a(side_b, angle_A, side_c)
        #         print("walked inside degree------", result)
        #     else:
        #         result = tlc.calculate_side_a(side_b, angle_a, side_c)
        #         print("walked inside radians-------", result)
        #
        #
        #     # radian to degree convertor
        #     # if angle_unit == 'degree':
        #     #     result = math.degrees(result)
        #     #     print("inside convert to degree------",result)
        #     result = round(result, significant_figures)
        #
        #     context = {
        #         'result': result,
        #         'side_b': side_b,
        #         'side_c': side_c,
        #         'angle_a':angle_a,
        #         'given': given,
        #         'angle_unit': angle_unit,
        #         'length_unit': length_unit,
        #         'significant_figures': significant_figures,
        #         'flag4': True
        #     }
        #     return render(request, 'mathematics/triangleLawOfCosines.html', context)
        #
        # # and angle_b and side_a and side_c
        # elif given == "form5" and angle_b and side_a and side_c:
        #
        #     side_a = float(request.POST['side_a'])  # sides from form
        #     side_c = float(request.POST['side_c'])
        #     angle_b = float(request.POST['angle_b'])  # angle from form
        #
        #     # Error check
        #     if angle_unit == 'degree':
        #         if angle_b == 0:
        #             messages.error(request, "Enter value greater than 0")
        #             return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form5'})
        #         elif angle_b >= 180:
        #             messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
        #             return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form5'})
        #     elif angle_unit == 'radian':
        #         if angle_b == 0:
        #             messages.error(request, "Enter value greater than 0")
        #             return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form5'})
        #         elif angle_b >= pi:
        #             messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
        #             return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form5'})
        #
        #     print("Inside form5->>>>>")
        #     result = None
        #     if angle_unit == 'degree':
        #         angle_B = math.radians(angle_b)
        #         result = tlc.calculate_side_b(side_a, angle_B, side_c)
        #         print("walked inside degree------", result)
        #     else:
        #         result = tlc.calculate_side_a(side_b, angle_b, side_c)
        #         print("walked inside radians-------", result)
        #
        #     #
        #     # result = tlc.calculate_side_b(side_a, angle_b, side_c)
        #     #
        #     # if angle_unit == 'degrees':
        #     #     result = tlc.convert_to_degree(result)
        #     result = round(result, significant_figures)
        #     print("Inside form5->>>>Result>",result)
        #
        #     context = {
        #         'result': result,
        #         'side_a': side_a,
        #         'side_c': side_c,
        #         'angle_b': angle_b,
        #         'given': given,
        #         'angle_unit': angle_unit,
        #         'length_unit': length_unit,
        #         'significant_figures': significant_figures,
        #         'flag5': True
        #     }
        #     print("Inside form5->>Before context render >>>")
        #     return render(request, 'mathematics/triangleLawOfCosines.html', context)
        #
        # # and angle_c and side_a and side_b:
        # elif given == "form6" and angle_c and side_a and side_b:
        #
        #     side_a = float(request.POST['side_a'])  # sides from form
        #     side_b = float(request.POST['side_b'])
        #     angle_c = float(request.POST['angle_c'])  # angle from form
        #
        #     # Error check
        #     if angle_unit == 'degree':
        #         if angle_c == 0:
        #             messages.error(request, "Enter value greater than 0")
        #             return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form6'})
        #         elif angle_c >= 180:
        #             messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
        #             return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form6'})
        #     elif angle_unit == 'radian':
        #         if angle_c == 0:
        #             messages.error(request, "Enter value greater than 0")
        #             return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form6'})
        #         elif angle_c >= pi:
        #             messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
        #             return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form6'})
        #
        #
        #
        #     result = None
        #     if angle_unit == 'degree':
        #         angle_C = math.radians(angle_c)
        #         result = tlc.calculate_side_b(side_a, angle_C, side_c)
        #         print("walked inside degrees------", result)
        #     else:
        #         result = tlc.calculate_side_c(side_a, angle_c, side_b)
        #         print("walked inside radians-------", result)
        #
        #     # result = tlc.calculate_side_c(side_a, angle_c, side_b)
        #     #
        #     # if angle_unit == 'degrees':
        #     #     result = tlc.convert_to_degree(result)
        #
        #     result = round(result, significant_figures)
        #
        #     context = {
        #         'result': result,
        #         'side_a': side_a,
        #         'side_b': side_b,
        #         'angle_c': angle_c,
        #         'given': given,
        #         'angle_unit': angle_unit,
        #         'length_unit': length_unit,
        #         'significant_figures': significant_figures,
        #         'flag6': True
        #     }
        #     return render(request, 'mathematics/triangleLawOfCosines.html', context)
        return render(request, 'mathematics/triangleLawOfSines.html', {'given': given})
    else:
        print("hit get  request---------------")
        return render(request, 'mathematics/triangleLawOfSines.html', {'given': 'form1'})


def checkError(request, angle_unit, s1, angle, s2, s1_name, a_name, s2_name, given):
    # print(" entry in fun")
    if angle_unit == 'degree':
        if angle == 0:
            messages.error(request, "Enter value greater than 0")
            return render(request, 'mathematics/triangleLawOfSines.html', {'given': given})
        elif angle >= 180:
            messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
            return render(request, 'mathematics/triangleLawOfSsines.html', {'given': given})
        elif angle >= 90 and s2 <= s1:
            messages.error(request,
                           f'For ASS (SSA) theorem with {a_name} ≥ 90° ({a_name} ≥ π/2) and {s2_name} ≤ {s1_name}, there are no solutions and no triangle!')

    elif angle_unit == 'radian':
        if angle == 0:
            messages.error(request, "Enter value greater than 0")
            return render(request, 'mathematics/triangleLawOfSsines.html', {'given': given})
        elif angle >= pi:
            messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
            return render(request, 'mathematics/triangleLawOfSines.html', {'given': given})
        elif angle >= pi and s2 <= s1:
            messages.error(request,
                           f'For ASS (SSA) theorem with {a_name} ≥ 90° ({a_name} ≥ π/2) and {s2_name} ≤ {s1_name}, there are no solutions and no triangle!')


def arctan(request):
    def convert_to_radian(value, unit):
        if unit == 'deg':
            value = value * 0.0174533
        elif unit == 'gon':
            value = value * 0.015708
        elif unit == 'mrad':
            value = value * 0.001
        elif unit == 'μrad':
            value = value * 0.000001
        elif unit == 'arcmin':
            value = value * 0.000290888
        elif unit == 'arcsec':
            value = value * 0.0000048501
        elif unit == 'tr':
            value = value * 6.28319
        return value

    def convert_radian_to_other(valueinradian):
        all_conversions_string = {
            "value in degree": str(round((valueinradian * 57.2958), 5)) + " deg",
            "value in radian": str(valueinradian) + " rad",
            "value in gradians": str(round((valueinradian * 63.662), 5)) + " gon",
            "value in turns": str(round((valueinradian * 0.159155), 5)) + " tr",
            "value in arcmin": str(round((valueinradian * 3437.75), 5)) + " arcmin",
            "value in arcsec": str(round((valueinradian * 206265), 5)) + " arcsec",
            "value in mrad": str(round((valueinradian * 1000), 5)) + " mrad",
            "value in microrad": str(round((valueinradian * 1000000), 5)) + " μrad"
        }
        return all_conversions_string

    if request.method == "POST":
        x = request.POST.get('x')
        y = request.POST.get('y')
        y_op = request.POST.get('y_op')
        given = request.POST.get('given')

        if given == 'form1' and x:  # checking whether input value is float or int
            x = request.POST.get('x')
            if '.' in x:
                x = float(x)
            else:
                x = int(x)

            result = round(math.atan(x), 4)

            all_conversions = convert_radian_to_other(result)  # converting radian answer to all other values

            context = {
                'result': result,
                'x': x,
                'y_op': y_op,
                'given': given,
                'flag1': True,
                'all_conversions': all_conversions
            }

            return render(request, 'mathematics/arctan.html', context)

        elif given == 'form2' and y:
            y = request.POST.get('y')
            if '.' in y:
                y = float(y)
            else:
                y = int(y)

            # Error Check
            msg = 'Inverse tangent ranges from -π/2 to π/2 radians exclusively'
            if (y_op == "deg" and (y > 90 or y < -90)) or \
                    (y_op == "rad" and (y > 1.5708 or y < -1.5708)) or \
                    (y_op == "gon" and (y > 100 or y < -100)) or \
                    (y_op == "mrad" and (y > 1570.8 or y < -1570.8)) or \
                    (y_op == "arcmin" and (y > 5400 or y < -5400)) or \
                    (y_op == "arcsec" and (y > 324000 or y < -324000)) or \
                    (y_op == "μrad" and (y > 1570796.32679487 or y < -1570796.32679487)) or \
                    (y_op == "tr" and (y > 0.25 or y < -0.25)):
                messages.error(request, msg)
                return render(request, 'mathematics/arctan.html', {'given': given, 'flag1': False})

            temp = convert_to_radian(y, y_op)
            result = round(math.tan(temp), 6)

            context = {
                'result': result,
                'y': y,
                'y_op': y_op,
                'given': given,
                'flag2': True
            }
            return render(request, 'mathematics/arctan.html', context)
        return render(request, 'mathematics/arctan.html', {'given': given, 'flag1': False})

    else:
        return render(request, 'mathematics/arctan.html', {'given': 'form1', 'flag1': False})


def cofunction(request):
    def convert_to_radian(value, unit):
        if unit == 'deg':
            value = value * 0.0174533
        return value

    if request.method == 'POST':
        function = request.POST.get('function')
        angle = request.POST.get('angle')
        angle_op = request.POST.get('angle_op')

        if '.' in angle:
            angle = float(angle)
        else:
            angle = int(angle)

        # Error check
        if (angle_op == 'deg' and (angle < 0 or angle > 90)) or (
                angle_op == 'rad' and (angle < 0 or angle > math.pi / 2)):
            messages.error(request,
                           'For the cofunction identities, the angle has to be between 0 and 90 degrees (or 0 and π/2 in radians).')
            return render(request, 'mathematics/cofunction.html',
                          {'function': function, 'angle': angle, 'angle_op': angle_op, 'flag': False})

        pi_div_2_value = math.pi / 2
        x = convert_to_radian(angle, angle_op)

        if angle_op == 'deg':
            op = 90
            eval = 90 - angle
            eval_str = '90 ' + '- ' + str(angle)
        else:
            op = round(pi_div_2_value, 5)
            eval = pi_div_2_value - x
            eval_str = str(pi_div_2_value) + " - " + str(x)

        result = None
        if function == 'sin':
            result = math.sin(x)
        elif function == 'cos':
            result = math.cos(x)
        elif function == 'tan':
            result = math.tan(x)
        elif function == 'cot':
            result = 1 / math.tan(x)
        elif function == 'sec':
            result = 1 / math.cos(x)
        elif function == 'csc':
            result = 1 / math.sin(x)
        result = round(result, 6)

        print("result----------------", result)
        context = {
            'result': result,
            'op': op,
            'eval': eval,
            'eval_str': eval_str,
            'angle': angle,
            'angle_op': angle_op,
            'function': function,
            'flag': True,
        }
        return render(request, 'mathematics/cofunction.html', context)

    else:
        return render(request, 'mathematics/cofunction.html', {'function': 'sin(x)', 'angle': 'deg', 'flag': False})


def cosecant(request):
    def convert_to_radian(value, unit):
        if unit == 'deg':
            value = value * 0.0174533
        return value

    if request.method == 'POST':
        angle = request.POST.get('angle')
        angle_op = request.POST.get('angle_op')

        if '.' in angle:
            angle = float(angle)
        else:
            angle = int(angle)

        # if angle_op == 'rad':
        #     angle_in_deg = angle * 57.295779513
        if (angle_op == 'deg' and angle % 180 == 0) or (angle_op == 'rad' and angle == 0):
            result = 'Undefined'
        else:
            if angle_op == 'deg':
                x = convert_to_radian(angle, angle_op)
            else:
                x = angle
            result = round(1 / math.sin(x), 8)

        context = {
            'result': result,
            'angle': angle,
            'angle_op': angle_op,
            'flag': True
        }
        return render(request, 'mathematics/cosecant.html', context)
    else:
        return render(request, 'mathematics/cosecant.html', {'flag': False})


def double_angle_formula(request):
    def convert_to_radian(value, unit):
        if unit == 'deg':
            value = value * (math.pi / 180)
        return value

    if request.method == 'POST':
        angle = request.POST.get('angle')
        angle_op = request.POST.get('angle_op')
        sol_op = request.POST.get('sol_op')

        if '.' in angle:
            angle = float(angle)
        else:
            angle = int(angle)

        sign = ''
        if angle_op == 'deg':
            x = convert_to_radian(angle, angle_op)
            sign = '°'
            angle_in_deg = angle
        else:
            x = angle
            angle_in_deg = angle * 57.295779513

        # Calculating sin2θ
        # sin2θ  = 2 * math.sin(x)*math.cos(x)
        sin_intermediate_result_1 = math.sin(x)
        sin_intermediate_result_2 = math.cos(x)
        sin_result = round(2 * sin_intermediate_result_1 * sin_intermediate_result_2, 8)

        # Calculating cos2θ
        # cos2θ = 1 - 2* sin(sqr)θ
        cos_intermediate_result_1 = sin_intermediate_result_1
        cos_result = round(1 - (2 * math.pow(cos_intermediate_result_1, 2)), 8)

        # Calculating tan2θ
        # (2 * tan(θ)) /( 1- tan(sqr)θ)
        tan_intermediate_result_1 = math.tan(x)
        if (tan_intermediate_result_1 * tan_intermediate_result_1 == 1) or (angle_op == 'deg' and angle % 180 == 45):
            tan_result = 'Undefined'
        else:
            tan_result = round((2 * tan_intermediate_result_1) / (1 - math.pow(tan_intermediate_result_1, 2)), 8)

        context = {
            'sin_result': sin_result,
            'sin_inter_1': sin_intermediate_result_1,
            'sin_inter_2': sin_intermediate_result_2,

            'cos_result': cos_result,
            'cos_inter_1': cos_intermediate_result_1,

            'tan_result': tan_result,
            'tan_inter_1': tan_intermediate_result_1,

            'angle': angle,
            'angle_in_deg': angle_in_deg,
            'angle_op': angle_op,
            'sol_op': sol_op,
            'sign': sign,
            'flag': True
        }
        return render(request, 'mathematics/double_angle_formula.html', context)
    else:
        return render(request, 'mathematics/double_angle_formula.html', {'flag': False})


def sum_of_linear_number_sequence(request):
    # to check for float values in input
    def check_decimal_values(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    # to generate the number sequence
    def find_sequence(periods, init_value, diff):
        p_ceil = math.ceil(periods)
        print("p_ceil-----------------", p_ceil)
        result_seq = ''
        count = 1
        start_value = init_value
        while count <= p_ceil:
            result_seq = result_seq + str(start_value) + ", "
            start_value = start_value + diff
            count += 1
        return result_seq

    if request.method == "POST":
        init_value = request.POST.get('init_value')  # values from form input
        diff = request.POST.get('diff')
        periods = request.POST.get('periods')
        fin_value = request.POST.get('fin_value')

        given = request.POST['given']

        # when initial value is choosen
        if given == "form1" and diff and periods and fin_value:
            diff = request.POST.get('diff')
            diff = check_decimal_values(diff)

            periods = request.POST.get('periods')
            periods = check_decimal_values(periods)

            fin_value = request.POST.get('fin_value')
            fin_value = check_decimal_values(fin_value)

            # Error condition
            if periods <= 0:
                messages.error(request, 'Periods should be greater than 0 and integer value')
                context = {'given': 'form1', 'diff': diff, 'fin_value': fin_value}
                return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)

            init_value_result = fin_value - (periods - 1) * diff
            sum = (periods / 2) * (init_value_result + fin_value)
            # print("sum  is : -------", sum)

            result_seq = find_sequence(periods, init_value_result, diff)

            context = {
                'given': given,
                'diff': diff,
                'periods': periods,
                'fin_value': fin_value,
                'init_value_result': init_value_result,
                'sum': sum,
                'sequence': result_seq,
                'flag1': True,
            }

            return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)

        # when Differnce is choosen
        elif given == "form2" and init_value and periods and fin_value:
            init_value = request.POST.get('init_value')
            init_value = check_decimal_values(init_value)

            periods = request.POST.get('periods')
            periods = check_decimal_values(periods)

            fin_value = request.POST.get('fin_value')
            fin_value = check_decimal_values(fin_value)

            if periods <= 0:
                messages.error(request, 'Periods should be greater than 0')
                context = {'given': 'form2', 'init_value': init_value, 'fin_value': fin_value, 'periods': periods}
                return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)

            diff_result = (fin_value - init_value) / (periods - 1)

            sum = (periods / 2) * (init_value + fin_value)

            result_seq = find_sequence(periods, init_value, diff_result)

            context = {
                'given': given,
                'diff_result': diff_result,
                'init_value': init_value,
                'periods': periods,
                'fin_value': fin_value,
                'sum': sum,
                'sequence': result_seq,
                'flag2': True
            }

            return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)

        # when Periods is choosen
        elif given == "form3" and init_value and diff and fin_value:

            diff = request.POST.get('diff')
            diff = check_decimal_values(diff)

            init_value = request.POST.get('init_value')
            init_value = check_decimal_values(init_value)

            fin_value = request.POST.get('fin_value')
            fin_value = check_decimal_values(fin_value)

            periods_result = ((fin_value - init_value) / diff) + 1
            # print("periods-------------------------",periods_result)

            # print(" result sequence -------------------", result_seq)
            if periods_result <= 0:
                messages.error(request, 'Periods should be greater than 0 ')
                context = {'given': 'form2', 'init_value': init_value, 'fin_value': fin_value}
                return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)

            sum = (periods_result / 2) * (init_value + fin_value)
            print("sum  is : -------", sum)

            result_seq = find_sequence(periods_result, init_value, diff)

            context = {
                'given': given,
                'diff': diff,
                'init_value': init_value,
                'fin_value': fin_value,
                'periods_result': periods_result,
                # 'periods_ceil':periods_ceil,
                'sum': sum,
                'sequence': result_seq,
                'flag3': True
            }
            return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)
        # when Find Final value is choosen
        if given == "form4" and init_value and diff and periods:
            diff = request.POST.get('diff')
            diff = check_decimal_values(diff)

            periods = request.POST.get('periods')
            periods = check_decimal_values(periods)

            init_value = request.POST.get('init_value')
            init_value = check_decimal_values(init_value)

            if periods <= 0:
                messages.error(request, 'Periods should be greater than 0')
                context = {'given': 'form4', 'diff': diff, 'init_value': init_value, 'periods': periods}
                return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)

            fin_value_result = init_value + (periods - 1) * diff

            sum = (periods / 2) * (init_value + fin_value_result)
            print("sum  is : -------", sum)
            result_seq = find_sequence(periods, init_value, diff)

            # sequence = numpy.linspace(init_value, fin_value_result, periods)
            # print("sequence---------", sequence, type(sequence))
            # result_seq = ''
            # for i in sequence:
            #     result_seq = result_seq + str(i) + ",  "
            # print(result_seq,"---------")

            context = {
                'given': given,
                'diff': diff,
                'periods': periods,
                'init_value': init_value,
                'sum': sum,
                'sequence': result_seq,
                'fin_value_result': fin_value_result,
                'flag4': True
            }
            return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)
        return render(request, 'mathematics/sum-of-linear-number-sequence.html',
                      {'given': given, 'diff': 2, 'periods': 5, 'fin_value': 10, 'init_value': 1})
    else:
        return render(request, 'mathematics/sum-of-linear-number-sequence.html',
                      {'given': 'form1', 'diff': 2, 'periods': 5, 'fin_value': 10})


def angle_between_two_vectors(request):
    # to check for float values in input
    def check_decimal_values(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':

        given = request.POST['given']
        print("given-----------------", given)

        given_2d_a = request.POST.get('given_2d_a')
        a_2d_x = request.POST.get('a_2d_cr_x')
        a_2d_y = request.POST.get('a_2d_cr_y')
        a_2d_x1 = request.POST.get('a_2d_pr_x1')
        a_2d_y1 = request.POST.get('a_2d_pr_y1')
        a_2d_x2 = request.POST.get('a_2d_pr_x2')
        a_2d_y2 = request.POST.get('a_2d_pr_y2')
        print("given_2d_a-----------------", given_2d_a)

        given_2d_b = request.POST.get('given_2d_b')
        b_2d_x = request.POST.get('b_2d_cr_x')
        b_2d_y = request.POST.get('b_2d_cr_y')
        b_2d_x1 = request.POST.get('b_2d_pr_x1')
        b_2d_y1 = request.POST.get('b_2d_pr_y1')
        b_2d_x2 = request.POST.get('b_2d_pr_x2')
        b_2d_y2 = request.POST.get('b_2d_pr_y2')
        print("given_2d_b-----------------", given_2d_b)

        given_3d_a = request.POST.get('given_3d_a')
        a_3d_x = request.POST.get('a_3d_cr_x')
        a_3d_y = request.POST.get('a_3d_cr_y')
        a_3d_z = request.POST.get('a_3d_cr_z')
        a_3d_x1 = request.POST.get('a_3d_pr_x1')
        a_3d_y1 = request.POST.get('a_3d_pr_y1')
        a_3d_z1 = request.POST.get('a_3d_pr_z1')
        a_3d_x2 = request.POST.get('a_3d_pr_x2')
        a_3d_y2 = request.POST.get('a_3d_pr_y2')
        a_3d_z2 = request.POST.get('a_3d_pr_z2')
        print("given_3d_a-----------------", given_3d_a)

        given_3d_b = request.POST.get('given_3d_b')
        b_3d_x = request.POST.get('b_3d_cr_x')
        b_3d_y = request.POST.get('b_3d_cr_y')
        b_3d_z = request.POST.get('b_3d_cr_z')
        b_3d_x1 = request.POST.get('b_3d_pr_x1')
        b_3d_y1 = request.POST.get('b_3d_pr_y1')
        b_3d_z1 = request.POST.get('b_3d_pr_z1')
        b_3d_x2 = request.POST.get('b_3d_pr_x2')
        b_3d_y2 = request.POST.get('b_3d_pr_y2')
        b_3d_z2 = request.POST.get('b_3d_pr_z2')
        print("given_3d_b-----------------", given_3d_b)

        if given == 'form1':
            if a_2d_x and a_2d_y and b_2d_x and b_2d_y:
                a_2d_x = check_decimal_values(a_2d_x)
                a_2d_y = check_decimal_values(a_2d_y)
                b_2d_x = check_decimal_values(b_2d_x)
                b_2d_y = check_decimal_values(b_2d_y)
                x = (a_2d_x * b_2d_x) + (a_2d_y * b_2d_y)
                y = math.sqrt(math.pow(a_2d_x, 2) + math.pow(a_2d_y, 2)) \
                    * math.sqrt(math.pow(b_2d_x, 2) + math.pow(b_2d_y, 2))

                result = numpy.arccos(x / y)


            elif a_2d_x and a_2d_y and b_2d_x1 and b_2d_y1 and b_2d_x2 and b_2d_y2:
                a_2d_x = check_decimal_values(a_2d_x)
                a_2d_y = check_decimal_values(a_2d_y)
                b_2d_x1 = check_decimal_values(b_2d_x1)
                b_2d_y1 = check_decimal_values(b_2d_y1)
                b_2d_x2 = check_decimal_values(b_2d_x2)
                b_2d_y2 = check_decimal_values(b_2d_y2)

                x = (a_2d_x * (b_2d_x2 - b_2d_x1)) + (a_2d_y * (b_2d_y2 - b_2d_y1))
                y = math.sqrt(math.pow(a_2d_x, 2) + math.pow(a_2d_y, 2)) \
                    * math.sqrt(math.pow((b_2d_x2 - b_2d_x1), 2) + math.pow((b_2d_y2 - b_2d_y1), 2))

                result = numpy.arccos(x / y)

            elif b_2d_x and b_2d_y and a_2d_x1 and a_2d_y1 and a_2d_x2 and a_2d_y2:

                a_2d_x1 = check_decimal_values(a_2d_x1)
                a_2d_y1 = check_decimal_values(a_2d_y1)
                a_2d_x2 = check_decimal_values(a_2d_x2)
                a_2d_y2 = check_decimal_values(a_2d_y2)
                b_2d_x = check_decimal_values(b_2d_x)
                b_2d_y = check_decimal_values(b_2d_y)

                x = ((a_2d_x2 - a_2d_x1) * b_2d_x) + ((a_2d_y2 - a_2d_y1) * b_2d_y)
                y = math.sqrt(math.pow((a_2d_x2 - a_2d_x1), 2) + math.pow((a_2d_y2 - a_2d_y1), 2)) \
                    * math.sqrt(math.pow(b_2d_x, 2) + math.pow(b_2d_y, 2))

                result = numpy.arccos(x / y)


            elif a_2d_x1 and a_2d_y1 and a_2d_x2 and a_2d_y2 \
                    and b_2d_x1 and b_2d_y1 and b_2d_x2 and b_2d_y2:
                a_2d_x1 = check_decimal_values(a_2d_x1)
                a_2d_y1 = check_decimal_values(a_2d_y1)
                a_2d_x2 = check_decimal_values(a_2d_x2)
                a_2d_y2 = check_decimal_values(a_2d_y2)
                b_2d_x1 = check_decimal_values(b_2d_x1)
                b_2d_y1 = check_decimal_values(b_2d_y1)
                b_2d_x2 = check_decimal_values(b_2d_x2)
                b_2d_y2 = check_decimal_values(b_2d_y2)

                x = ((a_2d_x2 - a_2d_x1) * (b_2d_x2 - b_2d_x1)) + ((a_2d_y2 - a_2d_y1) * (b_2d_y2 - b_2d_y1))
                y = math.sqrt(math.pow((a_2d_x2 - a_2d_x1), 2) + math.pow((a_2d_y2 - a_2d_y1), 2)) \
                    * math.sqrt(math.pow((b_2d_x2 - b_2d_x1), 2) + math.pow((b_2d_y2 - b_2d_y1), 2))

                result = numpy.arccos(x / y)

        if given == 'form2':
            if a_3d_x and a_3d_y and a_3d_z and b_3d_x and b_3d_y and b_3d_z:
                a_3d_x = check_decimal_values(a_3d_x)
                a_3d_y = check_decimal_values(a_3d_y)
                a_3d_z = check_decimal_values(a_3d_z)
                b_3d_x = check_decimal_values(b_3d_x)
                b_3d_y = check_decimal_values(b_3d_y)
                b_3d_z = check_decimal_values(b_3d_z)

                x = (a_3d_x * b_3d_x) + (a_3d_y * b_3d_y) + (a_3d_z * b_3d_z)
                y = math.sqrt(math.pow(a_3d_x, 2) + math.pow(a_3d_y, 2) + math.pow(a_3d_z, 2)) \
                    * math.sqrt(math.pow(b_3d_x, 2) + math.pow(b_3d_y, 2) + math.pow(b_3d_z, 2))

                result = numpy.arccos(x / y)



            elif a_3d_x and a_3d_y and a_3d_z and b_3d_x1 and b_3d_y1 \
                    and b_3d_z1 and b_3d_x2 and b_3d_y2 and b_3d_z2:
                a_3d_x = check_decimal_values(a_3d_x)
                a_3d_y = check_decimal_values(a_3d_y)
                a_3d_z = check_decimal_values(a_3d_z)
                b_3d_x1 = check_decimal_values(b_3d_x1)
                b_3d_y1 = check_decimal_values(b_3d_y1)
                b_3d_z1 = check_decimal_values(b_3d_z1)
                b_3d_x2 = check_decimal_values(b_3d_x2)
                b_3d_y2 = check_decimal_values(b_3d_y2)
                b_3d_z2 = check_decimal_values(b_3d_z2)

                x = (a_3d_x * (b_3d_x2 - b_3d_x1)) + (a_3d_y * (b_3d_y2 - b_3d_y1)) + (a_3d_z * (b_3d_z2 - b_3d_z1))
                y = math.sqrt(math.pow(a_3d_x, 2) + math.pow(a_3d_y, 2) + math.pow(a_3d_z, 2)) \
                    * math.sqrt(
                    math.pow((b_3d_x2 - b_3d_x1), 2) + math.pow((b_3d_y2 - b_3d_y1), 2) + math.pow((b_3d_z2 - b_3d_z1),
                                                                                                   2))

                result = numpy.arccos(x / y)


            elif b_3d_x and b_3d_y and b_3d_z and a_3d_x1 and a_3d_y1 \
                    and a_3d_z1 and a_3d_x2 and a_3d_y2 and a_3d_z2:

                a_3d_x1 = check_decimal_values(a_3d_x1)
                a_3d_y1 = check_decimal_values(a_3d_y1)
                a_3d_z1 = check_decimal_values(a_3d_z1)
                a_3d_x2 = check_decimal_values(a_3d_x2)
                a_3d_y2 = check_decimal_values(a_3d_y2)
                a_3d_z2 = check_decimal_values(a_3d_z2)
                b_2d_x = check_decimal_values(b_3d_x)
                b_3d_y = check_decimal_values(b_3d_y)
                b_3d_z = check_decimal_values(b_3d_z)

                x = ((a_3d_x2 - a_3d_x1) * b_3d_x) + ((a_3d_y2 - a_3d_y1) * b_3d_y) + ((a_3d_z2 - a_3d_z1) * b_3d_z)
                y = math.sqrt(
                    math.pow((a_3d_x2 - a_3d_x1), 2) + math.pow((a_3d_y2 - a_3d_y1), 2) + math.pow((a_3d_z2 - a_3d_z1),
                                                                                                   2)) \
                    * math.sqrt(math.pow(b_3d_x, 2) + math.pow(b_3d_y, 2) + math.pow(b_3d_z, 2))

                result = numpy.arccos(x / y)


            elif a_3d_x1 and a_3d_y1 and a_3d_z1 and a_3d_x2 and a_3d_y2 and a_3d_z2 \
                    and b_3d_x1 and b_3d_y1 and b_3d_z1 and b_3d_x2 and b_3d_y2 and b_3d_z2:
                a_3d_x1 = check_decimal_values(a_3d_x1)
                a_3d_y1 = check_decimal_values(a_3d_y1)
                a_3d_z1 = check_decimal_values(a_3d_z1)
                a_3d_x2 = check_decimal_values(a_3d_x2)
                a_3d_y2 = check_decimal_values(a_3d_y2)
                a_3d_z2 = check_decimal_values(a_3d_z2)

                b_3d_x1 = check_decimal_values(b_3d_x1)
                b_3d_y1 = check_decimal_values(b_3d_y1)
                b_3d_z1 = check_decimal_values(b_3d_z1)
                b_3d_x2 = check_decimal_values(b_3d_x2)
                b_3d_y2 = check_decimal_values(b_3d_y2)
                b_3d_z2 = check_decimal_values(b_3d_z2)

                x = ((a_3d_x2 - a_3d_x1) * (b_3d_x2 - b_3d_x1)) + ((a_3d_y2 - a_3d_y1) * (b_3d_y2 - b_3d_y1)) + (
                            (a_3d_z2 - a_3d_z1) * (b_3d_z2 - b_3d_z1))
                y = math.sqrt(
                    math.pow((a_3d_x2 - a_3d_x1), 2) + math.pow((a_3d_y2 - a_3d_y1), 2) + math.pow((a_3d_z2 - a_3d_z1),
                                                                                                   2)) \
                    * math.sqrt(
                    math.pow((b_3d_x2 - b_3d_x1), 2) + math.pow((b_3d_y2 - b_3d_y1), 2) + math.pow((b_3d_z2 - b_3d_z1),
                                                                                                   2))

                result = numpy.arccos(x / y)

        context = {
            'given': given,
            'given_2d_a': given_2d_a,
            'given_2d_b': given_2d_b,
            'given_3d_a': given_3d_a,  # angle_between_two_vectors, backup_angle_btw_2_vectors
            'given_3d_b': given_3d_b
        }
        return render(request, 'mathematics/angle_between_two_vectors.html', context)

    else:
        return render(request, 'mathematics/angle_between_two_vectors.html',
                      {'given': 'form1', 'given_2d_a': 'cr', 'given_2d_b': 'cr'})


def gradient(request):
    # to check for float values in input
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        x1 = request.POST.get('x1')
        y1 = request.POST.get('y1')
        x2 = request.POST.get('x2')
        y2 = request.POST.get('y2')

        x1 = check_decimal(x1)
        y1 = check_decimal(y1)
        x2 = check_decimal(x2)
        y2 = check_decimal(y2)

        if x1 == x2 and y1 == y2:
            messages.error(request,
                           'You have inputted the same position twice, so the line and the gradient are undefined.')
            return render(request, 'mathematics/gradient.html', {'y1': y1, 'y2': y2, 'x1': x1, 'x2': x2})
        elif x1 == x2:
            messages.error(request, 'The line is vertical; therefore the gradient is undefined.')
            return render(request, 'mathematics/gradient.html', {'y1': y1, 'y2': y2, 'x1': x1, 'x2': x2})

        rise = round((y2 - y1), 8)
        run = round((x2 - x1), 8)
        gradient = round((rise / run), 5)

        context = {
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2,
            'rise': rise,
            'run': run,
            'gradient': gradient,
            'flag': True,
        }
        return render(request, 'mathematics/gradient.html', context)
    else:
        return render(request, 'mathematics/gradient.html', {'x1': 2, 'x2': 4, 'y1': 3, 'y2': 6})


def parabola(request):
    from sympy import simplify, symbols, expand, factor

    # to check for float values in input
    def check_decimal_values(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        given = request.POST['given']

        # form1
        f1_a = request.POST.get('f1_a')
        f1_b = request.POST.get('f1_b')
        f1_c = request.POST.get('f1_c')

        # form2
        f2_a = request.POST.get('f2_a')
        f2_h = request.POST.get('f2_h')
        f2_k = request.POST.get('f2_k')

        # form4
        # form2
        f4_x = request.POST.get('f4_x')
        f4_y = request.POST.get('f4_y')
        f4_h = request.POST.get('f4_h')
        f4_k = request.POST.get('f4_k')

        if given == 'form1' and f1_a and f1_b and f1_c:
            f1_a = check_decimal_values(f1_a)
            f1_b = check_decimal_values(f1_b)
            f1_c = check_decimal_values(f1_c)
            # print(" a, h , k -----------", a, h, k)

            x = symbols('x')
            # e1 = expand()
            # print("-------------expand is is-----  {}".format(e1))
            expr = f1_a * x ** 2 + f1_b * x + f1_c
            smpl = simplify(expr)

            # # print("-------------experssions is-----  {}".format(smpl1))
            # smpl = simplify(expr)
            # ex = expand(smpl)
            print("smpl-------", smpl)
            print("-------------experssions is-----  {}".format(smpl))
            # print("-------------expand is is-----  {}".format(ex))
            focus_x = round((-(f1_b) / (2 * f1_a)), 3)
            focus_y = round((f1_c - (f1_b * f1_b - 1) / (4 * f1_a)), 3)
            vertex_x = round((-(f1_b) / (2 * f1_a)), 3)
            vertex_y = round((f1_c - f1_b * f1_b / (4 * f1_a)), 3)
            directrix = round((f1_c - (f1_b * f1_b + 1) / (4 * f1_a)), 3)

            context = {
                'given': given,
                'result': smpl,
                'f1_a': f1_a,
                'f1_b': f1_b,
                'f1_c': f1_c,
                'focus_x': focus_x,
                'focus_y': focus_y,
                'vertex_x': vertex_x,
                'vertex_y': vertex_y,
                'directrix': directrix,

                'flag1': True
    
            }
            return render(request, 'mathematics/parabola.html', context)


        elif given == 'form2' and f2_a and f2_h and f2_k:

            f2_a = check_decimal_values(f2_a)
            f2_h = check_decimal_values(f2_h)
            f2_k = check_decimal_values(f2_k)
            print(" a, h , k -----------", f2_a, f2_h, f2_k)
            if f2_a == 0:
                messages.error(request, "Parameter 'a' can never equal zero for a parabola")
                context = {
                    'given': given,
                    'f2_a': f2_a,
                    'f2_h': f2_h,
                    'f2_k': f2_k,

                }
                return render(request, 'mathematics/parabola.html', context)

            x = symbols('x')
            e1 = expand((x - f2_h) ** 2)
            # print("-------------expand is is-----  {}".format(e1))
            expr = f2_a * (e1) + f2_k
            smpl = simplify(expr)
            factor = factor(smpl)
            print(" factors -----------------", factor)

            # # print("-------------experssions is-----  {}".format(smpl1))
            # smpl = simplify(expr)
            # ex = expand(smpl)
            print("smpl-------", smpl)
            print("-------------experssions is-----  {}".format(smpl))
            # print("-------------expand is is-----  {}".format(ex))

            # directrix calculations
            b = -(f2_h * 2 * f2_a)
            c = f2_k + (b * b) / 4 * f2_a
            directrix = round((c - (b * b + 1) / 4 * f2_a), 3)
            vertex_x = f2_h
            vertex_y = f2_k
            focus_x = f2_h
            focus_y = c - (b * b - 1) / 4 * f2_a
            y_intercept = c

            context = {
                'given': given,
                'result': smpl,
                'f2_a': f2_a,
                'f2_h': f2_h,
                'f2_k': f2_k,
                'vertex_x': vertex_x,
                'vertex_y': vertex_y,
                'focus_x': focus_x,
                'focus_y': focus_y,
                'y_intercept': y_intercept,
                'directrix': directrix,
                'flag2': True
            }
            return render(request, 'mathematics/parabola.html', context)

        elif given == 'form4' and f4_h and f4_k and f4_x and f4_y:

            f4_h = check_decimal_values(f4_h)
            f4_k = check_decimal_values(f4_k)
            f4_x = check_decimal_values(f4_x)
            f4_y = check_decimal_values(f4_y)

            if f4_h != f4_x:
                messages.error(request,
                               "The x-coordinate of the vertex (h) and the focus (xₒ) should be the same! "
                               "Consider changing the orientation of the parabola to horizontal.")
                context = {
                    'given': given, 'f4_h': f4_h, 'f4_k': f4_k, 'f4_x': f4_x, 'f4_y': f4_y,
                }
                return render(request, 'mathematics/parabola.html', context)

            x = symbols('x')
            e1 = expand((x - f2_h) ** 2)
            # print("-------------expand is is-----  {}".format(e1))
            expr = f2_a * (e1) + f2_k
            smpl = simplify(expr)
            factor = factor(smpl)
            print(" factors -----------------", factor)

            # # print("-------------experssions is-----  {}".format(smpl1))
            # smpl = simplify(expr)
            # ex = expand(smpl)
            print("smpl-------", smpl)
            print("-------------experssions is-----  {}".format(smpl))
            # print("-------------expand is is-----  {}".format(ex))

            # directrix calculations
            b = -(f2_h * 2 * f2_a)
            c = f2_k + (b * b) / 4 * f2_a
            directrix = round((c - (b * b + 1) / 4 * f2_a), 3)
            vertex_x = f2_h
            vertex_y = f2_k
            focus_x = f2_h
            focus_y = c - (b * b - 1) / 4 * f2_a
            y_intercept = c

            context = {
                'given': given,
                'result': smpl,
                'f2_a': f2_a,
                'f2_h': f2_h,
                'f2_k': f2_k,
                'vertex_x': vertex_x,
                'vertex_y': vertex_y,
                'focus_x': focus_x,
                'focus_y': focus_y,
                'y_intercept': y_intercept,
                'directrix': directrix,
                'flag2': True
            }
            return render(request, 'mathematics/parabola.html', context)
        return render(request, 'mathematics/parabola.html', {'given': given})

    else:
        return render(request, 'mathematics/parabola.html', {'given': 'form1'})


def parallel_line(request):
    # to check for float values in input
    def check_decimal_values(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        m = request.POST['m']
        r = request.POST['r']
        x = request.POST['x']
        y = request.POST['y']

        m = check_decimal_values(m)
        r = check_decimal_values(r)
        x = check_decimal_values(x)
        y = check_decimal_values(y)

        a = m
        # b = y - m * x
        b = y - m * x
        b = round(b, 4)
        # print("b---a--------------",b, a)

        # D = | b - r | / √(m² + 1)
        # print("absolute--------------",abs(b-r))
        distance = abs(b - r) / math.sqrt(m * m + 1)
        distance = round(distance, 4)
        # print("difffff--------------", distance)

        context = {'x': x, 'y': y, 'm': m, 'r': r, 'a': a, 'b': b, 'distance': distance, 'flag': True

                   }
        return render(request, 'mathematics/parallel_line.html', context)

    else:
        return render(request, 'mathematics/parallel_line.html', {'x': 2, 'y': 3, 'm': 4, 'r': 5})


def linear_interpolation(request):
    from sympy import simplify, symbols

    # to check for float values in input
    def check_decimal_values(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        x1 = request.POST['x1']
        y1 = request.POST['y1']
        x2 = request.POST['x2']
        y2 = request.POST['y2']

        x1 = check_decimal_values(x1)
        x2 = check_decimal_values(x2)
        y1 = check_decimal_values(y1)
        y2 = check_decimal_values(y2)

        x = symbols('x')
        # e1 = expand()
        # print("-------------expand is is-----  {}".format(e1))
        expr = (x - x1) * ((y2 - y1) / (x2 - x1)) + y1
        smpl = simplify(expr)

        x_coef = round(smpl.coeff(x, 1), 4)
        print("type smpl-----------", type(smpl), smpl)
        eq_in_str = str(smpl)
        constt = eq_in_str.split()[-1]
        print(constt, type(constt))
        print("type x_coeff-----------", type(x_coef), x_coef)

        # print("simplified-------------",smpl)
        context = {
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2,
            'equation': smpl,
            'x_coef': x_coef,
            'constt': constt,
            'flag': True
        }
        return render(request, 'mathematics/linear_interpolation.html', context)

    else:
        return render(request, 'mathematics/linear_interpolation.html', {'x1': 2, 'y1': 3, 'x2': 4, 'y2': 5})


def midpoint(request):

    # to check for float values in input
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        x1 = request.POST.get('x1')
        y1 = request.POST.get('y1')
        x2 = request.POST.get('x2')
        y2 = request.POST.get('y2')

        x1 = check_decimal(x1)
        y1 = check_decimal(y1)
        x2 = check_decimal(x2)
        y2 = check_decimal(y2)

        x_midpoint = (x1 + x2) / 2
        y_midpoint = (y1 + y2) / 2
        # print("-------------", x_midpoint, y_midpoint)
        x_midpoint = round(x_midpoint, 4)
        y_midpoint = round(y_midpoint, 4)

        context = {
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2,
            'x_midpoint': x_midpoint,
            'y_midpoint': y_midpoint,
            'flag':True,
        }
        return render(request, 'mathematics/midpoint.html', context)
    else:
        context = {
            'x1': 2,
            'y1': 6,
            'x2': 4,
            'y2': 10,
        }
        return render(request, 'mathematics/midpoint.html', context)

def cartesian_to_polar(request):

    # to check for float values in input
    def check_decimal_values(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    # conversion
    def convert_to_radian(value, unit):
        if unit == 'deg':
            value = value * 0.0174533
        elif unit == 'gon':
            value = value * 0.015708
        elif unit == 'mrad':
            value = value * 0.001
        elif unit == 'μrad':
            value = value * 0.000001
        elif unit == 'arcmin':
            value = value * 0.000290888
        elif unit == 'arcsec':
            value = value * 0.0000048501
        elif unit == 'tr':
            value = value * 6.28319
        return value

    def convert_radian_to_other(valueinradian):
        all_conversions_string = {
            "value in degree": str(round((valueinradian * 57.2958), 5)) + " deg",
            "value in radian": str(valueinradian) + " rad",
            "value in gradians": str(round((valueinradian * 63.662), 5)) + " gon",
            "value in turns": str(round((valueinradian * 0.159155), 5)) + " tr",
            "value in arcmin": str(round((valueinradian * 3437.75), 5)) + " arcmin",
            "value in arcsec": str(round((valueinradian * 206265), 5)) + " arcsec",
            "value in mrad": str(round((valueinradian * 1000), 5)) + " mrad",
            "value in microrad": str(round((valueinradian * 1000000), 5)) + " μrad"
        }
        return all_conversions_string

    if request.method == "POST":
        given = request.POST.get('given')
        x = request.POST.get('x')
        y = request.POST.get('y')
        r = request.POST.get('r')
        t = request.POST.get('t')
        t_op = request.POST.get('t_op')

        if given == 'form1' and x and y:
            x = check_decimal_values(x)
            y = check_decimal_values(y)

            # r = √(x² + y²)
            r_result = math.sqrt(math.pow(x,2) + math.pow(y,2))
            r_result = round(r_result, 5)

            # θ = arctan(y / x)
            t_result = numpy.arctan(y/x)

            all_conversions = convert_radian_to_other(t_result)
            t_result = str(round((t_result * 57.2958), 5)) + " deg"


            context = {
                'x':x, 'y':y, 'r_result':r_result, 't_result':t_result, 't':t, 'r':r, 'given':given,'flag1':True,
                'all_conversions':all_conversions,
            }
            return render(request, 'mathematics/cartesian_to_polar.html', context)


        elif given == 'form2' and r and t and t_op:
            r = check_decimal_values(r)
            t = check_decimal_values(t)
            if r < 0:
                messages.error(request, 'R cannot be negative')
                context = {
                    't': t, 'r': r, 'given': given
                }
                return render(request, 'mathematics/cartesian_to_polar.html', context)

            rad_con = convert_to_radian(t, t_op)

            # x = r * cosθ
            x_result = r * math.cos(rad_con)
            x_result = round(x_result, 5)
            # y = r * sinθ
            y_result = r * math.sin(rad_con)
            y_result = round(y_result, 5)

            context = {
                'x_result': x_result, 'y_result': y_result, 't': t, 'r': r, 'given': given,'t_op':t_op,
                'flag2': True,
            }
            return render(request, 'mathematics/cartesian_to_polar.html', context)

        return render(request, 'mathematics/cartesian_to_polar.html', {'given':given})

    else:
        return render(request, 'mathematics/cartesian_to_polar.html', {'given':'form1', 'x':4, 'y':6} )


def slope_intercept_form(request):
    # to check for float values in input
    def check_decimal_values(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        x1 = request.POST.get('x1')
        y1 = request.POST.get('y1')
        x2 = request.POST.get('x2')
        y2 = request.POST.get('y2')

        x1 = check_decimal_values(x1)
        y1 = check_decimal_values(y1)
        x2 = check_decimal_values(x2)
        y2 = check_decimal_values(y2)

        # m calculation m = (y₂ - y₁)/(x₂ - x₁)
        y = y2 - y1
        x = x2 - x1
        m = y/x

        # b calculation b = y₁ - m * x₁
        b = y1 - (m*x1)

        x_intercept =  round((-b/m), 4)
        y_intercept = round(b, 4)

        b = round(b, 4)
        m = round(m, 4)

        context = {
            'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2,
            'm_result':m, 'b_result':b,
            'y':y, 'x':x, 'x_intercept':x_intercept, 'y_intercept':y_intercept,
            'flag':True,
        }
        return render(request, 'mathematics/slope_intercept_form.html', context)

    else:
        return render(request, 'mathematics/slope_intercept_form.html', {'x1':4, 'x2':9, 'y1':3, 'y2':12})



def dot_product(request):

    # to check for float values in input
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    def convert_radian_to_other(valueinradian):
        all_conversions_string = {
            "value in degree": str(round((valueinradian * 57.2958), 5)) + " degrees (deg)",
            "value in radian": str(valueinradian) + " radian (rad)",
            "value in gradians": str(round((valueinradian * 63.662), 5)) + " gradian (gon)",
            "value in turns": str(round((valueinradian * 0.159155), 5)) + " turns (tr)",
            "value in arcmin": str(round((valueinradian * 3437.75), 5)) + " minutes of arc (arcmin)",
            "value in arcsec": str(round((valueinradian * 206265), 5)) + " seconds of arc (arcsec)",
            "value in mrad": str(round((valueinradian * 1000), 5)) + " miliradian (mrad)",
            "value in microrad": str(round((valueinradian * 1000000), 5)) + " microradian (μrad)"
        }
        return all_conversions_string


    if request.method == 'POST':
        x1 = request.POST.get('x1')
        y1 = request.POST.get('y1')
        z1 = request.POST.get('z1')
        x2 = request.POST.get('x2')
        y2 = request.POST.get('y2')
        z2 = request.POST.get('z2')

        x1 = check_decimal(x1)
        y1 = check_decimal(y1)
        z1 = check_decimal(z1)
        x2 = check_decimal(x2)
        y2 = check_decimal(y2)
        z2 = check_decimal(z2)

        x = x1*x2
        y = y1*y2
        z = z1*z2

        dotProduct = x + y + z
        a_vector = math.sqrt(pow(x1,2) + pow(y1,2)+ pow(z1,2))
        if a_vector < 0:
            a_vector = -(a_vector)
        b_vector = math.sqrt(pow(x2, 2)+pow(y2, 2)+pow(z2,2))
        if b_vector < 0:
            b_vector = -(b_vector)
        mag_vec = a_vector*b_vector
        a_vector = round(a_vector, 5)
        b_vector = round(b_vector, 5)

        angle_result = round(math.acos(dotProduct/mag_vec), 5)

        all_conversions = convert_radian_to_other(angle_result)
        dotProduct = round(dotProduct, 4)

        context = {
            'a_vector':a_vector,
            'b_vector':b_vector,
            'mag_vec':mag_vec,
            'angle_result':angle_result,
            'dotProduct':dotProduct,
            'all_conversions':all_conversions,
            'x':x, 'y':y, 'z':z,
            'x1':x1, 'y1':y1, 'z1':z1, 'x2':x2, 'y2':y2, 'z2':z2,
            'flag':True
        }
        return render(request, 'mathematics/dot_product.html', context)
    else:
        return render(request, 'mathematics/dot_product.html', {'x1':2, 'y1':4, 'z1':6, 'x2':7, 'y2':9, 'z2':12 })




def cross_product(request):

    # to check for float values in input
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value


    if request.method == 'POST':
        x1 = request.POST.get('x1')
        y1 = request.POST.get('y1')
        z1 = request.POST.get('z1')
        x2 = request.POST.get('x2')
        y2 = request.POST.get('y2')
        z2 = request.POST.get('z2')

        x1 = check_decimal(x1)
        y1 = check_decimal(y1)
        z1 = check_decimal(z1)
        x2 = check_decimal(x2)
        y2 = check_decimal(y2)
        z2 = check_decimal(z2)

        x = round((y1*z2 - z1*y2), 4)
        y = round((z1*x2 - x1*z2), 4)
        z = round((x1*y2 - y1*x2), 4)
        context = {
            'x':x, 'y':y, 'z':z,
            'x1':x1, 'y1':y1, 'z1':z1, 'x2':x2, 'y2':y2, 'z2':z2,
            'flag':True
        }
        return render(request, 'mathematics/cross_product.html', context)
    else:
        return render(request, 'mathematics/cross_product.html', {'x1':2, 'y1':4, 'z1':6, 'x2':7, 'y2':9, 'z2':12 })



def spherical_coordinates(request):
    # to check for float values in input
    def check_decimal_values(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    # conversion
    def convert_to_radian(value, unit):
        if unit == 'deg':
            value = value * 0.0174533
        elif unit == 'gon':
            value = value * 0.015708
        elif unit == 'mrad':
            value = value * 0.001
        elif unit == 'μrad':
            value = value * 0.000001
        elif unit == 'arcmin':
            value = value * 0.000290888
        elif unit == 'arcsec':
            value = value * 0.0000048501
        elif unit == 'tr':
            value = value * 6.28319
        return value

    def convert_radian_to_other(valueinradian):
        all_conversions_string = {
            "value in degree": str(round((valueinradian * 57.2958), 5)) + " deg",
            "value in radian": str(valueinradian) + " rad",
            "value in gradians": str(round((valueinradian * 63.662), 5)) + " gon",
            "value in turns": str(round((valueinradian * 0.159155), 5)) + " tr",
            "value in arcmin": str(round((valueinradian * 3437.75), 5)) + " arcmin",
            "value in arcsec": str(round((valueinradian * 206265), 5)) + " arcsec",
            "value in mrad": str(round((valueinradian * 1000), 5)) + " mrad",
            "value in microrad": str(round((valueinradian * 1000000), 5)) + " μrad"
        }
        return all_conversions_string

    if request.method == 'POST':
        given = request.POST.get('given')
        x = request.POST.get('x')
        y = request.POST.get('y')
        z = request.POST.get('z')

        r = request.POST.get('r')
        t = request.POST.get('t')
        t1 = request.POST.get('t1')

        t_op = request.POST.get('t_op')
        t1_op = request.POST.get('t1_op')

        if given == 'form1' and x and y and z:
            x = check_decimal_values(x)
            y = check_decimal_values(y)
            z = check_decimal_values(z)

            # r = √(x² + y² + z²)
            r_result = math.sqrt(x**2 + y**2 + z**2)

            # θ = arccos(z / r)
            a = z/r_result
            print("--------a",a)
            t_result = math.acos(a)
            print("--------anglea", t_result)

            # φ = arctan(y / x)

            if x == 0:
                if y < 0:
                    t1_result = -1.5708
                else:
                    t1_result = 1.5708
            else:
                b = y/x
                t1_result = math.atan(b)
            print("--------angleb", t1_result)

            all_conversions_angle1 = convert_radian_to_other(t_result)
            all_conversions_angle2 = convert_radian_to_other(t1_result)

            # answer in degree
            tresult = round((t_result * 57.2958), 4)
            t1result = round((t1_result * 57.2958), 4)

            # round off
            r_result = round(r_result, 4)

            context = {'x': x, 'y': y, 'z': z, 'r':r, 'given':given,
                       'r_result': r_result, 't_result': tresult, 't1_result': t1result,
                       'all_conversions_angle1':all_conversions_angle1,
                       'all_conversions_angle2': all_conversions_angle2,

                       'flag1': True

                       }
            return render(request, 'mathematics/spherical_coordinates.html', context)

        elif given == 'form2' and t and t1 and r and t1_op and t_op:
            r = check_decimal_values(r)
            t = check_decimal_values(t)
            t1 = check_decimal_values(t1)

            if t_op != 'rad':
                t_in_rad = convert_to_radian(t, t_op)
            else:
                t_in_rad = t

            if t1_op != 'rad':
                t1_in_rad = convert_to_radian(t1, t1_op)
            else:
                t1_in_rad = t1

            x = r * math.sin(t_in_rad) * math.cos(t1_in_rad)
            y = r * math.sin(t_in_rad) * math.sin(t1_in_rad)
            z = r * math.cos(t_in_rad)

            # roung off
            x = round(x, 5)
            y = round(y, 5)
            z = round(z, 5)


            context = {
                'r':r, 't':t, 't1':t1,
                'x_result':x,'y_result':y, 'z_result':z, 't_op':t_op, 't1_op':t1_op,
                'given':given,'flag2':True

            }

            return render(request, 'mathematics/spherical_coordinates.html', context)
        return render(request, 'mathematics/spherical_coordinates.html', {'given':given})
    else:
        return render(request, 'mathematics/spherical_coordinates.html', {'given':'form1', 'x':4, 'y':6, 'z':9 })


def average_rate_of_change(request):

    # to check for float values in input
    def check_decimal_values(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        x1 = request.POST.get('x1')
        fx1 = request.POST.get('fx1')
        x2 = request.POST.get('x2')
        fx2 = request.POST.get('fx2')


        # A = [f(x2) - f(x1)] / [x2 - x1]
        x1 = check_decimal_values(x1)
        fx1 = check_decimal_values(fx1)
        x2 = check_decimal_values(x2)
        fx2 = check_decimal_values(fx2)


        if x2 - x1 == 0:
            messages.error(request, 'You entered the same coordinates twice.'
                                    ' It is not possible to calculate the average rate of change.')
            return render(request, 'mathematics/average_rate_of_change.html',{'x1':x1, 'fx1':fx1, 'x2':x2, 'fx2':fx2} )


        a_result = (fx2 - fx1)/(x2 - x1)
        a_result = round(a_result, 5)

        context = {'x1':x1, 'fx1':fx1, 'x2':x2, 'fx2':fx2,
                       'a_result':a_result,'flag':True}

        return render(request, 'mathematics/average_rate_of_change.html', context)

    else:
        return render(request, 'mathematics/average_rate_of_change.html',
                      {'x1':2, 'fx1':4, 'x2':5, 'fx2':9, })


def cylindrical_coordinates(request):

    # to check for float values in input
    def check_decimal_values(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

        # conversion

    def convert_to_radian(value, unit):
        if unit == 'deg':
            value = value * 0.0174533
        elif unit == 'gon':
            value = value * 0.015708
        elif unit == 'mrad':
            value = value * 0.001
        elif unit == 'μrad':
            value = value * 0.000001
        elif unit == 'arcmin':
            value = value * 0.000290888
        elif unit == 'arcsec':
            value = value * 0.0000048501
        elif unit == 'tr':
            value = value * 6.28319
        return value

    def convert_radian_to_other(valueinradian):
        all_conversions_string = {
            "value in degree": str(round((valueinradian * 57.2958), 5)) + " deg",
            "value in radian": str(valueinradian) + " rad",
            "value in gradians": str(round((valueinradian * 63.662), 5)) + " gon",
            "value in turns": str(round((valueinradian * 0.159155), 5)) + " tr",
            "value in arcmin": str(round((valueinradian * 3437.75), 5)) + " arcmin",
            "value in arcsec": str(round((valueinradian * 206265), 5)) + " arcsec",
            "value in mrad": str(round((valueinradian * 1000), 5)) + " mrad",
            "value in microrad": str(round((valueinradian * 1000000), 5)) + " μrad"
        }
        return all_conversions_string

    if request.method =='POST':

        given = request.POST.get('given')
        x = request.POST.get('x')
        y = request.POST.get('y')
        z1 = request.POST.get('z1')

        r = request.POST.get('r')
        t = request.POST.get('t')
        z3 = request.POST.get('z3')

        t_op = request.POST.get('t_op')


        if given == 'form1' and x and y and z1:
            x = check_decimal_values(x)
            y = check_decimal_values(y)
            z1 = check_decimal_values(z1)

            # r = √(x² + y²)
            r_result = math.sqrt(x**2 + y**2)

            # θ = arctan(y / x)
            if x == 0:
                if y < 0:
                    t_result_in_deg = -90
                else:
                    t_result_in_deg = 90
                t_result = convert_to_radian(t_result_in_deg, 'deg')
            else:
                t_result = numpy.arctan(y/x)
                t_result_in_deg = round((t_result * 57.2958), 5)

            all_conversions = convert_radian_to_other(t_result)

            # z₂ = z₁
            z2_result = z1

            # rounf off
            r_result = round(r_result, 5)
            t_result_in_deg = round(t_result_in_deg, 5)

            context = {
                'x':x, 'y':y,'z1':z1,'given':given,
                'r_result':r_result, 't_result_in_deg':t_result_in_deg, 'z2_result':z2_result,
                'all_conversions':all_conversions, 'flag1':True,
            }
            return render(request, 'mathematics/cylindrical_coordinates.html', context)

        elif given == 'form2' and r and t and z3 and t_op:
            r = check_decimal_values(r)
            t = check_decimal_values(t)
            z3 = check_decimal_values(z3)

            # convert t_op into radian
            t_in_rad = convert_to_radian(t, t_op)

            # x = ρ * cosθ
            x_result = r * math.cos(t)

            # y = ρ * sinθ
            y_result = r * math.sin(t)

            # z₁ = z
            z3_result = z3

            # round off values
            x_result = round(x_result, 5)
            y_result = round(y_result, 5)

            context = {
                'r': r, 't': t, 'z3': z3,'t_op':t_op,'given':given,
                'x_result': x_result, 'y_result': y_result, 'z3_result': z3_result,
               'flag2': True,
            }
            return render(request, 'mathematics/cylindrical_coordinates.html',context)
        return render(request, 'mathematics/cylindrical_coordinates.html', {'given':given})


    else:
        return render(request, 'mathematics/cylindrical_coordinates.html', {'given':'form1', 'x':2,'y':5,'z1':9} )



def distance_3d(request):
    # to check for float values in input
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        x1 = request.POST.get('x1')
        y1 = request.POST.get('y1')
        z1 = request.POST.get('z1')
        x2 = request.POST.get('x2')
        y2 = request.POST.get('y2')
        z2 = request.POST.get('z2')

        x1 = check_decimal(x1)
        y1 = check_decimal(y1)
        z1 = check_decimal(z1)
        x2 = check_decimal(x2)
        y2 = check_decimal(y2)
        z2 = check_decimal(z2)

        mid_x = x2-x1
        mid_y = y2-y1
        mid_z = z2-z1

        mid_sol = mid_x**2 + mid_y**2 + mid_z**2
        d_sol = math.sqrt(mid_sol)
        d_sol = round(d_sol, 5)



        context = {
            'x1': x1, 'y1': y1, 'z1': z1, 'x2': x2, 'y2': y2, 'z2': z2,
            'mid_x':mid_x, 'mid_y':mid_y, 'mid_z':mid_z,
            'mid_sol':mid_sol, 'd_sol':d_sol,
            'flag': True
        }
        return render(request, 'mathematics/distance_3d.html', context)

    else:
        context ={
            'x1': 2, 'y1': 6, 'z1': 9, 'x2': 4, 'y2': 13, 'z2':8,
        }
        return render(request, 'mathematics/distance_3d.html', context)


def work_combine(request):
    from fractions import Fraction

    # to check for float values in input
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    def gcf(n1, n2):
        if n1 == n2:
            return n1
        # elif n1 > n2:
        #     small = n2
        # else:
        #     small = n1
        divi = n1
        div = n2
        rem = divi%div
        # print("rem----",rem)

        while rem != 0:
            divi = div
            div = rem
            rem = divi % div

        return div


    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')

        a = check_decimal(a)
        b = check_decimal(b)

        if a <= 0 or b <= 0:
            messages.error(request, 'Enter the valid values:')
            return render(request, 'mathematics/work_combine.html', )


        num1, num2 = 1, 1
        denom1, denom2 = a, b
        print("a------b",a, b)

        is_two_no_equal = None

        if a != b:
            mid_numerator1 = num1*denom2
            mid_numerator2 = num2*denom1
            print("mid nums --------", mid_numerator1, mid_numerator2)
            total_numerator = mid_numerator1 + mid_numerator2
            total_denominator = denom1 * denom2
            print("total num and demon---------", total_numerator, total_denominator)
            is_two_no_equal = False


        else:
            mid_numerator1 = 1
            mid_numerator2 = 1
            total_numerator = 2
            total_denominator = a

            is_two_no_equal = True

        # can_fraction_simplify = Fraction(total_numerator, total_denominator)
        # print(" can_fraction_simplify-------------", can_fraction_simplify, type(can_fraction_simplify))

        gcf = gcf(total_numerator, total_denominator)
        print("gfg-------------",gcf)

        is_gcf_available = None
        if isinstance(gcf, int) and gcf != 1:
            is_gcf_available = True

            new_numerator = total_numerator // gcf
            new_denominator = total_denominator // gcf

        else:
            new_numerator = total_numerator
            new_denominator = total_denominator


        #
        # if gcf == 1:
        #     is_gcdf_1 = True
        # elif type(gcf) == 'int':
        #     is_gcdf_1 = False



        # new_fraction = can_fraction_simplify
        # print("new num and denom--------",new_numerator,new_denominator )

        mid_min_ans = 60 * new_denominator
        min_final_ans = mid_min_ans/new_numerator

        # conversion in hours
        total_minutes = min_final_ans

        # Get hours with floor division
        hours = total_minutes // 60

        minutes = total_minutes % 60
        minutes = round(minutes, 4)

        ans_in_hour = "{} hours, {} minutes".format(hours, minutes)

        # round off
        min_final_ans = round(min_final_ans, 4)
        context = {
            'a':a, 'b':b, 'num1':num1, 'num2':num2,
            'denom1':denom1, 'denom2':denom2,
            'mid_numerator1':mid_numerator1, 'mid_numerator2':mid_numerator2,
            'total_numerator':total_numerator, 'total_denominator':total_denominator,
            'gcf':gcf, 'mid_min_ans':mid_min_ans,
            'new_denominator':new_denominator, 'new_numerator':new_numerator,
            # 'new_fraction': new_fraction,
            'min_final_ans':min_final_ans,
            'ans_in_hour':ans_in_hour,
            'is_two_no_equal':is_two_no_equal, 'is_gcf_available':is_gcf_available,
            'flag':True
        }
        return render(request, 'mathematics/work_combine.html', context)


    else:
        return render(request, 'mathematics/work_combine.html', {'a':4, 'b':7, 'flag':False} )


def hyperbola(request):
    # to check for float values in input
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        num1 = check_decimal(request.POST.get('num1'))
        num2 = check_decimal(request.POST.get('num2'))
        denom1 = check_decimal(request.POST.get('denom1'))
        denom2 = check_decimal(request.POST.get('denom2'))
        rhs = check_decimal(request.POST.get('rhs'))


        first_choice = request.POST.get('first_choice')
        second_choice = request.POST.get('second_choice')

        print("initial inputs---------------", num1, num2, denom1, denom2, first_choice, second_choice , rhs)

        # difference check
        maximum_of_3 = max(num1, num2, rhs)
        print("maximum of 3---------",maximum_of_3)

        denom_out_1 = num1/(denom1 * maximum_of_3)
        denom_out_2 = num2/(denom2 * maximum_of_3)
        rhs_out_1 = rhs/maximum_of_3

        print("After applying maximum variable---denom_out_1-------denom_out_2----rhs_out_1-----", denom_out_1, denom_out_2, rhs_out_1)

        # calculation of a, b
        a = math.sqrt(denom_out_1) #a
        b = math.sqrt(denom_out_2) #b

        sqr_sqrt1 = pow(a,2)
        sqr_sqrt2 = pow(b, 2)

        sum_of_sqr_sqrt = sqr_sqrt1 + sqr_sqrt2
        c = math.sqrt(sum_of_sqr_sqrt)  #sqrt_sum

        eccentricity = c/a

        num_of_lr = 2*sqr_sqrt2
        result_lr = num_of_lr/a
        print(" l ------r-----",result_lr)

        semi_lr_result = result_lr/2


        context = {
            'num1': num1, 'num2': num2, 'denom1': denom1, 'denom2': denom2, 'rhs':rhs,
            'first_choice': first_choice, 'second_choice': second_choice,
            'maximum_of_3':maximum_of_3,
            'denom_out_1':denom_out_1, 'denom_out_2':denom_out_2, 'rhs_out_1':rhs_out_1,

            'a':a, 'b':b,
            'sqr_sqrt1':sqr_sqrt1, 'sqr_sqrt2':sqr_sqrt2,

            'sum_of_sqr_sqrt':sum_of_sqr_sqrt,'c':c,
            'eccentricity':eccentricity,

            'num_of_lr':num_of_lr, 'result_lr':result_lr,

            'semi_lr_result':semi_lr_result,

            'flag': True
        }
        return render(request, 'mathematics/hyperbola.html', context)

    else:
        context = {
            'num1':2, 'num2':4, 'denom1':5, 'denom2':6, 'rhs':9,
        }
        return render(request, 'mathematics/hyperbola.html', context)


def parallel_resistor(request):

    # to check for float values in input
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    # ohm converter
    def ohm_converter(value, op):
        if op == 'moh':
            return value * 0.0001
        elif op == 'koh':
            return value * 1000
        elif op == 'megaoh':
            return value * 1000000
        else:
            return value

    if request.method == 'POST':
        given = request.POST.get('given')
        nor = check_decimal(request.POST.get('nor'))
        print("nor ------------------------------------------", nor)

        er1 = request.POST.get('er1')
        er2 = request.POST.get('er2')
        er3 = request.POST.get('er3')
        er4 = request.POST.get('er4')
        er5 = request.POST.get('er5')

        er1_op = request.POST.get('er1_op')
        er2_op = request.POST.get('er2_op')
        er3_op = request.POST.get('er3_op')
        er4_op = request.POST.get('er4_op')
        er5_op = request.POST.get('er5_op')

        mr1 = request.POST.get('mr1')
        mr2 = request.POST.get('mr2')
        mr3 = request.POST.get('mr3')
        mr4 = request.POST.get('mr4')
        mr5 = request.POST.get('mr5')

        mr1_op = request.POST.get('mr1_op')
        mr2_op = request.POST.get('mr2_op')
        mr3_op = request.POST.get('mr3_op')
        mr4_op = request.POST.get('mr4_op')
        mr5_op = request.POST.get('mr5_op')

        dtr_op = request.POST.get('dtr_op')
        dtr = request.POST.get('dtr')
        print("dtr -     ---            ----- ------", dtr, dtr_op)


        if given == 'form1':
            print("-----------++((((------", er1, er2, er3, er4, er5)
            total = 0
            if er1 :
                er1 = check_decimal(er1)
                t_er1 = ohm_converter(er1, er1_op)
                total += (1/t_er1)
            if er2 :
                er2 = check_decimal(er2)
                t_er2 = ohm_converter(er2, er2_op)
                total += (1/t_er2)
            if er3 :
                er3 = check_decimal(er3)
                t_er3 = ohm_converter(er3, er3_op)
                total += (1/t_er3)
            if er4 :
                er4 = check_decimal(er4)
                t_er4 = ohm_converter(er4, er4_op)
                total += (1/t_er4)
            if er5 :
                er5 = check_decimal(er5)
                t_er5 = ohm_converter(er5, er5_op)
                total += (1/t_er5)

            # if nor == 1:
            #     total = (1/er1)
            # elif nor == 2:
            #     total = (1/er1)+ (1/er2)
            # elif nor == 3:
            #     total = (1/er1)+ (1/er2)+ (1/er3)
            # elif nor == 4:
            #     total = (1/er1)+ (1/er2)+ (1/er3) +(1/er4)
            # elif nor == 5:
            #     total = (1 / er1) + (1 / er2) + (1 / er3) + (1 / er4) + (1/er5)

            if er1 :
                er_result = 1/total
                t_total = round(total, 5)
                print("total----------------",total)

                # er_result = power_raise(er_result)
                # print("er_total---------------------------------", er_result)
                # er_result = round(er_result, 4)

                context = {
                    'er1':er1, 'er2':er2, 'er3':er3, 'er4':er4, 'er5':er5,
                    # 't_er1':t_er1, 't_er2':t_er2, 't_er3':t_er3, 't_er4':t_er4, 't_er5':t_er5,
                    'er1_op': er1_op, 'er2_op': er2_op, 'er3_op': er3_op, 'er4_op': er4_op, 'er5_op': er5_op,
                    'total':total, 'er_result':er_result, 'flag1':True,
                    'nor':nor,'given':given,
                }

                return render(request, 'mathematics/parallel_resistor.html',context )

            context = {
                'er1': er1, 'er2': er2, 'er3': er3, 'er4': er4, 'er5': er5,
                'er1_op': er1_op, 'er2_op': er2_op, 'er3_op': er3_op, 'er4_op': er4_op, 'er5_op': er5_op,
                'nor': nor, 'given': given,
            }
            return render(request, 'mathematics/parallel_resistor.html', context )

        if given == 'form2' and dtr:
            total = 0
            if mr1:
                mr1 = check_decimal(mr1)
                t_mr1 = ohm_converter(mr1, mr1_op)
                total += (1 / t_mr1)
            if mr2:
                mr2 = check_decimal(mr2)
                t_mr2 = ohm_converter(mr2, mr2_op)
                total += (1 / t_mr2)
            if mr3:
                mr3 = check_decimal(mr3)
                t_mr3 = ohm_converter(mr3, mr3_op)
                total += (1 / t_mr3)
            if mr4:
                mr4 = check_decimal(mr4)
                t_mr4 = ohm_converter(mr4, mr4_op)
                total += (1 / t_mr4)
            if mr5:
                mr5 = check_decimal(mr5)
                t_mr5 = ohm_converter(mr5, mr5_op)
                total += (1 / t_mr5)

            if mr1:
                t_dtr = check_decimal(dtr)
                t_dtr = ohm_converter(t_dtr, dtr_op)
                r_dtr = 1/t_dtr
                result_dtr = -(1/(total - r_dtr))
                print("result dttr -------------------------------",result_dtr)
                result_dtr_rounded = round(result_dtr, 5)

                context = {
                    'mr1': mr1, 'mr2': mr2, 'mr3': mr3, 'mr4': mr4, 'mr5': mr5,
                    'mr1_op': mr1_op, 'mr2_op': mr2_op, 'mr3_op': mr3_op, 'mr4_op': mr4_op, 'mr5_op': mr5_op,
                    'total': total,'flag2': True,
                    'dtr': dtr, 'dtr_op': dtr_op,
                    'nor': nor, 'given': given,'result_dtr':result_dtr
                }
                return render(request, 'mathematics/parallel_resistor.html', context)

        context = {
            'er1': er1, 'er2': er2, 'er3': er3, 'er4': er4, 'er5': er5,
            'er1_op': er1_op, 'er2_op': er2_op, 'er3_op': er3_op, 'er4_op': er4_op, 'er5_op': er5_op,
            'mr1': mr1, 'mr2': mr2, 'mr3': mr3, 'mr4': mr4, 'mr5': mr5,
            'mr1_op': mr1_op, 'mr2_op': mr2_op, 'mr3_op': mr3_op, 'mr4_op': mr4_op, 'mr5_op': mr5_op,
            'nor': nor,'given':given, 'dtr':dtr, 'dtr_op':dtr_op
        }
        
        return render(request, 'mathematics/parallel_resistor.html', context)

    else:
            return render(request, 'mathematics/parallel_resistor.html', {'given':'form1', 'nor':2})


def velocity_addition(request):
    # to check for float values in input
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

        # convertor

    def meterconverter(lenn, lentype):
        if lentype == 'km/s':
            m = lenn * 1000
        elif lentype == 'mi/s':
            m = lenn * 1609.34
        elif lentype == 'c':
            m = lenn * 299792458
        else:
            m = lenn
        return m

    if request.method == 'POST':
        sv = request.POST.get('sv')
        pv = request.POST.get('pv')
        rpv = request.POST.get('rpv')

        sv_op = request.POST.get('sv_op')
        pv_op = request.POST.get('pv_op')
        rpv_op = request.POST.get('rpv_op')

        given = request.POST.get('given')

        if given =='form1' and pv and sv:
            sv = check_decimal(sv)
            pv = check_decimal(pv)

            t_pv = meterconverter(pv, pv_op)
            t_sv = meterconverter(sv, sv_op)

            if (t_pv > 299792458 or t_sv > 299792458):
                messages.error(request, 'The speed of the projectile can not exceed the speed of light')
                return render(request, 'mathematics/velocity_addition.html', {'given': given, 'sv': sv, 'sv_op': sv_op, 'pv': pv, 'pv_op': pv_op})

            rpv_mid_num = t_sv + t_pv
            rpv_sec_num = t_sv * t_pv
            rpv_sqr_of_c = math.pow(299792458, 2)
            rpv_result = rpv_mid_num /( 1 + (rpv_sec_num/rpv_sqr_of_c) )
            rpv_result = round(rpv_result, 10)

            context = {
                'given':given, 'sv':sv, 'pv':pv, 'sv_op':sv_op, 'pv_op':pv_op,
                'rpv_result':rpv_result, 'rpv_mid_num':rpv_mid_num,
                'rpv_sqr_of_c':rpv_sqr_of_c,
                'flag1':True,
            }
            return render(request, 'mathematics/velocity_addition.html', context)

        # u = (v + w) / (1 + (v * w) / c²)
        # w = c² (u - v) / (c2 - u*v)
        if given == 'form2' and rpv and sv:
            rpv = check_decimal(rpv)
            sv = check_decimal(sv)

            t_rpv = meterconverter(rpv, rpv_op)
            t_sv = meterconverter(sv, sv_op)

            if (t_rpv > 299792458 or t_sv > 299792458):
                messages.error(request, 'The speed of the projectile can not exceed the speed of light')
                return render(request, 'mathematics/velocity_addition.html', {'given': given, 'rpv': rpv, 'rpv_op': rpv_op, 'sv': sv, 'sv_op': sv_op})

            pv_num = t_rpv - t_sv
            pv_denom = t_rpv * t_sv

            pv_sqr_of_c = math.pow(299792458, 2)
            pv_result = (pv_sqr_of_c * pv_num)/(pv_sqr_of_c - pv_denom)
            pv_result = round(pv_result, 10)

            context = {
                'given': given, 'rpv': rpv, 'sv': sv, 'rpv_op': rpv_op, 'sv_op': sv_op,
                'pv_result': pv_result, 'pv_num': pv_num, 'pv_denom':pv_denom,
                'pv_sqr_of_c': pv_sqr_of_c,
                'flag2': True,
            }

            return render(request, 'mathematics/velocity_addition.html', context)

        # u = (v + w) / (1 + (v * w) / c²)
        # v = c² (u - w) / (c² - u*w)
        if given == 'form3' and rpv and pv:
            rpv = check_decimal(rpv)
            pv = check_decimal(pv)
            print()

            t_pv = meterconverter(pv, pv_op)
            t_rpv = meterconverter(rpv, rpv_op)

            if(t_pv > 299792458 or t_rpv > 299792458 ):
                print(" entered in errorpart---------------------------------------------")
                messages.error(request, 'The speed of the projectile can not exceed the speed of light')
                return render(request, 'mathematics/velocity_addition.html', {'given':given, 'rpv':rpv, 'rpv_op':rpv_op, 'pv':pv, 'pv_op':pv_op })


            sv_num = t_rpv - t_pv
            sv_denom = t_rpv * t_pv

            sv_sqr_of_c = math.pow(299792458, 2)
            sv_result = (sv_sqr_of_c * sv_num) / (sv_sqr_of_c - sv_denom)

            sv_result = round(sv_result, 10)
            context = {
                'given': given, 'rpv': rpv, 'pv': pv,  'rpv_op': rpv_op, 'pv_op': pv_op,
                'sv_result': sv_result, 'sv_num': sv_num, 'sv_denom':sv_denom,
                'sv_sqr_of_c': sv_sqr_of_c,
                'flag3': True,
            }
            return render(request, 'mathematics/velocity_addition.html', context)

        context = {
            'given': given, 'rpv': rpv, 'pv': pv,'sv': sv, 'rpv_op': rpv_op, 'pv_op': pv_op, 'sv_op': sv_op,
        }
        return render(request, 'mathematics/velocity_addition.html', context)

    else:
        return render(request, 'mathematics/velocity_addition.html', {'given': 'form1', 'sv':1, 'pv':1, 'rpv':1})


def spherical_capacitor(request):

    # convertor
    def meterconverter(lentype, lenn):
        if lentype == 'km':
            m = lenn * 1000
        elif lentype == 'mm':
            m = lenn / 1000
        elif lentype == 'cm':
            m = lenn / 100.0
        elif lentype == 'in':
            m = lenn / 39.37
        elif lentype == 'ft':
            m = lenn / 3.28084
        elif lentype == 'yd':
            m = lenn / 1.094
        elif lentype == 'mi':
            m = lenn * 1609
        else:
            m = lenn
        return m

    def faradconverter(t, l):
        if t == "nf":
            l = l / 1000000000
        elif t == "uf":
            l = l / 1000000
        elif t == "pf":
            l = l / 1000000000000
        elif t == "mf":
            l = l / 1000
        else:
            l = l


    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    def convert_farad_to_other(r):
        all_conversions_string = {
            "value in farad": str(r) + "farads(F)",
            "value in milifarad": str((round((r * 1000), 10)) )+ " milifarad(mF)",
            "value in microfarad": str(round((r * 1000000), 10)) + " microfards(μF)",
            "value in nanofarad": str(round((r * 1000000000), 10)) + " nanofarads(nF)",
            "value in picofarad": str(round((r * 1000000000000), 10)) + " picofarads(pF)",

        }
        return all_conversions_string

    if request.method == 'POST':
        isr = request.POST.get('isr')
        isr_op = request.POST.get('isr_op')
        osr = request.POST.get('osr')
        osr_op = request.POST.get('osr_op')

        print("-------", isr, isr_op, osr, osr_op)

        isr = check_decimal(isr)
        osr = check_decimal(osr)

        isr_in_m = meterconverter(isr_op,isr)
        osr_in_m = meterconverter(osr_op,osr)
        print("in meters-------", isr_in_m, osr_in_m)
        if(isr_in_m >= osr_in_m):
            context = {
                'isr':isr,
                'osr':osr,
                'isr_op':isr_op,
                'osr_op':osr_op,
            }
            messages.error(request, 'outer radius must be greater than inner radius')
            return render(request,  'mathematics/spherical_capacitor.html', context)

        if (isr== 0 or osr == 0):
            context = {
                'isr': isr,
                'osr': osr,
                'isr_op': isr_op,
                'osr_op': osr_op,
            }
            messages.error(request, '0 input will give 0 output')
            return render(request, 'mathematics/spherical_capacitor.html', context)

        # C = 4 * π * ε0 * εk / (1 / a - 1 /  , 8.85 × 10^(−12) F/m
        result = (4 * math.pi * 8.85* math.pow(10, -12)* 1 )/((1/isr_in_m) - (1/osr_in_m))
        result = round(result, 12)

        all_conversions = convert_farad_to_other(result)

        context ={
            'flag':True,
            'result':result,
            'isr': isr,
            'osr': osr,
            'isr_op': isr_op,
            'osr_op': osr_op,
            'all_conversions':all_conversions
        }
        return render(request, 'mathematics/spherical_capacitor.html', context)

    else:
        return render(request, 'mathematics/spherical_capacitor.html', {'isr':4, 'osr':5})


def resonant_frequecy(request):

    if request.method == 'POST':
        pass
    else:
        return render(request, 'mathematics/resonant_frequency.html')




def quarter_mile(request):

    # check for decimal digits
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    # power to metric horsepower
    def powerConverter(val, op):
        if op == 'w':
            value = val * 0.00135962
        elif op == 'kw':
            value = val * 1.35962
        elif op == 'mw':
            value = val * 1359.62
        elif op == 'hpl':
            value = val * 1.01
        elif op == 'hpm':
            value = val * 1.01
        return value

    # weight converter
    def wtconverter_to_pounds(val, op):
        if op == 'kg':
            value = val * 2.20462
        elif op == 'US tons':
            value = val * 2000
        elif op == 't':
            value = val * 2204.6226218
        elif op == 'Long tons':
            value = val * 2240
        elif op == 'lb':
            value = val
        return value

    def sec_to_other_units(r):
        all_conversions_string = {
            "ET in seconds": str(r) + " seconds(sec)",
            "ET in minutes": str((round((r * 0.0166667), 5)) )+ " minutes(min)",
            "ET in hours": str(round((r * 0.000277778), 5)) + " hours(hr)",
        }
        return all_conversions_string

    def hpm_to_other_units(r):
        all_conversions_string = {
            "value in miles per hour": str(r) + " mph",
            "value in meters per second": str((round((r * 0.44704), 5)) )+ " meters per seconds(m/s)",
            "value in kilometers per hour": str(round((r * 1.60934), 5)) + " kilometer per hour(km/h)",
            "value in feet per second": str(round((r * 1.46667), 5)) + " feet per second(ft/s)",
        }
        return all_conversions_string

    if request.method == 'POST':
        given = request.POST.get('given')
        weight = request.POST.get('weight')
        wt_op = request.POST.get('wt_op')

        power = request.POST.get('power')
        pv_op = request.POST.get('pv_op')

        if power and check_decimal(power)==0:
            messages.error(request, 'Elepsed time = infinity and Trap speed = 0 (in these inputs) try something else ')
            context = {
                'given': given,
                'weight': weight, 'wt_op': wt_op,
                'power': power, 'pv_op': pv_op,
            }
            return render(request, 'mathematics/quarter_mile.html', context)

        if weight and check_decimal(weight)==0:
            messages.error(request, 'Elepsed time = 0 and Trap speed = Infinity(in these inputs) try something else ')
            context = {
                'given': given,
                'weight': weight, 'wt_op': wt_op,
                'power': power, 'pv_op': pv_op,
            }
            return render(request, 'mathematics/quarter_mile.html', context)


        if given == 'form1' and weight and power:

            weight = check_decimal(weight)
            power = check_decimal(power)

            weight_in_pounds = round(wtconverter_to_pounds(weight, wt_op),5)
            power_in_hpm = round(powerConverter(power, pv_op), 5)

            # ET = 6.290 * (weight / power)¹ᐟ³
            div_of_wt_pow = weight_in_pounds / power_in_hpm
            elapsed_time = 6.290 * math.pow((div_of_wt_pow), 1/3)

            # final speed = 224 * (power / weight)¹ᐟ³
            div_of_pow_wt = power_in_hpm/weight_in_pounds
            final_speed = 224 * math.pow(div_of_pow_wt, 1/3)

            # rounding off
            elapsed_time = round(elapsed_time, 5)
            final_speed = round(final_speed, 5)
            div_of_wt_pow = round(div_of_wt_pow, 5)

            coversionSecToOther = sec_to_other_units(elapsed_time)
            conversionHpmToOther = hpm_to_other_units(final_speed)
            context = {
                'given': given,
                'weight': weight, 'wt_op': wt_op,
                'power': power, 'pv_op': pv_op,
                'div_of_wt_pow': div_of_wt_pow, 'elapsed_time': elapsed_time,
                'div_of_pow_wt': div_of_pow_wt, 'final_speed': final_speed,
                'coversionSecToOther':coversionSecToOther,
                'conversionHpmToOther': conversionHpmToOther,
                'flag1': True,
            }
            return render(request, 'mathematics/quarter_mile.html', context)

        elif given == 'form2' and weight and power:

            weight = check_decimal(weight)
            power = check_decimal(power)

            weight_in_pounds = round(wtconverter_to_pounds(weight, wt_op),5)
            power_in_hpm = round(powerConverter(power, pv_op), 5)


            # ET = 6.269 * (weight / power)¹ᐟ³
            div_of_wt_pow = weight_in_pounds / power_in_hpm
            elapsed_time = 6.269 * math.pow((div_of_wt_pow), 1/3)

            # final speed = 230 * (power / weight)¹ᐟ³
            div_of_pow_wt = power_in_hpm / weight_in_pounds
            final_speed = 230 * math.pow(div_of_pow_wt, 1/3)

            # rounding off
            elapsed_time = round(elapsed_time, 5)
            final_speed = round(final_speed, 5)
            div_of_wt_pow = round(div_of_wt_pow, 5)

            coversionSecToOther = sec_to_other_units(elapsed_time)
            conversionHpmToOther = hpm_to_other_units(final_speed)

            context = {
                'given': given,
                'weight': weight, 'wt_op': wt_op,
                'power': power, 'pv_op': pv_op,
                'div_of_wt_pow': div_of_wt_pow, 'elapsed_time': elapsed_time,
                'div_of_pow_wt': div_of_pow_wt, 'final_speed': final_speed,
                'coversionSecToOther': coversionSecToOther,
                'conversionHpmToOther': conversionHpmToOther,
                'flag2': True,
            }
            return render(request, 'mathematics/quarter_mile.html', context)

        elif given == 'form3' and weight and power:

            weight = check_decimal(weight)
            power = check_decimal(power)

            weight_in_pounds = round(wtconverter_to_pounds(weight, wt_op),5)
            power_in_hpm = round(powerConverter(power, pv_op), 5)


            # ET = 5.825 * (weight / power)¹ᐟ³
            div_of_wt_pow = weight_in_pounds / power_in_hpm
            elapsed_time = 5.825 * math.pow((div_of_wt_pow), 1/3)


            # final speed = 234 * (power / weight)¹ᐟ³
            div_of_pow_wt = power_in_hpm / weight_in_pounds
            final_speed = 234 * math.pow(div_of_pow_wt, 1/3)

            #rounding off
            elapsed_time = round(elapsed_time, 5)
            final_speed = round(final_speed, 5)
            div_of_wt_pow = round(div_of_wt_pow, 5)

            coversionSecToOther = sec_to_other_units(elapsed_time)
            conversionHpmToOther = hpm_to_other_units(final_speed)
            context = {
                'given': given,
                'weight': weight, 'wt_op': wt_op,
                'power': power, 'pv_op': pv_op,
                'div_of_wt_pow': div_of_wt_pow, 'elapsed_time': elapsed_time,
                'div_of_pow_wt': div_of_pow_wt, 'final_speed': final_speed,
                'coversionSecToOther': coversionSecToOther,
                'conversionHpmToOther':conversionHpmToOther,
                'flag3': True,
            }
            return render(request, 'mathematics/quarter_mile.html', context)

        context = {
            'given':given,
            # 'weight':weight, 'wt_op':wt_op,
            # 'power':power, 'pv_op':pv_op,
        }
        return render(request, 'mathematics/quarter_mile.html', context)
    else:
        return render(request, 'mathematics/quarter_mile.html', {'given':'form1', 'weight':20, 'power':10})



def affine_cipher(request):

    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    no_correspond_to_alphabet = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
        'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
        'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }

    key_list = list(no_correspond_to_alphabet.keys())
    print(" key list --------------", key_list)
    val_list = list(no_correspond_to_alphabet.values())
    print(" value list --------------", val_list)

    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'
                 'P','Q','R','S','T','U','V','W','X','Y','Z']

    def sum_using_formula(a, b, value_corr_to_alpha):
        mid_sum = a*value_corr_to_alpha
        final_sum = a*value_corr_to_alpha + b
        return mid_sum, final_sum

    mid_values = []
    final_values = []
    no_corres_to_alpha_values = []
    mod_values = []
    no_to_alpha_values = []


    if request.method == 'POST':

        str_input = request.POST.get('str_to_translate')
        a = request.POST.get('a')
        b = request.POST.get('b')

        a = check_decimal(a)
        b = check_decimal(b)


        number_of_letters = len(str_input) - str_input.count(" ")
        print("no count is----------",number_of_letters)

        count = 0
        itr_list = []
        str_without_spaces = ''
        for i in str_input:
            if i != ' ':
                str_without_spaces += i
                itr_list.append(count)
                count+=1


        for i in str_without_spaces:
            nca = ''
            final_sum = 0
            if i=='O' or i=='P' or (i in alphabets) :

                nca = no_correspond_to_alphabet.get(i, 0)
                no_corres_to_alpha_values.append(nca)
                # print("nca=-----i to number----type----------",i, nca, type(nca))

                mid_sum, final_sum = sum_using_formula(a, b, nca)
                mid_values.append(round(mid_sum,2))
                final_values.append(round(final_sum,2))

            else:
                no_corres_to_alpha_values.append('')
                mid_sum = 0
                final_sum = b
                mid_values.append(0)
                final_values.append(b)


            t = int(final_sum) % 26

            mod_values.append(round(t,2))

            # finding corresponding alphabet with the modulous answer
            no_to_alpha = key_list[val_list.index(t)]
            no_to_alpha_values.append(no_to_alpha)
        # print("---------------------------------------------------------------------------------------------------")

        print("no---------", no_corres_to_alpha_values)
        print("mid_values-", mid_values)
        print("fin_values-", final_values)
        print("mod_values-", mod_values)
        print("alpha------", no_to_alpha_values)
        print("len of array------------", len(no_to_alpha_values))
        print("iter list--------", itr_list)

        my_sol = zip(str_without_spaces, no_corres_to_alpha_values, mid_values, final_values, mod_values, no_to_alpha_values )

        context = {
            'str_to_translate': str_input,
            'a':a, 'b':b,
            'flag': True,
            'no_corres_to_alpha_values': no_corres_to_alpha_values,
            'mid_values': mid_values,
            'final_values': final_values,
            'mod_values': mod_values,
            'no_to_alpha_values': no_to_alpha_values,
            'number_of_letters':number_of_letters,
            'str_without_spaces':str_without_spaces,
            'my_sol':my_sol,
        }
        return render(request, 'mathematics/affine_cipher.html', context )


    else:
        strr = "AFFIN CIPHER"
        context = {
            'str_to_translate': strr,
            'a':3, 'b':8,
        }
        return render(request, 'mathematics/affine_cipher.html', context)



def find_both_numbers(request):
    from sympy import symbols, Eq, solve

    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        print("num1 and 2--------",num1, num2)

        num1 = check_decimal(num1)
        num2 = check_decimal(num2)

        p = -(num1)
        rearranged_eq_1 = f'x - y = {p}'
        # print("Rearanged equation no 1--------",rearranged_eq_1)
        rearranged_eq_2 = f'x + y = {num2}'

        x, y = symbols('x y')
        eq1 = Eq((num2 - y), 0) # x + y = 10 second eqation

        eq_after_sub_from_both_sides_str = f'x = {num2} - y'

        expr1 = Eq((x - y), 0)
        after_subs = expr1.subs(x, num2 -y)
        putting_x_in_sub = f' {num2} - y - y = {p}'

        expr2 = Eq((x - y), p)
        # print("expres 2 is:",expr2 )
        solve_for_y = expr2.subs(x, num2 - y)
        # print("solve_for_y:", solve_for_y)
        fin_solve_for_y = solve(solve_for_y, y)
        # print("fin------------------type", type(fin_solve_for_y), fin_solve_for_y)

        y_result = round(float(fin_solve_for_y[0]), 3)
        # print("y_ ",y_, type(y))
        print("output of y is : y result", fin_solve_for_y, y_result, type(y_result))
        y_is = f'y = {y_result}'

        eq_for_find_x = Eq((x - y), p)
        # print("eq_for_find_x:", eq_for_find_x)
        new_eq = eq_for_find_x.subs(y, y_result )
        # print("new equation s :", new_eq)
        final_result = solve(new_eq, x)
        # print("final xx is is ", final_result)

        final_result = round(float(final_result[0]), 3)
        eq_x_result = f'x = {final_result}'
        # print("final eq is ", eq_x_result)


        context = {
            'num1':num1, 'num2':num2,
            'p':p,
            'rearranged_eq_1':rearranged_eq_1,
            'rearranged_eq_2':rearranged_eq_2,
            'eq_after_sub_from_both_sides_str':eq_after_sub_from_both_sides_str,
            'putting_x_in_sub':putting_x_in_sub,
            'y_is':y_is,
            'y_result':y_result,
            'fin_solve_for_y':fin_solve_for_y,
            'eq_x_result':eq_x_result,
            'flag':True,
        }        

        return render(request, 'mathematics/find_both_numbers.html', context)

    else:
        return render(request, 'mathematics/find_both_numbers.html', {'num1':10, 'num2':18})



def cross_partition(request):
    open_list = ["[", "{"]
    close_list = ["]", "}"]

    # Function to check parentheses
    def check(myStr):
        stack = []
        for i in myStr:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((len(stack) > 0) and
                        (open_list[pos] == stack[len(stack) - 1])):
                    stack.pop()
                else:
                    return "Unbalanced"
            else:
                pass
        if len(stack) == 0:
            return False
        else:
            return True


    if request.method == 'POST':
        value_entered = request.POST.get('partition_entered')
        print("entered value is : ", value_entered)

        if check(value_entered):
            messages.error(request, 'Unbalanced brakets or parenthesis check again')
            return render(request, 'mathematics/cross_partition.html')

        # sq_brack = []
        # for i in value_entered:
        sq_brack = value_entered.split(']')
        print(sq_brack)

       
        return HttpResponse("Successful")


    return render(request, 'mathematics/cross_partition.html', {'partition_entered':'[{1,2,3},{2,3}][{3,4},{6,3,4}]'})









def markup(request):
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value    

    if request.method == 'POST':
        initial_price = request.POST.get('initial_price')
        final_price = request.POST.get('final_price')
        markup = request.POST.get('markup')
        given = request.POST.get('given')
        # print("given-------------", given)

        if given == 'form1' and final_price and markup:
            fin_price = check_decimal(final_price)
            mark_value = check_decimal(markup)

            markup_amt = fin_price
            one_plus_markup = 1 + mark_value/100
            orginal_price_output = markup_amt/one_plus_markup
            orginal_price_output = round(orginal_price_output, 2)

            context = {
                'given':given,'final_price':final_price, 'markup':markup,
                'markup_amt':markup_amt, 'one_plus_markup':one_plus_markup,
                'orginal_price_output':orginal_price_output,
                'flag1':True,
            }
            return render(request, 'mathematics/markup.html', context)
        
        elif given == 'form2' and final_price and initial_price:
            fin_price = check_decimal(final_price)
            init_price = check_decimal(initial_price)
           
            diff_fin_inital = fin_price - init_price
            x_output = diff_fin_inital/init_price
            percentage_output = 100 * x_output

            x_output = round(x_output, 2)
            percentage_output = round(percentage_output, 2)              

            context = {
                'given':given,'final_price':final_price, 'initial_price':initial_price,
                'x_output':x_output, 'diff_fin_inital':diff_fin_inital,
                'percentage_output':percentage_output,
                'flag2':True,
            }
            return render(request, 'mathematics/markup.html', context)

        elif given == 'form3' and markup and initial_price:
            mark_up = check_decimal(markup)
            init_price = check_decimal(initial_price)
           
            mul_init_markup = init_price * (mark_up/100)
            sell_price_output = init_price + mul_init_markup            

            sell_price_output = round(sell_price_output, 2)
            mul_init_markup = round(mul_init_markup, 4)              

            context = {
                'given':given,'markup':markup, 'initial_price':initial_price,
                'mul_init_markup':mul_init_markup,
                'sell_price_output':sell_price_output,
                'flag3':True,
            }
            return render(request, 'mathematics/markup.html', context)
        context = {'given': given}
        return render(request, 'mathematics/markup.html', context)
        
    else:
        return render(request, 'mathematics/markup.html', {'given':'form2', 'initial_price':12, 'final_price':25})


def variation_eq(request):

    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        y = request.POST.get('y')
        given = request.POST.get('given')

        if given == 'form1' and x1 and x2 and y and request.method == 'POST':
            y = check_decimal(y)
            x1 = check_decimal(x1)
            x2 = check_decimal(x2)

            if x1 == 0 or x2 == 0:
                messages.error(request, 'First x can not be 0')
                context = {
                'given':given, 'x1':x1, 'x2':x2,'y':y,
                }
                return render(request, 'mathematics/variation_eq.html', context)

            div_result = y/x1
            y_result = div_result * x2

            div_result = round(div_result, 3)
            y_result =round(y_result, 2)

            context = {
                'y':y, 'x1':x1, 'x2':x2, 'given':given,
                'div_result':div_result, 'y_result':y_result,
                'flag1':True,
            }
            return render(request, 'mathematics/variation_eq.html', context)

        elif given == 'form2' and x1 and x2 and y and request.method == 'POST':
            y = check_decimal(y)
            x1 = check_decimal(x1)
            x2 = check_decimal(x2)

            if x2 == 0:
                messages.error(request, 'second x should be not be 0')
                context = {
                'given':given, 'x1':x1, 'x2':x2,'y':y,
                }
                return render(request, 'mathematics/variation_eq.html', context)

            k_result = y * x1
            y_result = k_result/x2

            y_result =round(y_result, 2)

            context = {
                'y':y, 'x1':x1, 'x2':x2, 'given':given,
                'k_result':k_result, 'y_result':y_result,
                'flag2':True,
            }
            return render(request, 'mathematics/variation_eq.html', context)

        elif given == 'form3' and x1 and x2 and y and request.method == 'POST':
            y = check_decimal(y)
            x1 = check_decimal(x1)
            x2 = check_decimal(x2)

            if x1 == 0 or x2 == 0:
                messages.error(request, 'First x can not be 0')
                context = {
                'given':given, 'x1':x1, 'x2':x2,'y':y,
                }
                return render(request, 'mathematics/variation_eq.html', context)

            sqr_of_x1 = x1 * x1
            k_result = y/sqr_of_x1

            sqr_of_x2 = x2 * x2
            y_result = k_result * sqr_of_x2

            k_result = round(k_result, 2)
            y_result = round(y_result, 3)
            sqr_of_x2 = round(sqr_of_x2, 3)

            context = {
                'y':y, 'x1':x1, 'x2':x2, 'given':given,
                'sqr_of_x1':sqr_of_x1, 'k_result':k_result,
                'sqr_of_x2':sqr_of_x2,
                'y_result':y_result,
                'flag3':True,
            }
            return render(request, 'mathematics/variation_eq.html', context)

        elif given == 'form4' and x1 and x2 and y and request.method == 'POST':
            y = check_decimal(y)
            x1 = check_decimal(x1)
            x2 = check_decimal(x2)

            if x1 == 0 or x2 == 0:
                messages.error(request, 'x should be not be 0')
                context = {
                'given':given, 'x1':x1, 'x2':x2,'y':y,
                }
                return render(request, 'mathematics/variation_eq.html', context)


            cube_of_x1 = x1 * x1 * x1
            k_result = y/cube_of_x1
            
            cube_of_x2 = x2 * x2 * x2
            y_result = k_result * cube_of_x2

            k_result = round(k_result, 4)
            y_result = round(y_result, 2)
            cube_of_x2 = round(cube_of_x2, 4)

            context = {
                'y':y, 'x1':x1, 'x2':x2, 'given':given,
                'cube_of_x1':cube_of_x1, 'k_result':k_result,
                'cube_of_x2':cube_of_x2,
                'y_result':y_result,
                'flag4':True,
            }
            return render(request, 'mathematics/variation_eq.html', context)

        elif given == 'form5' and x1 and x2 and y and request.method == 'POST':
            y = check_decimal(y)
            x1 = check_decimal(x1)
            x2 = check_decimal(x2)            

            if x1 <= 0 or x2 <= 0:
                messages.error(request, 'x should be greater than 0')
                context = {
                'given':given, 'x1':x1, 'x2':x2,'y':y,
                }
                return render(request, 'mathematics/variation_eq.html', context)


            sqr_root_of_x1 = math.sqrt(x1)
            k_result = y/sqr_root_of_x1

            sqr_root_of_x2 = math.sqrt(x2)
            y_result = k_result * sqr_root_of_x2

            k_result = round(k_result, 2)
            y_result = round(y_result)
            sqr_root_of_x1 = round(sqr_root_of_x1, 4)
            sqr_root_of_x2 = round(sqr_root_of_x2, 4)

            context = {
                'y':y, 'x1':x1, 'x2':x2, 'given':given,
                'sqr_root_of_x1':sqr_root_of_x1, 'k_result':k_result,
                'sqr_root_of_x2':sqr_root_of_x2,
                'y_result':y_result,
                'flag5':True,
            }
            return render(request, 'mathematics/variation_eq.html', context)

        elif given == 'form6' and x1 and x2 and y and request.method == 'POST':
            y = check_decimal(y)
            x1 = check_decimal(x1)
            x2 = check_decimal(x2)

            if x1 == 0 or x2 == 0:
                messages.error(request, 'x should be not be zero')
                context = {
                'given':given, 'x1':x1, 'x2':x2,'y':y,
                }
                return render(request, 'mathematics/variation_eq.html', context)

            sqr_of_x1 = x1*x1
            k_result = y * sqr_of_x1
            sqr_of_x2 = x2 * x2
            y_result = k_result/sqr_of_x2

            y_result =round(y_result, 2)
            sqr_of_x2 = round(sqr_of_x2, 4)
            k_result = round(k_result, 4)

            context = {
                'y':y, 'x1':x1, 'x2':x2, 'given':given,
                'sqr_of_x1':sqr_of_x1,'sqr_of_x2':sqr_of_x2,
                'k_result':k_result, 'y_result':y_result,
                'flag6':True,
            }
            return render(request, 'mathematics/variation_eq.html', context)
        
        elif given == 'form7' and x1 and x2 and y and request.method == 'POST':
            y = check_decimal(y)
            x1 = check_decimal(x1)
            x2 = check_decimal(x2)

            if x1 == 0 or x2 == 0:
                messages.error(request, 'x should be not be zero')
                context = {
                'given':given, 'x1':x1, 'x2':x2,'y':y,
                }
                return render(request, 'mathematics/variation_eq.html', context)

            cube_of_x1 = x1*x1*x1
            k_result = y * cube_of_x1

            cube_of_x2 = x2*x2*x2
            y_result = k_result/cube_of_x2

            y_result =round(y_result, 2)
            cube_of_x1 = round(cube_of_x1, 4)
            cube_of_x2 = round(cube_of_x2, 4)
            k_result = round(k_result, 4)

            context = {
                'y':y, 'x1':x1, 'x2':x2, 'given':given,
                'cube_of_x1':cube_of_x1,'cube_of_x2':cube_of_x2,
                'k_result':k_result, 'y_result':y_result,
                'flag7':True,
            }
            return render(request, 'mathematics/variation_eq.html', context)
        elif given == 'form8' and x1 and x2 and y and request.method == 'POST':
            y = check_decimal(y)
            x1 = check_decimal(x1)
            x2 = check_decimal(x2)

            if x1 <= 0 or x2 <= 0:
                messages.error(request, 'x should be non-negative')
                context = {
                'given':given, 'x1':x1, 'x2':x2,'y':y,
                }
                return render(request, 'mathematics/variation_eq.html', context)

            sqr_root_of_x1 = math.sqrt(x1)
            k_result = y * sqr_root_of_x1

            sqr_root_of_x2 = math.sqrt(x2)
            y_result = k_result/sqr_root_of_x2

            y_result =round(y_result, 2)
            sqr_root_of_x1 = round(sqr_root_of_x1, 4)
            k_result = round(k_result, 4)

            context = {
                'y':y, 'x1':x1, 'x2':x2, 'given':given,
                'sqr_root_of_x1':sqr_root_of_x1,'sqr_root_of_x2':sqr_root_of_x2,
                'k_result':k_result, 'y_result':y_result,
                'flag8':True,
            }
            return render(request, 'mathematics/variation_eq.html', context)

        return render(request, 'mathematics/variation_eq.html', {'given':given})

    else:
        return render(request, 'mathematics/variation_eq.html', {'given':'form1', 'y':10, 'x1':2, 'x2':4})


def eq_annual_cost(request):
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        invst_cost_a = request.POST.get('invst_cost_a')
        invst_cost_b = request.POST.get('invst_cost_b')

        expec_lftm_a = request.POST.get('expec_lftm_a')
        expec_lftm_b = request.POST.get('expec_lftm_b')

        main_cost_a = request.POST.get('main_cost_a')
        main_cost_b = request.POST.get('main_cost_b')

        cost_of_cap = request.POST.get('cost_of_cap')

        

        invst_cost_a = check_decimal(invst_cost_a)
        invst_cost_b = check_decimal(invst_cost_b)
        expec_lftm_a = check_decimal(expec_lftm_a)
        expec_lftm_b = check_decimal(expec_lftm_b)
        main_cost_a = check_decimal(main_cost_a)
        main_cost_b = check_decimal(main_cost_b)
        cost_of_cap = check_decimal(cost_of_cap)

        if invst_cost_a<=0 or invst_cost_b<=0 or expec_lftm_a<=0 or expec_lftm_b<=0 or main_cost_a<=0 or main_cost_b<=0 or cost_of_cap<=0:
                messages.error(request, 'values should be greater than 0')
                context = {
                    'invst_cost_a':invst_cost_a, 'invst_cost_b':invst_cost_b,
                    'expec_lftm_a':expec_lftm_a, 'expec_lftm_b':expec_lftm_b,
                    'main_cost_a':main_cost_a, 'main_cost_b':main_cost_b,
                    'cost_of_cap':cost_of_cap,
                }
                return render(request, 'mathematics/variation_eq.html', context)


        cost_of_cap_in_percent = cost_of_cap/100
        cost_of_cap_in_percent_pls1 = 1 + cost_of_cap_in_percent
        v_result = 1/(cost_of_cap_in_percent_pls1)
        
        v_power_lifetime_a = math.pow(v_result, expec_lftm_a)
        sub_a = 1 - v_power_lifetime_a

        disc_fact_a = sub_a/cost_of_cap_in_percent
        disc_inv_a = invst_cost_a/disc_fact_a
        sum_disInv_main_cost_a = disc_inv_a + main_cost_a

        v_result = round(v_result, 5)

        v_power_lifetime_b = math.pow(v_result, expec_lftm_b)
        sub_b = 1 - v_power_lifetime_b
        disc_fact_b = sub_b/cost_of_cap_in_percent
        disc_inv_b = invst_cost_b/disc_fact_b
        sum_disInv_main_cost_b = disc_inv_b + main_cost_b

        disc_fact_a = round(disc_fact_a, 5)
        disc_fact_b = round(disc_fact_b, 5)

        disc_inv_a = round(disc_inv_a, 4)
        disc_inv_b = round(disc_inv_b, 4)

        sum_disInv_main_cost_a = round(sum_disInv_main_cost_a, 4)
        sum_disInv_main_cost_b = round(sum_disInv_main_cost_b, 4)

        low = 0
        if sum_disInv_main_cost_b < sum_disInv_main_cost_a:
            low = 2
        else:
            low = 1

        context = {
            'invst_cost_a':invst_cost_a, 'invst_cost_b':invst_cost_b,
            'expec_lftm_a':expec_lftm_a, 'expec_lftm_b':expec_lftm_b,
            'main_cost_a':main_cost_a, 'main_cost_b':main_cost_b,
            'cost_of_cap':cost_of_cap,

            'cost_of_cap_in_percent':cost_of_cap_in_percent,
            'cost_of_cap_in_percent_pls1':cost_of_cap_in_percent_pls1,
            'v_result':v_result,

            'v_power_lifetime_a':v_power_lifetime_a,'sub_a':sub_a,
            'disc_fact_a':disc_fact_a, 'disc_inv_a':disc_inv_a,
            'sum_disInv_main_cost_a':sum_disInv_main_cost_a,

            'v_power_lifetime_b':v_power_lifetime_b, 'sub_b':sub_b,
            'disc_fact_b':disc_fact_b, 'disc_inv_b':disc_inv_b,
            'sum_disInv_main_cost_b':sum_disInv_main_cost_b,   

            'low':low, 'flag':True,        

        }
        return render(request, 'mathematics/eac.html', context)

    else:
        context = {
            'invst_cost_a':15000, 'invst_cost_b':20000,
            'expec_lftm_a':8, 'expec_lftm_b':3,
            'main_cost_a':5000, 'main_cost_b':400,
            'cost_of_cap':5,

        }
        return render(request, 'mathematics/eac.html', context)


def powerWithDisplacement(request):

    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value


    # convertor
    def meterconverter(lentype, lenn):
        if lentype == 'km':
            m = lenn * 1000
        elif lentype == 'mm':
            m = lenn / 1000
        elif lentype == 'cm':
            m = lenn / 100.0
        elif lentype == 'in':
            m = lenn / 39.37
        elif lentype == 'ft':
            m = lenn / 3.28084
        elif lentype == 'yd':
            m = lenn / 1.094
        elif lentype == 'mi':
            m = lenn * 1609
        else:
            m = lenn
        return m

    if request.method == 'POST':
        force = check_decimal(request.POST.get('force'))
        displacement = check_decimal(request.POST.get('displacement'))
        time = check_decimal(request.POST.get('time'))
        # displacement_op = request.POST.get('displacement_op')
        # time_op = request.POST.get('time_op')

        actual_disp = displacement
        actual_time = time

        # using displacement converter function
        # displacement = meterconverter(displacement_op, displacement )        
        # print("----------", force, displacement, time)

        if time == 0:
            messages.error(request, 'Please enter vaild time, it can not be 0')
            context = {
            'force':force,
            'displacement':actual_disp,
            'time':actual_time,            
            }
            return render(request, 'mathematics/power_with_displacement.html', context)

        if displacement == 0 or force == 0:
            f_into_dis = 0
            power = 0
        else:         

            #power calculation        
            f_into_dis = force * displacement
            power = f_into_dis/time

            #round off
            f_into_dis = round(f_into_dis, 5)
            power = round(power, 4)

        context = {
            'force':force,
            'displacement':actual_disp,
            'time':actual_time,
            'power':power,
            'f_into_dis':f_into_dis,
            'flag':True,
        }
        return render(request, 'mathematics/power_with_displacement.html', context)

    else:        
        return render(request, 'mathematics/power_with_displacement.html')



# Moment of Inertia
def momentOfInertia(request):
    
    if request.method == 'POST':
        shape = request.POST.get('shape')
        print("shape------", shape)
        print("--------------------------in post")

        if shape == 'triangle':
            tri_width = request.POST.get('tri_width')
            tri_height = request.POST.get('tri_height')
            tri_doh = request.POST.get('tri_doh')

            print("------------------------------", tri_width, tri_height, tri_doh)
            cube_height = math.pow(tri_height, 3)
            cube_width = math.pow(tri_width, 3)

            # ix =  ( tri_width * cube_height )/ 36
            # iy = (tri_height * cube_width ) - (tri_height * tri_doh * tri_width*tri_width )+ tri_width * tri_height * tri_doh * tri_doh) / 36


            return render(request, 'mathematics/moment_of_inertia.html', {'shape':shape})

        # elif  shape == 'rectangle':
        #     pass


        # elif  shape == 'semicircle':
        #     pass

        # elif  shape == 'circle':
        #     pass

        # elif  shape == 'ellipse':
        #     pass

        # elif  shape == 'regular_hexagon':
        #     pass

        # return render(request, 'mathematics/moment_of_inertia.html', {'shape':shape})


        
    else:
        print("--------------------------in gettt")
        shape = request.POST.get('shape')
        print("shippppppppppp-------", shape)

        return render(request, 'mathematics/moment_of_inertia.html', {'shape':'triangle'})