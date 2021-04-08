


# while count <= t:
#     print(t, '*', count, '=',t*count)
#     count += 1

# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]

list1 = [2, 4, 5]
list2 = [2, 3, 6]
mult_list = []

for i in range(0,len(list1)):
    mult_list.append(list1[i]*list2[i])

print(list1, "X", list2, "=", mult_list)

# for i in range(num1):
#     for width in range(num2):
#         if height == 0 or height == num1 - 1 or width == 0 or width == num2 - 1:
#             print('*', end = '')
#         else:
#             print(' ', end = '')
#     print()

