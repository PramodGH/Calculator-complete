def fact(n):
    if n == 1 or n == 0:
        output = '1*'
        return 1, output
    factorial, output = fact(n - 1)
    print("---iside n ", n)
    factorial = factorial * n
    print("factorial :", factorial)

    output = output + str(n) + '*'
    return factorial, output

result, output = fact(4)
print("result: ", result)
print("output: ", output)