import operator


def arithmetic_arranger(problems, answer=False):
    # function to validate the string in the problems array and get all the errors out in a go
    def validate(arr):
        # assigning all the variable their values using unpacking concept of lists
        x, op, y = arr.split(" ")
        if not x.isdigit() or not y.isdigit():
            raise ValueError("Error: Numbers must only contain digits.")
        if op not in ops:
            raise ValueError("Error: Operator must be '+' or '-'.")
        if int(x) >= 1e4 or int(y) >= 1e4:
            raise ValueError("Error: Numbers cannot be more than four digits.")
        # return the data according to you if not error is raised
        return (int(x), op, int(y))

    # function to format the item in validated problems and return tuple
    def format_eqn(eqn, answer):
        x, op, y = eqn
        # higher number between the provided two
        biggest_num = max(x, y)
        # find out the length of the higher number
        width = len(str(biggest_num))
        lines = (
            f"{x:>{width+2}}",
            f"{op} {y:>{width}}",
            f"{'':->{width+2}}",
        )
        if answer:
            lines += (f"{ops[op](x, y):>{width+2}}",)
        return lines

    # check if the number of problems exceed 5 and initialize the ops dict
    ops = {"+": operator.add, "-": operator.sub}
    if len(problems) > 5:
        return "Error: Too many problems."
    # execute the validate function and get all the error here without going further in the code
    try:
        validated_problems = [validate(problem) for problem in problems]
    except ValueError as e:
        return e
    # format the equation and zip the value of first line together and the second line ...
    formatted_eqn = zip(*(format_eqn(arr, answer) for arr in validated_problems))
    # join the first group with four space and then join these group with a new line
    return "\n".join("    ".join(line) for line in formatted_eqn)


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))

# * To pass all the tests
# import operator


# def arithmetic_arranger(problems, answer=False):
#     # function to format the item in validated problems and return tuple
#     def format_eqn(eqn, answer):
#         x, op, y = eqn
#         # higher number between the provided two
#         biggest_num = max(x, y)
#         # find out the length of the higher number
#         width = len(str(biggest_num))
#         lines = (
#             f"{x:>{width+2}}",
#             f"{op} {y:>{width}}",
#             f"{'':->{width+2}}",
#         )
#         if answer:
#             lines += (f"{ops[op](x, y):>{width+2}}",)
#         return lines

#     # check if the number of problems exceed 5 and initialize the ops dict
#     ops = {"+": operator.add, "-": operator.sub}
#     if len(problems) > 5:
#         return "Error: Too many problems."
#     # execute the validate function and get all the error here without going further in the code
#     validated_problems = []
#     for arr in problems:
#         # assigning all the variable their values using unpacking concept of lists
#         x, op, y = arr.split(" ")
#         if not x.isdigit() or not y.isdigit():
#             return "Error: Numbers must only contain digits."
#         if op not in ops:
#             return "Error: Operator must be '+' or '-'."
#         if int(x) >= 1e4 or int(y) >= 1e4:
#             return "Error: Numbers cannot be more than four digits."
#         # return the data according to you if not error is raised
#         validated_problems.append((int(x), op, int(y)))
#     # format the equation and zip the value of first line together and the second line ...
#     formatted_eqn = zip(*(format_eqn(arr, answer) for arr in validated_problems))
#     # join the first group with four space and then join these group with a new line
#     return "\n".join("    ".join(line) for line in formatted_eqn)

# ! Old solution
# def arithmetic_arranger(problem, answer=False):
#     op = []
#     num = []
#     var1 = []
#     for i in problem:
#         x = i.split()
#         var1.append(x)

#     for i in range(len(var1)):
#         op.append(var1[i][1])
#         num.append(var1[i][0])
#         num.append(var1[i][2])

#         # print(var1)
#         # print(op)
#         # print(num)

#     def max_of_digits(m):
#         return max(len(var1[m][0]), len(var1[m][2]))

#     def min_of_digits(m):
#         return min(len(var1[m][0]), len(var1[m][2]))

#     ans = ''
#     k = ''
#     s = ''
#     h = ''
#     for i in range(len(var1)):
#         if len(var1[i][0]) >= len(var1[i][2]):
#             s += ' ' * 2 + var1[i][0] + ' ' * 4
#             k += var1[i][1] + ' ' * (len(var1[i][0]) - len(var1[i][2]) + 1) + var1[i][2] + ' ' * 4
#         elif len(var1[i][0]) < len(var1[i][2]):
#             s += ' ' * 2 + ' ' * (len(var1[i][2]) - len(var1[i][0])) + var1[i][0] + ' ' * 4
#             k += var1[i][1] + ' ' + var1[i][2] + ' ' * 4
#         h += '-' * (max_of_digits(i) + 2) + ' ' * 4

#     if len(var1) < 6:
#         if '/' not in op and '*' not in op:
#             pass
#         else:
#             return "Error: Operator must be '+' or '-'."
#     else:
#         return 'Error: Too many problems.'

#     for i in range(len(num)):
#         if num[i].isdigit() and len(num[i]) < 5:
#             continue

#         elif len(num[i]) >= 5:
#             return "Error: Numbers cannot be more than four digits."

#         elif not num[i].isdigit():
#             return "Error: Numbers must only contain digits."

#     for i in range(len(var1)):
#         if '+' in var1[i]:
#             y = int(var1[i][0]) + int(var1[i][2])
#             ans += str(y).rjust(2 + max_of_digits(i), ' ') + ' ' * 4
#         elif '-' in var1[i]:
#             y = int(var1[i][0]) - int(var1[i][2])
#             ans += str(y).rjust(max_of_digits(i) + 2, ' ') + ' ' * 4

#     # print(s)
#     # print(k)
#     # print(x)
#     if answer == True:
#         u = s.rstrip() + '\n' + k.rstrip() + '\n' + h.rstrip() + '\n' + ans.rstrip()
#     else:
#         u = s.rstrip() + '\n' + k.rstrip() + '\n' + h.rstrip()
#     return u
