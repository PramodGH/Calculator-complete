
def sum_of_linear_number_sequence(request):

    # to check for float values in input
    def check_decimal_values(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    # to generate the number sequence
    def find_sequence(periods, init_value, diff):
        p_ceil = math.ceil(periods)
        print("p_ceil-----------------", p_ceil)
        result_seq = ''
        count = 1
        start_value = init_value
        while count <= p_ceil:
            result_seq = result_seq + str(start_value) + ", "
            start_value = start_value + diff
            count += 1
        return result_seq


    if request.method == "POST":
        init_value = request.POST.get('init_value')  # values from form input
        diff = request.POST.get('diff')
        periods = request.POST.get('periods')
        fin_value = request.POST.get('fin_value')

        given = request.POST['given']

        # when initial value is choosen
        if given == "form1" and diff and periods and fin_value:
            diff = request.POST.get('diff')
            diff = check_decimal_values(diff)

            periods = request.POST.get('periods')
            periods = check_decimal_values(periods)

            fin_value = request.POST.get('fin_value')
            fin_value = check_decimal_values(fin_value)

            # Error condition
            if periods <= 0 :
                messages.error(request, 'Periods should be greater than 0 and integer value')
                context = {'given':'form1', 'diff':diff, 'fin_value':fin_value }
                return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)

            init_value_result = fin_value - (periods-1)*diff
            sum = (periods / 2) * (init_value_result + fin_value)
            # print("sum  is : -------", sum)

            result_seq = find_sequence(periods, init_value_result, diff)

            context = {
                'given': given,
                'diff':diff,
                'periods':periods,
                'fin_value':fin_value,
                'init_value_result':init_value_result,
                'sum':sum,
                'sequence': result_seq,
                'flag1': True,
            }

            return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)

        # when Differnce is choosen
        elif given == "form2" and init_value and periods and fin_value:
            init_value = request.POST.get('init_value')
            init_value = check_decimal_values(init_value)

            periods = request.POST.get('periods')
            periods = check_decimal_values(periods)

            fin_value = request.POST.get('fin_value')
            fin_value = check_decimal_values(fin_value)

            if periods <= 0:
                messages.error(request, 'Periods should be greater than 0')
                context = {'given':'form2', 'init_value':init_value, 'fin_value':fin_value, 'periods':periods }
                return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)

            diff_result = (fin_value - init_value)/(periods-1)

            sum = (periods / 2) * (init_value + fin_value)

            result_seq = find_sequence(periods, init_value, diff_result)

            context = {
                'given': given,
                'diff_result':diff_result,
                'init_value': init_value,
                'periods': periods,
                'fin_value': fin_value,
                'sum':sum,
                'sequence':result_seq,
                'flag2':True
            }

            return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)

        # when Periods is choosen
        elif given == "form3" and init_value and diff and fin_value:

            diff = request.POST.get('diff')
            diff = check_decimal_values(diff)

            init_value = request.POST.get('init_value')
            init_value = check_decimal_values(init_value)

            fin_value = request.POST.get('fin_value')
            fin_value = check_decimal_values(fin_value)

            periods_result = ((fin_value - init_value)/diff)+1
            # print("periods-------------------------",periods_result)

            # print(" result sequence -------------------", result_seq)
            if periods_result <= 0:
                messages.error(request, 'Periods should be greater than 0 ')
                context = {'given': 'form2', 'init_value': init_value, 'fin_value': fin_value}
                return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)

            sum = (periods_result/2) * (init_value + fin_value)
            print("sum  is : -------", sum)

            result_seq = find_sequence(periods_result, init_value, diff)


            context = {
                'given': given,
                'diff': diff,
                'init_value': init_value,
                'fin_value': fin_value,
                'periods_result':periods_result,
                # 'periods_ceil':periods_ceil,
                'sum':sum,
                'sequence':result_seq,
                'flag3':True
            }
            return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)
        # when Find Final value is choosen
        if given == "form4" and init_value and diff and periods:
            diff = request.POST.get('diff')
            diff = check_decimal_values(diff)

            periods = request.POST.get('periods')
            periods = check_decimal_values(periods)

            init_value = request.POST.get('init_value')
            init_value = check_decimal_values(init_value)

            if periods <= 0:
                messages.error(request, 'Periods should be greater than 0')
                context = {'given':'form4', 'diff':diff, 'init_value':init_value, 'periods':periods }
                return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)


            fin_value_result = init_value + (periods - 1)*diff

            sum = (periods/2)*(init_value + fin_value_result)
            print("sum  is : -------", sum)
            result_seq = find_sequence(periods, init_value, diff)

            # sequence = numpy.linspace(init_value, fin_value_result, periods)
            # print("sequence---------", sequence, type(sequence))
            # result_seq = ''
            # for i in sequence:
            #     result_seq = result_seq + str(i) + ",  "
            # print(result_seq,"---------")

            context = {
                'given': given,
                'diff': diff,
                'periods': periods,
                'init_value': init_value,
                'sum': sum,
                'sequence': result_seq,
                'fin_value_result': fin_value_result,
                'flag4': True
            }
            return render(request, 'mathematics/sum-of-linear-number-sequence.html', context)
        return render(request, 'mathematics/sum-of-linear-number-sequence.html',
                      {'given': given, 'diff':2, 'periods':5, 'fin_value':10, 'init_value':1})
    else:
        return render(request, 'mathematics/sum-of-linear-number-sequence.html',
                      {'given': 'form1',  'diff':2, 'periods':5, 'fin_value':10})