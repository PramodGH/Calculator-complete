def find_both_numbers(request):
    from sympy import symbols, Eq, solve

    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        print("num1 and 2--------",num1, num2)

        num1 = check_decimal(num1)
        num2 = check_decimal(num2)

        p = -(num1)
        # r = f'x - y = {p}'
        # print("r ---------------", r, p)
        rearranged_eq_1 = f'x - y = {p}'
        print("Rearanged equation no 1--------",rearranged_eq_1)
        rearranged_eq_2 = f'x + y = {num2}'

        x, y = symbols('x y')
        eq1 = Eq((num2 - y), 0) # x + y = 10 second eqation

        eq_after_sub_from_both_sides_str = f'x = {num2} - y'
        print("equatio after-----------",eq_after_sub_from_both_sides_str)

        expr1 = Eq((x - y), 0)
        after_subs = expr1.subs(x, num2 -y )
        print("after substitution: -------",after_subs)
        putting_x_in_sub = f' {num2} - y - y = {p}'
        # full_eq_after_subs = f'{after_subs} = {p}'
        # print("New expression string-----",putting_x_in_sub,full_eq_after_subs )
        # print("putting x ------", putting_x)
        print("after subs--", expr1)
        expr2 = Eq((x - y), p)
        print("expres 2 is:",expr2 )
        solve_for_y = expr2.subs(x, num2 - y)
        print("solve_for_y:", solve_for_y)
        fin_solve_for_y = solve(solve_for_y, y)
        print("fin------------------type", type(fin_solve_for_y), fin_solve_for_y)
        # y_ =
        y_result = round(float(fin_solve_for_y[0]), 3)
        # print("y_ ",y_, type(y))
        print("output of y is : y result", fin_solve_for_y, y_result, type(y_result))
        y_is = f'y = {y_result}'

        eq_for_find_x = Eq((x - y), p)
        print("eq_for_find_x:", eq_for_find_x)
        new_eq = eq_for_find_x.subs(y, y_result )
        print("new equation s :", new_eq)
        final_result = solve(new_eq, x)
        print("final xx is is ", final_result)
        # k =
        # print("k :", k, type(k))
        final_result = round(float(final_result[0]), 3)
        eq_x_result = f'x = {final_result}'
        print("final eq is ", eq_x_result)


        # solve_for_y = solve(after_subs)

        # q = -(p)
        #
        # eq3 = Eq(x - y + q)
        #
        # print("new equation3 -", eq3)
        # solved_for_y = solve(eq3, y)

        context = {
            'num1':num1, 'num2':num2,
            'p':p,
            'rearranged_eq_1':rearranged_eq_1,
            'rearranged_eq_2':rearranged_eq_2,
            'eq_after_sub_from_both_sides_str':eq_after_sub_from_both_sides_str,
            'putting_x_in_sub':putting_x_in_sub,
            # 'full_eq_after_subs':full_eq_after_subs,
            'y_is':y_is,
            'y_result':y_result,
            'fin_solve_for_y':fin_solve_for_y,
            # 'solved_for_y':solved_for_y,
            'eq_x_result':eq_x_result,




            # 'eq_after_sub_from_both_sides_str':eq1,

            'flag':True,
        }

        return render(request, 'mathematics/find_both_numbers.html', context)

    else:
        return render(request, 'mathematics/find_both_numbers.html', {'num1':10, 'num2':18})

