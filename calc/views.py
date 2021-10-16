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


