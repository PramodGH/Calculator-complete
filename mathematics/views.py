from django.shortcuts import render, HttpResponse
from django.contrib import messages

# factorial function :
def fact(n):
    if n == 0:
        output = "1"
        return 1, output
    result = 1
    output = " "
    for i in range(n, 0, -1):
        result *= i
        if i == 1:
            output = output + str(i)
        else:
            output = output + str(i) + "*"
    # print("----loop output is: ", result)
    return result, output

# factorial calculator
def factorial(request):
    if request.method == 'POST':
        value = int(request.POST['value'])
        # print("---value :", value)

        (result, output) = tuple(fact(value))
        # print("result is :", result)
        # print("output is :", output)

        context = {
            'result' : result,
            'value': value,
            'output':output,
        }
        return render(request, 'mathematics/factorial.html', context)
    else:
        return render(request, 'mathematics/factorial.html')


# combination calculator
def combination(request):
    if request.method == 'POST':
        n = int(request.POST['n'])
        r = int(request.POST['r'])

        # for wrong inputs
        if r>n:
            messages.error(request, 'Please enter vaild data, "r" should not be greater than "n"')
            return render(request, 'mathematics/combinations.html')
        elif  n < 0 or r < 0:
            messages.error(request, 'Please enter vaild data, values should be non-negative')
            return render(request, 'mathematics/combinations.html')

        result1, output1 = fact(n)
        result2, output2 = fact(r)
        result3, output3 = fact(n-r)

        result = result1 // (result2 * result3)    # Final answer

        context = {
            'result':result,
            'result1': result1,      # Intermediate results -> resul1, result2, result3
            'result2': result2,
            'result3': result3,

            'output1':output1,      # output to show each factorial value and how it's evaluated
            'output2': output2,
            'output3':output3,

            'n':n,                  # Input values
            'r':r,
        }
        return render(request, 'mathematics/combinations.html', context)

    else:
        return render(request, 'mathematics/combinations.html')