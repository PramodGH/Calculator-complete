import math
def double_angle_formula(request):
    def convert_to_radian(value, unit):
        if unit == 'deg':
            value = value * (math.pi/180)
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

        #Calculating sin2θ
        # sin2θ  = 2 * math.sin(x)*math.cos(x)
        sin_intermediate_result_1 = math.sin(x)
        sin_intermediate_result_2 = math.cos(x)
        sin_result = round(2 * sin_intermediate_result_1 * sin_intermediate_result_2, 8)

        #Calculating cos2θ
        # cos2θ = 1 - 2* sin(sqr)θ
        cos_intermediate_result_1 = sin_intermediate_result_1
        cos_result = round(1 - (2*math.pow(cos_intermediate_result_1, 2)),8)

        # Calculating tan2θ
        # (2 * tan(θ)) /( 1- tan(sqr)θ)
        tan_intermediate_result_1 = math.tan(x)
        if (tan_intermediate_result_1 * tan_intermediate_result_1 == 1 ) or (angle_op == 'deg' and angle%180 == 45):
            tan_result = 'Undefined'
        else:
            tan_result = round((2 * tan_intermediate_result_1) / (1- math.pow(tan_intermediate_result_1, 2)),8)


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
            'sol_op':sol_op,
            'sign':sign,
            'flag': True
        }
        return render(request, 'mathematics/double_angle_formula.html', context)
    else:
        return render(request, 'mathematics/double_angle_formula.html', {'flag': False})