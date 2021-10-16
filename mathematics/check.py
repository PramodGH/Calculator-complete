# r = float(6.242e+18*0.000000000000000001)
# print(r)
# print(type(r))
# print(r)
#
# def power_raise(value):
#     scientific_notation = "{:.2e}".format(value)
#     print(scientific_notation,"-----scn noti----")
#     # print(type(scientific_notation),"-----type---")
#     # [print(x, end=",") for x in scientific_notation]
#     output = ""
#     power = ''
#     output += scientific_notation[:4] + " x 10 "
#     if scientific_notation[5:6] == "+":
#         power = scientific_notation[6:]
#         if power[0]=='0':
#             power = power[1:]
#     else:
#         power_digit = scientific_notation[6:]
#         power = power + '-'
#
#         if power_digit[0]=='0':
#             power += power_digit[1:]
#         else:
#             power +=power_digit
#         # power = scientific_notation[5:]
#     # print(output,"----------",power)
#     return output, power
#
# out, powerr = power_raise(0.0000000000000000001)
# print("--->",out,powerr)
# #
# x = -(-2)
# print("x -->", x, type(x))

# from sympy import symbols, Eq, solve
# num1 = 8
# num2 = 10
# p = -(num1)
# rearranged_eq_1 = f'x - y = {p}'
# print("Rearanged equation no 1--",rearranged_eq_1)
# rearranged_eq_2 = f'x + y = {num2}'
# print("Rearanged equation no 1--",rearranged_eq_2)
# x, y = symbols('x y')
# eq1 = Eq((num2 - y), 0)   # x + y = 10 second eqation
# str_eq1 = str(eq1)
# eq_after_sub_from_both_sides_str = f'x = {num2} - y'
# print("eq after subs", eq_after_sub_from_both_sides_str)
#
# print("eq by using sypy", str_eq1, type(str_eq1))
# print(str_eq1)
# print(solve(eq1, y))
#
# expr1 = Eq((x - y), 0)
# print("expres1 --", expr1)
# after_subs = expr1.subs(x, num2 -y )
# # we =str(after_subs)
# print("after substitution : ",after_subs)
# # solve_for_y = solve()
# expr2 = Eq((x - y), p)
# solve_for_y = expr2.subs(x, num2 - y)
# fin_solve_for_y = solve(solve_for_y, y)
# print("output of y is : ", fin_solve_for_y)
# x = "[{1,2,3},{2,3}][{3,4},{6,3,4}]"
# cou = x.count('[')
# print(cou)
# x, y = symbols('x y')
#         eq1 = Eq((num2 - y), 0)
#
#         eq_after_sub_from_both_sides_str = f'x = {eq1}'
#         print("equatio after-----------",eq_after_sub_from_both_sides_str)
#
# Python3 code to Check for
# balanced parentheses in an expression
# open_list = ["[", "{", "("]
# close_list = ["]", "}", ")"]


# Function to check parentheses
# def check(myStr):
#     stack = []
#     for i in myStr:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if ((len(stack) > 0) and
#                     (open_list[pos] == stack[len(stack) - 1])):
#                 stack.pop()
#             else:
#                 return "Unbalanced"
#         else:
#             pass
#     if len(stack) == 0:
#         return "Balanced"
#     else:
#         return "Unbalanced"

# print(check(x))

value_entered='[{1,2,3},{4,5,6}][{1,4},{2,3,5,6}][{2,8}{4,7,9},{3,6}]'
new_list_values = []
sq_brack = value_entered.split(']')
print(sq_brack)
for i in sq_brack:
    i+=']'
    new_list_values.append(i)
    # print(i)
new_list_values.pop()
print("new liast: ", new_list_values)
print(type(new_list_values))
print("-----------------------------")
no_of_partition = len(new_list_values)-1
print("no of partition: ", no_of_partition)
for i, j in enumerate(new_list_values):
    print("i : ", i)
    print(j)
