# def fact(n):
#     if n == 1 or n == 0:
#         output = '1*'
#         return 1, output
#     factorial, output = fact(n - 1)
#     print("---iside n ", n)
#     factorial = factorial * n
#     print("factorial :", factorial)
#
#     output = output + str(n) + '*'
#     return factorial, output
#
# result, output = fact(4)
# print("result: ", result)
# print("output: ", output)
scientific_notation = "{:.2e}".format(42)
print(scientific_notation)
print(type(scientific_notation))
# [print(x, end=",") for x in scientific_notation]
output=""
output+=scientific_notation[:4]+" x 10"
if(scientific_notation[5:6]=="+"):
    output+=scientific_notation[6:]
else:
    output+=scientific_notation[5:]
print(output)
