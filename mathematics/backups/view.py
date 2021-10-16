
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


 # url pattern
path('quarter-mile/', views.quarter_mile, name='quarter-mile'),