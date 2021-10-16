
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

        print("Entry in post method-------")
        # print(side_a, side_b, side_c)
        given = request.POST['given']
        print('which form request--------',given)
        # print('values in starting post------', side_a,side_b,side_c,angle_a, angle_b, angle_c, angle_unit)
        # and side_a and side_b and side_c:

        # Error check


        # and side_a and side_b and side_c
        if (given == "form1" or given == "form2" or given == "form3") and side_a and side_b and side_c:
            side_a = float(request.POST['side_a']) # sides from form
            side_b = float(request.POST['side_b'])
            side_c = float(request.POST['side_c'])
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
                print('in form1-------------')
                result = tlc.calculate_angle_A(side_a, side_b, side_c)

            elif given == 'form2':
                print('in form2-------------')
                result = tlc.calculate_angle_B(side_a, side_b, side_c)

            elif given == 'form3':
                print('in forrm3------------')
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

        # and angle_a and side_b and side_c:
        elif given == "form4" and angle_a and side_b and side_c:
            side_b = float(request.POST['side_b'])
            side_c = float(request.POST['side_c'])

            angle_a = float(request.POST['angle_a'])
            print("ange a, and angl unit -----",angle_a, angle_unit)
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
                print("walked inside degree------", result)
            else:
                result = tlc.calculate_side_a(side_b, angle_a, side_c)
                print("walked inside radians-------", result)


            # radian to degree convertor
            # if angle_unit == 'degree':
            #     result = math.degrees(result)
            #     print("inside convert to degree------",result)
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

        # and angle_b and side_a and side_c
        elif given == "form5" and angle_b and side_a and side_c:

            side_a = float(request.POST['side_a'])  # sides from form
            side_c = float(request.POST['side_c'])
            angle_b = float(request.POST['angle_b'])  # angle from form

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

            print("Inside form5->>>>>")
            result = None
            if angle_unit == 'degree':
                angle_B = math.radians(angle_b)
                result = tlc.calculate_side_b(side_a, angle_B, side_c)
                print("walked inside degree------", result)
            else:
                result = tlc.calculate_side_a(side_b, angle_b, side_c)
                print("walked inside radians-------", result)

            #
            # result = tlc.calculate_side_b(side_a, angle_b, side_c)
            #
            # if angle_unit == 'degrees':
            #     result = tlc.convert_to_degree(result)
            result = round(result, significant_figures)
            print("Inside form5->>>>Result>",result)

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
            print("Inside form5->>Before context render >>>")
            return render(request, 'mathematics/triangleLawOfCosines.html', context)

        # and angle_c and side_a and side_b:
        elif given == "form6" and angle_c and side_a and side_b:

            side_a = float(request.POST['side_a'])  # sides from form
            side_b = float(request.POST['side_b'])
            angle_c = float(request.POST['angle_c'])  # angle from form

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

            # result = tlc.calculate_side_c(side_a, angle_c, side_b)
            #
            # if angle_unit == 'degrees':
            #     result = tlc.convert_to_degree(result)

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
        return render(request, 'mathematics/triangleLawOfCosines.html', {'given': 'form1'} )


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
            a = float(request.POST['side_a']) # sides from form
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
        return render(request, 'mathematics/triangleLawOfSines.html', {'given':given})
    else:
        print("hit get  request---------------")
        return render(request, 'mathematics/triangleLawOfSines.html', {'given': 'form1'} )


def checkError(request, angle_unit, s1, angle, s2, s1_name, a_name, s2_name, given):
    print(" entry in fun")
    if angle_unit == 'degree':
        if angle == 0 :
            messages.error(request, "Enter value greater than 0")
            return render(request, 'mathematics/triangleLawOfSines.html', {'given': given})
        elif angle >= 180:
            messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
            return render(request, 'mathematics/triangleLawOfSsines.html', {'given': given})
        elif angle >= 90 and s2 <= s1:
            messages.error(request,f'For ASS (SSA) theorem with {a_name} ≥ 90° ({a_name} ≥ π/2) and {s2_name} ≤ {s1_name}, there are no solutions and no triangle!')

    elif angle_unit == 'radian':
        if angle == 0:
            messages.error(request, "Enter value greater than 0")
            return render(request, 'mathematics/triangleLawOfSsines.html', {'given': given})
        elif angle >= pi:
            messages.error(request, 'Sum of entered angles is too large for a regular triangle!')
            return render(request, 'mathematics/triangleLawOfSines.html', {'given': given})
        elif angle >= pi and s2 <= s1:
            messages.error(request, f'For ASS (SSA) theorem with {a_name} ≥ 90° ({a_name} ≥ π/2) and {s2_name} ≤ {s1_name}, there are no solutions and no triangle!')
