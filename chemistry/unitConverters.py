# conversion of differrent units of weight into grams
def wt_converter(value, unit):
    formula_des=''
    if unit == "μg":
        formula_des = f' {value} {unit} to grams = {value} / 1000000  '
        value = value / 1000000
        formula_des += f' = {value} g'

    elif unit == "kg":
        formula_des = f' {value} {unit} to grams = {value} * 1000 '
        value = value * 1000
        formula_des += f' = {value} g'

    elif unit == "mg":
        formula_des = f' {value} {unit} to grams = {value} value / 1000 '
        value = value / 1000
        formula_des += f' = {value} g'

    elif unit == "lb":
        formula_des = f' {value} {unit} to liters = {value} * 453.59237 '
        value = value * 453.59237
        formula_des += f' = {value} g'

    elif unit == 'oz':
        formula_des = f' {value} {unit} to grams = {value} * 28.3495'
        value = value * 28.3495
        formula_des += f' = {value} g'

    elif unit == 'dg':
        formula_des = f' {value} {unit} to grams = {value} * 10'
        value = value * 10
        formula_des += f' = {value} g'

    elif unit == 'stone':
        formula_des = f' {value} {unit} to grams = {value} * 6350.29'
        value = value * 6350.29
        formula_des += f' = {value} g'

    elif unit == 'US ton':
        formula_des = f' {value} {unit} to grams = {value} * 907185'
        value = value * 907185
        formula_des += f' = {value} g'

    elif unit == 'gr':
        formula_des = f' {value} {unit} to grams = {value} * 0.0647989'
        value = value * 0.0647989
        formula_des += f' = {value} g'

    elif unit == 'dr':
        formula_des = f' {value} {unit} to grams = {value} * 1.7718451953125'
        value = value * 1.7718451953125
        formula_des += f' = {value} g'

    elif unit == 't':
        formula_des = f' {value} {unit} to liters = {value} * 1000000 '
        value = value * 1000000
        formula_des += f' = {value} L'

    else:
        formula_des = f' Weight Already in grams = {value} g '

    return value, formula_des


# Conversion of different units volume into liters
def vol_converter(value, unit):
    formula_des = ''
    if unit == "m³":
        formula_des = f' {value} {unit} to liters = {value} * 1000 '
        value = value * 1000
        formula_des += f' = {value} L'

    elif unit == "cu in":
        formula_des = f' {value} {unit} to liters = {value} * 0.016387064 '
        value = value * 0.016387064
        formula_des += f' = {value} L'

    elif unit == "mm³":
        formula_des = f' {value} {unit} to liters = {value} * 0.000001  '
        value = value * 0.000001
        formula_des += f' = {value} L'

    elif unit == "cm³":
        formula_des = f' {value} {unit} to liters = {value} * 0.001 '
        value = value * 0.001
        formula_des += f' = {value} L'

    elif unit == 'cu ft':
        formula_des = f' {value} {unit} to liters = {value} * 28.3168  '
        value = value * 28.3168
        formula_des += f' = {value} L'

    elif unit == 'cu yd':
        formula_des = f' {value} {unit} to liters = {value} * 764.554857984 '
        value = value * 764.554857984
        formula_des += f' = {value} L'

    elif unit == 'dm³':
        formula_des = f' {value} {unit} to liters = {value} * 1 '
        value = value * 1
        formula_des += f' = {value} L'

    elif unit == 'ml':
        formula_des = f' {value} {unit} to liters = {value} * 0.001 '
        value = value * 0.001
        formula_des += f' = {value} L'

    elif unit == 'cl':
        formula_des = f' {value} {unit} to liters = {value} * 0.01 '
        value = value * 0.01
        formula_des += f' = {value} L'

    elif unit == 'US fl oz':
        formula_des = f' {value} {unit} to liters = {value} * 0.0295735295625 '
        value = value * 0.0295735295625
        formula_des += f' = {value} L'

    elif unit == 'US gal':
        formula_des = f' {value} {unit} to liters = {value} * 3.785409 '
        value = value * 3.785409
        formula_des += f' = {value} L'

    elif unit == 'US qt':
        formula_des = f' {value} {unit} to liters = {value} * 946.3529 '
        value = value * 946.3529
        formula_des += f' = {value} L'

    elif unit == 'US pt':
        formula_des = f' {value} {unit} to liters = {value} * 473.176475 '
        value = value * 473.176475
        formula_des += f' = {value} L'

    else:
        formula_des = f' Volume Already in liters = {value} L'

    return value, formula_des

def power_raise(value):
    scientific_notation = "{:.2e}".format(value)
    output = ""
    power = ''
    print(scientific_notation,"-----------scn noti")
    output += scientific_notation[:4] + " x 10 "
    if (scientific_notation[5:6] == "+"):
        power = scientific_notation[6:]
        if power[0]=='0':
            power = power[1:]
    else:
        power_digit = scientific_notation[6:]
        power = power + '-'

        if power_digit[0] == '0':
            power += power_digit[1:]
        else:
            power += power_digit
    # print(output,"----------",power)
    return output, power