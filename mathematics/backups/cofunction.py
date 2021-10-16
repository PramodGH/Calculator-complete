import math
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
        if (angle_op == 'deg' and (angle < 0 or angle > 90)) or (angle_op == 'rad' and (angle < 0 or angle > math.pi/2 )):
            messages.error(request, 'For the cofunction identities, the angle has to be between 0 and 90 degrees (or 0 and π/2 in radians).')
            return render(request, 'mathematics/cofunction.html',{'function':function, 'angle':angle,'angle_op':angle_op,'flag':False})

        pi_div_2_value = math.pi / 2
        x = convert_to_radian(angle, angle_op)

        if angle_op == 'deg':
            op = 90
            eval = 90 - angle
            eval_str = '90 ' + '- ' + str(angle)
        else:
            op = round(pi_div_2_value, 5)
            eval = pi_div_2_value - x
            eval_str = str(pi_div_2_value) + " - "+str(x)

        result = None
        if function == 'sin':
            result = math.sin(x)
        elif function == 'cos':
            result = math.cos(x)
        elif function == 'tan':
            result = math.tan(x)
        elif function == 'cot':
            result = 1/math.tan(x)
        elif function == 'sec':
            result = 1/math.cos(x)
        elif function == 'csc':
            result = 1/math.sin(x)
        result = round(result, 6)

        print("result----------------",result)
        context = {
            'result':result,
            'op':op,
            'eval':eval,
            'eval_str':eval_str,
            'angle':angle,
            'angle_op':angle_op,
            'function':function,
            'flag': True,
        }
        return render(request, 'mathematics/cofunction.html', context)

    else:
        return render(request, 'mathematics/cofunction.html',{'function':'sin(x)', 'angle':'deg', 'flag':False})