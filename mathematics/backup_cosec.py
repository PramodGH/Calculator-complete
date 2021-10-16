from django.shortcuts import render
import math

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

        if angle == 0:
            result = 'Undefined'
        else:
            if angle_op == 'deg':
                x = convert_to_radian(angle, angle_op)
            else:
                x = angle
            result = round(1/math.sin(x), 8)

        context = {
            'result': result,
            'angle': angle,
            'angle_op': angle_op,
            'flag': True
        }
        return render(request, 'mathematics/cosecant.html', context)
    else:
        return render(request, 'mathematics/cosecant.html',{'flag':False})
