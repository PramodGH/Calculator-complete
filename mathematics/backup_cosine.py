from django.shortcuts import render, HttpResponse
from django.contrib import messages
import math
from .unitConverter import power_raise
from . import triangle_law_of_cosines_calculations as tlc
from . import triangle_law_of_sines_calculations as tls
from math import pi
from numpy import arctan

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
                    'given':given, 'side_a':side_a, 'side_b':side_b, 'side_c':side_c,
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
                'angle_unit':angle_unit,
                'given': given,
                'length_unit':length_unit,
                'significant_figures':significant_figures,
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
                    return render(request, 'mathematics/triangleLawOfCosines.html',{'given':'form4'})
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
                'angle_a':angle_a,
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
        return render(request, 'mathematics/triangleLawOfCosines.html', {'given':given})
    else:
        print("hit get  request---------------")
        return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form1'})