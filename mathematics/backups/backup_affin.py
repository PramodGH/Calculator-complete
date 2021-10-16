def affine_cipher(request):

    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    no_correspond_to_alphabet = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
        'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
        'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }
    key_list = list(no_correspond_to_alphabet.keys())
    print(" key list --------------", key_list)
    val_list = list(no_correspond_to_alphabet.values())
    print(" value list --------------", val_list)

    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'
                 'P','Q','R','S','T','U','V','W','X','Y','Z']

    def sum_using_formula(a, b, value_corr_to_alpha):
        mid_sum = a*value_corr_to_alpha
        final_sum = a*value_corr_to_alpha + b
        return mid_sum, final_sum

    mid_values = []
    final_values = []
    no_corres_to_alpha_values = []
    mod_values = []
    no_to_alpha_values = []


    if request.method == 'POST':

        str_input = request.POST.get('str_to_translate')
        a = request.POST.get('a')
        b = request.POST.get('b')
        # print("---------str, s, b", str_input, a, b, type(a))
        a = check_decimal(a)
        b = check_decimal(b)

        # print("---------str, s, b", str_input, a, b, type(a))


        for i in str_input:
            # print("cheking for----------------", i)
            nca = ''
            if i in alphabets:
                print("------------------present or not-------",i," is perent" )
                nca = no_correspond_to_alphabet.get(i, 0)
                no_corres_to_alpha_values.append(nca)
                # print("nca=-----i to number----type----------",i, nca, type(nca))


                mid_sum, final_sum = sum_using_formula(a, b, nca)
                mid_values.append(mid_sum)
                final_values.append(final_sum)

                # t = int(final_sum)%26
                #
                # mod_values.append(t)

                #finding corresponding alphabet with the modulous answer
                # no_to_alpha = key_list[val_list.index(t)]
                # no_to_alpha_values.append(no_to_alpha)




                # print("print----------mid_sum and final_sum", mid_sum, final_sum)

            else:
                no_corres_to_alpha_values.append('')
                mid_sum = 0
                final_sum = b
                mid_values.append(0)
                final_values.append(b)

                # no_to_alpha = key_list[val_list.index(t)]
                # no_to_alpha_values.append(no_to_alpha)

            t = int(final_sum) % 26

            mod_values.append(t)

            # finding corresponding alphabet with the modulous answer
            no_to_alpha = key_list[val_list.index(t)]
            no_to_alpha_values.append(no_to_alpha)
        # print("---------------------------------------------------------------------------------------------------")
        #
        # print("no---------", no_corres_to_alpha_values)
        # print("mid_values-", mid_values)
        # print("fin_values-", final_values)
        # print("mod_values-", mod_values)
        # print("alpha------", no_to_alpha_values)


        context = {
            'str_to_translate': str_input,
            'a': a, 'b': b,
            'flag': True,
            'no_corres_to_alpha_values':no_corres_to_alpha_values,
            'mid_values':mid_values,
            'final_values':final_values,
            'mod_values':mod_values,
            'no_to_alpha_values':no_to_alpha_values,

        }
        return render(request, 'mathematics/affine_cipher.html', context)


    else:
        strr = "AFFIN CIPHER"
        context = {
            'str_to_translate': strr,
            'a':3, 'b':8,
            'flag':True,
        }
        return render(request, 'mathematics/affine_cipher.html', context)
