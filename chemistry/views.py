from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import math
from .unitConverters import wt_converter, vol_converter, power_raise


# neutralization calculator
def neutralization(request):
    if request.method == "POST":
        norm = request.POST.get('norm')  # values from form
        vol_sol = request.POST.get('vol_sol')
        wt_sol = request.POST.get('wt_sol')
        eq_wt = request.POST.get('eq_wt')

        given = request.POST['given']

        if given == "form1" and vol_sol and eq_wt and wt_sol:
            vol_sol = float(request.POST.get('vol_sol'))  # values from form if form1 is selected
            vol_sol_op = request.POST.get('vol_sol_op')

            eq_wt = float(request.POST['eq_wt'])
            eq_wt_op = request.POST.get('eq_wt_op')

            wt_sol = float(request.POST.get('wt_sol'))
            wt_sol_op = request.POST.get('wt_sol_op')

            # unit conversions
            vol_sol_c, formula1 = vol_converter(vol_sol, vol_sol_op)
            eq_wt_c, formula2 = wt_converter(eq_wt, eq_wt_op)
            wt_sol_c, formula3 = wt_converter(wt_sol, wt_sol_op)

            vol_sol_c = vol_sol_c

            put_values_in_formula = f' Normality = {wt_sol_c} / {vol_sol_c} * {eq_wt_c}'
            try:
                norm_solution = float(wt_sol_c / (vol_sol_c * eq_wt_c))
                result, power = power_raise(norm_solution)  # to convert answer in power form
            except ZeroDivisionError:
                messages.error(request, f'volume of solvent & equivalent weight must be > 0 ')
                return render(request, 'chemistry/neutralization.html', {'given': 'form1'})
            else:
                context = {
                    # 'norm': norm_solution,
                    # chages made
                    'norm': result,
                    'power_of_result': power,

                    'vol_sol': vol_sol,
                    'wt_sol': wt_sol,
                    'eq_wt': eq_wt,
                    'vol_sol_op': vol_sol_op,
                    'eq_wt_op': eq_wt_op,
                    'wt_sol_op': wt_sol_op,
                    'given': given,
                    'formula_desc': [formula1, formula2, formula3],
                    'put_values_in_formula': put_values_in_formula,
                    'flag1': True
                }
                # print("------------Normalization is : ", norm_solution)
                return render(request, 'chemistry/neutralization.html', context)


        elif given == "form2" and vol_sol and wt_sol and norm:
            vol_sol = float(request.POST.get('vol_sol'))  # values from form if form2 is selected
            vol_sol_op = request.POST.get('vol_sol_op')

            wt_sol = float(request.POST.get('wt_sol'))
            wt_sol_op = request.POST.get('wt_sol_op')

            norm = float(request.POST.get('norm'))
            norm_op = request.POST.get('norm_op')


            # unit conversions
            vol_sol_c, formula1 = vol_converter(vol_sol, vol_sol_op)
            wt_sol_c, formula2 = wt_converter(wt_sol, wt_sol_op)

            put_values_in_formula = f'Equivalent weight = {wt_sol_c} / ({norm} * {vol_sol_c})'

            try:
                eq_wt_soltion = float(wt_sol_c / (norm * vol_sol_c))
                result, power = power_raise(eq_wt_soltion)  # to convert answer in power form
            except ZeroDivisionError:
                messages.error(request, f'volume of solvent & Normality must be > 0 ')
                return render(request, 'chemistry/neutralization.html', {'given': 'form2'})

            context = {
                # 'eq_wt': eq_wt_soltion,
                'eq_wt': result,
                'power_of_result': power,
                'vol_sol': vol_sol,
                'wt_sol': wt_sol,

                'vol_sol_op': vol_sol_op,
                'wt_sol_op': wt_sol_op,
                'norm': norm,
                'given': given,
                'formula_desc': [formula1, formula2],
                'put_values_in_formula': put_values_in_formula,
                'flag2': True
            }
            return render(request, 'chemistry/neutralization.html', context)

        elif given == "form3" and wt_sol and eq_wt and norm:
            wt_sol = float(request.POST.get('wt_sol'))  # values from form if form3 is selected
            wt_sol_op = request.POST.get('wt_sol_op')

            eq_wt = float(request.POST.get('eq_wt'))
            eq_wt_op = request.POST.get('eq_wt_op')

            norm = float(request.POST.get('norm'))

            # unit conversions
            wt_sol_c, formula1 = wt_converter(wt_sol, wt_sol_op)
            eq_wt_c, formula2 = wt_converter(eq_wt, eq_wt_op)

            put_values_in_formula = f'Volume of solvent = {wt_sol_c} / ({norm} * {eq_wt_c})'

            try:
                vol_solution = wt_sol_c / (norm * eq_wt_c)
                result, power = power_raise(vol_solution)  # to convert answer in power form
                print("-----result", result, "------power",power)
            except ZeroDivisionError:
                messages.error(request, f'normality & equivalent weight must be > 0 ')
                return render(request, 'chemistry/neutralization.html', {'given': 'form3'})
            # print("--------vol_solution solution ", vol_solution)

            context = {
                # 'vol_sol': vol_solution,
                'vol_sol': result,
                'power_of_result': power,

                'wt_sol': wt_sol,
                'eq_wt': eq_wt,
                'wt_sol_op': wt_sol_op,
                'eq_wt_op': eq_wt_op,
                'norm': norm,
                'given': given,
                'formula_desc': [formula1, formula2],
                'put_values_in_formula': put_values_in_formula,
                'flag3': True
            }
            return render(request, 'chemistry/neutralization.html', context)

        elif given == "form4" and vol_sol and eq_wt and norm:
            vol_sol = float(request.POST.get('vol_sol'))  # values from form if form4(find wt of solute) is selected
            vol_sol_op = request.POST.get('vol_sol_op')

            eq_wt = float(request.POST.get('eq_wt'))
            eq_wt_op = request.POST.get('eq_wt_op')

            norm = float(request.POST.get('norm'))

            # unit conversions
            vol_sol_c, formula1 = vol_converter(vol_sol, vol_sol_op)
            eq_wt_c, formula2 = wt_converter(eq_wt, eq_wt_op)

            put_values_in_formula = f'Weight of solute = {norm} * {eq_wt_c} * {vol_sol_c}'

            wt_solution = float(norm * eq_wt_c * vol_sol_c)
            result, power = power_raise(wt_solution)  # to convert answer in power form

            context = {
                # 'wt_sol': wt_solution,
                'wt_sol': result,
                'power_of_result': power,

                'vol_sol': vol_sol,
                'eq_wt': eq_wt,
                'vol_sol_op': vol_sol_op,
                'eq_wt_op': eq_wt_op,
                # 'wt_sol_op': wt_sol_op,
                'norm': norm,
                'given': given,
                'formula_desc': [formula1, formula2],
                'put_values_in_formula': put_values_in_formula,
                'flag4': True
            }

            return render(request, 'chemistry/neutralization.html', context)
        return render(request, 'chemistry/neutralization.html', {'given': given})
    else:
        return render(request, 'chemistry/neutralization.html', {'given': 'form1'})
