from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import math

# neutralization calculator
def neutralization(request):
    if request.method == "POST":

        norm = request.POST.get('norm')             # values from form
        vol_sol = request.POST.get('vol_sol')
        wt_sol = request.POST.get('wt_sol')
        eq_wt = request.POST.get('eq_wt')

        given = request.POST['given']

        if given == "form1" and vol_sol and eq_wt and wt_sol:
            vol_sol = float(request.POST.get('vol_sol'))    # values from form if form1 is selected
            vol_sol_op = request.POST.get('vol_sol_op')

            eq_wt = float(request.POST['eq_wt'])
            eq_wt_op = request.POST.get('eq_wt_op')

            wt_sol = float(request.POST.get('wt_sol'))
            wt_sol_op = request.POST.get('wt_sol_op')

            # unit conversions
            vol_sol_c, formula1 = vol_converter(vol_sol, vol_sol_op)
            eq_wt_c, formula2 = wt_converter(eq_wt, eq_wt_op)
            wt_sol_c, formula3 = wt_converter(wt_sol, wt_sol_op)

            vol_sol_c = float(vol_sol_c)

            put_values_in_formula = f' Normality = {wt_sol_c} / {vol_sol_c} * {eq_wt_c}'
            norm_solution = float(wt_sol_c / (vol_sol_c * eq_wt_c))
            # print("--------normal solution ", norm_solution)

            context = {
                'norm': norm_solution,
                'vol_sol': vol_sol,
                'wt_sol': wt_sol,
                'eq_wt': eq_wt,
                'vol_sol_op': vol_sol_op,
                'eq_wt_op': eq_wt_op,
                'wt_sol_op': wt_sol_op,
                'given': given,
                'formula_desc': [formula1, formula2, formula3],
                'put_values_in_formula': put_values_in_formula
            }
            # print("------------Normalization is : ", norm_solution)
            return render(request, 'chemistry/neutralization.html', context)

        elif given == "form2" and vol_sol and wt_sol and norm:
            vol_sol = float(request.POST.get('vol_sol'))        # values from form if form2 is selected
            vol_sol_op = request.POST.get('vol_sol_op')

            wt_sol = float(request.POST.get('wt_sol'))
            wt_sol_op = request.POST.get('wt_sol_op')

            norm = float(request.POST.get('norm'))
            norm_op = request.POST.get('norm_op')

            # unit conversions
            vol_sol_c, formula1 = vol_converter(vol_sol, vol_sol_op)
            wt_sol_c, formula2 = wt_converter(wt_sol, wt_sol_op)

            put_values_in_formula = f'Equivalent weight = {wt_sol_c} / ({norm} * {vol_sol_c})'
            eq_wt_soltion = float(wt_sol_c / (norm * vol_sol_c))

            # print("--------eq_wt_soltion solution ", eq_wt_soltion)

            context = {
                'eq_wt': eq_wt_soltion,
                'vol_sol': vol_sol,
                'wt_sol': wt_sol,

                'vol_sol_op': vol_sol_op,
                'wt_sol_op': wt_sol_op,
                'norm': norm,
                'given': given,
                'formula_desc': [formula1, formula2],
                'put_values_in_formula': put_values_in_formula

            }
            return render(request, 'chemistry/neutralization.html', context)

        elif given == "form3" and wt_sol and eq_wt and norm:
            wt_sol = float(request.POST.get('wt_sol'))          # values from form if form3 is selected
            wt_sol_op = request.POST.get('wt_sol_op')

            eq_wt = float(request.POST.get('eq_wt'))
            eq_wt_op = request.POST.get('eq_wt_op')

            norm = float(request.POST.get('norm'))


            # unit conversions
            wt_sol_c, formula1 = wt_converter(wt_sol, wt_sol_op)
            eq_wt_c, formula2 = wt_converter(eq_wt, eq_wt_op)

            # wt_sol = wt_converter(wt_sol, wt_sol_op)
            put_values_in_formula = f'Volume of solvent = {wt_sol_c} / ({norm} * {eq_wt_c})'
            vol_solution = wt_sol_c / (norm * eq_wt_c)
            # print("--------vol_solution solution ", vol_solution)

            context = {
                'vol_sol': vol_solution,
                'wt_sol': wt_sol,
                'eq_wt': eq_wt,
                'wt_sol_op': wt_sol_op,
                'eq_wt_op': eq_wt_op,
                # 'wt_sol_op': wt_sol_op,
                'norm': norm,
                'given': given,
                'formula_desc': [formula1, formula2],
                'put_values_in_formula': put_values_in_formula,

            }
            return render(request, 'chemistry/neutralization.html', context)

        elif given == "form4" and vol_sol and eq_wt and norm:
            vol_sol = float(request.POST.get('vol_sol'))       # values from form if form4(find wt of solute) is selected
            vol_sol_op = request.POST.get('vol_sol_op')

            eq_wt = float(request.POST.get('eq_wt'))
            eq_wt_op = request.POST.get('eq_wt_op')

            norm = float(request.POST.get('norm'))

            # unit conversions
            vol_sol_c, formula1 = vol_converter(vol_sol, vol_sol_op)
            eq_wt_c, formula2 = wt_converter(eq_wt, eq_wt_op)

            put_values_in_formula = f'Weight of solute = {norm} * {eq_wt_c} * {vol_sol_c}'
            wt_solution = float(norm * eq_wt_c * vol_sol_c)
            # print("--------wt_solutionsolution ", wt_solution)

            context = {
                'wt_sol': wt_solution,

                'vol_sol': vol_sol,
                'eq_wt': eq_wt,
                'vol_sol_op': vol_sol_op,
                'eq_wt_op': eq_wt_op,
                # 'wt_sol_op': wt_sol_op,
                'norm': norm,
                'given': given,
                'formula_desc': [formula1, formula2],
                'put_values_in_formula': put_values_in_formula

            }

            return render(request, 'chemistry/neutralization.html', context)
        return render(request, 'chemistry/neutralization.html', {'given': given})
    else:
        return render(request, 'chemistry/neutralization.html', {'given': 'form1'})


# conversion of differrent units of weight into grams
def wt_converter(value, unit):
    if unit == "μg":
        formula_des = f' Convert {value} {unit} to liters = {value} / 1000000  '
        value = value / 1000000
        formula_des += f' = {value} g'

    elif unit == "kg":
        formula_des = f' Convert {value} {unit} to liters = {value} * 1000 '
        value = value * 1000
        formula_des += f' = {value} g'

    elif unit == "mg":
        formula_des = f'Convert {value} {unit} to liters = {value} value / 1000 '
        value = value / 1000
        formula_des += f' = {value} g'

    elif unit == "lb":
        formula_des = f' Convert -> {value} {unit} to liters = {value} * 453.59237 '
        value = value * 453.59237
        formula_des += f' = {value} g'

    elif unit == 'oz':
        formula_des = f' Convert -> {value} {unit} to liters = {value} * 28.3495'
        value = value * 28.3495
        formula_des += f' = {value} g'

    elif unit == 'dg':
        formula_des = f' Convert -> {value} {unit} to liters = {value} * 10'
        value = value * 10
        formula_des += f' = {value} g'

    else:
        formula_des = f' Weight Already in grams = {value} g , '

    return value, formula_des


# Conversion of different units volume into liters
def vol_converter(value, unit):
    formula_des = ''
    if unit == "m³":
        formula_des = f' Convert {value} {unit} to liters = {value} * 1000 '
        value = value * 1000
        formula_des += f' = {value} L'

    elif unit == "in":
        formula_des = f' Convert {value} {unit} to liters = {value} * 0.016387064 '
        value = value * 0.016387064
        formula_des += f' = {value} L'

    elif unit == "mm³":
        formula_des = f' Convert {value} {unit} to liters = {value} * 0.000001  '
        value = value * 0.000001
        formula_des += f' = {value} L'

    elif unit == "cm³":
        formula_des = f' Convert {value} {unit} to liters = {value} * 0.001 , '
        value = value * 0.001
        formula_des += f' = {value} L'

    elif unit == 'ft':
        formula_des = f' Convert {value} {unit} to liters = {value} * 28.3168 , '
        value = value * 28.3168
        formula_des += f' = {value} L'

    else:
        formula_des = f' Volume Alreay in liters = {value} L , '

    return value, formula_des
