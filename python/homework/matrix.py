

[ [1, 3], ]

list1 = [2, 4, 5]
list2 = [2, 3, 6]
mult_list = []

for i in range(0,len(list1)):
    mult_list.append(list1[i]*list2[i])

print(list1, "X", list2, "=", mult_list)
