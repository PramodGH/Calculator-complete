def eq_annual_cost(request):
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    if request.method == 'POST':
        invst_cost_a = request.POST.get('invst_cost_a')
        invst_cost_b = request.POST.get('invst_cost_b')

        expec_lftm_a = request.POST.get('expec_lftm_a')
        expec_lftm_b = request.POST.get('expec_lftm_b')

        main_cost_a = request.POST.get('main_cost_a')
        main_cost_b = request.POST.get('main_cost_b')

        cost_of_cap = request.POST.get('cost_of_cap')

        

        invst_cost_a = check_decimal(invst_cost_a)
        invst_cost_b = check_decimal(invst_cost_b)
        expec_lftm_a = check_decimal(expec_lftm_a)
        expec_lftm_b = check_decimal(expec_lftm_b)
        main_cost_a = check_decimal(main_cost_a)
        main_cost_b = check_decimal(main_cost_b)
        cost_of_cap = check_decimal(cost_of_cap)

        if invst_cost_a<=0 or invst_cost_b<=0 or expec_lftm_a<=0 or expec_lftm_b<=0 or main_cost_a<=0 or main_cost_b<=0 or cost_of_cap<=0:
                messages.error(request, 'values should be greater than 0')
                context = {
                    'invst_cost_a':invst_cost_a, 'invst_cost_b':invst_cost_b,
                    'expec_lftm_a':expec_lftm_a, 'expec_lftm_b':expec_lftm_b,
                    'main_cost_a':main_cost_a, 'main_cost_b':main_cost_b,
                    'cost_of_cap':cost_of_cap,
                }
                return render(request, 'mathematics/variation_eq.html', context)


        cost_of_cap_in_percent = cost_of_cap/100
        cost_of_cap_in_percent_pls1 = 1 + cost_of_cap_in_percent
        v_result = 1/(cost_of_cap_in_percent_pls1)
        
        v_power_lifetime_a = math.pow(v_result, expec_lftm_a)
        sub_a = 1 - v_power_lifetime_a

        disc_fact_a = sub_a/cost_of_cap_in_percent
        disc_inv_a = invst_cost_a/disc_fact_a
        sum_disInv_main_cost_a = disc_inv_a + main_cost_a

        v_result = round(v_result, 5)

        v_power_lifetime_b = math.pow(v_result, expec_lftm_b)
        sub_b = 1 - v_power_lifetime_b
        disc_fact_b = sub_b/cost_of_cap_in_percent
        disc_inv_b = invst_cost_b/disc_fact_b
        sum_disInv_main_cost_b = disc_inv_b + main_cost_b

        disc_fact_a = round(disc_fact_a, 5)
        disc_fact_b = round(disc_fact_b, 5)

        disc_inv_a = round(disc_inv_a, 4)
        disc_inv_b = round(disc_inv_b, 4)

        sum_disInv_main_cost_a = round(sum_disInv_main_cost_a, 4)
        sum_disInv_main_cost_b = round(sum_disInv_main_cost_b, 4)

        low = 0
        if sum_disInv_main_cost_b < sum_disInv_main_cost_a:
            low = 2
        else:
            low = 1

        context = {
            'invst_cost_a':invst_cost_a, 'invst_cost_b':invst_cost_b,
            'expec_lftm_a':expec_lftm_a, 'expec_lftm_b':expec_lftm_b,
            'main_cost_a':main_cost_a, 'main_cost_b':main_cost_b,
            'cost_of_cap':cost_of_cap,

            'cost_of_cap_in_percent':cost_of_cap_in_percent,
            'cost_of_cap_in_percent_pls1':cost_of_cap_in_percent_pls1,
            'v_result':v_result,

            'v_power_lifetime_a':v_power_lifetime_a,'sub_a':sub_a,
            'disc_fact_a':disc_fact_a, 'disc_inv_a':disc_inv_a,
            'sum_disInv_main_cost_a':sum_disInv_main_cost_a,

            'v_power_lifetime_b':v_power_lifetime_b, 'sub_b':sub_b,
            'disc_fact_b':disc_fact_b, 'disc_inv_b':disc_inv_b,
            'sum_disInv_main_cost_b':sum_disInv_main_cost_b,   

            'low':low, 'flag':True,        

        }
        return render(request, 'mathematics/eac.html', context)

    else:
        context = {
            'invst_cost_a':15000, 'invst_cost_b':20000,
            'expec_lftm_a':8, 'expec_lftm_b':3,
            'main_cost_a':5000, 'main_cost_b':400,
            'cost_of_cap':5,

        }
        return render(request, 'mathematics/eac.html', context)

# URL route.
path('equivalent-annual-cost/', views.eq_annual_cost, name='equivalent-annual-cost'),