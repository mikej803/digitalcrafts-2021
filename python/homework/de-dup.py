


L = [5, 6, 7, 7, 8, 8, 10, 12, 20]
print(data)

def remove_duplicates(duplist):
    noduplist = []
    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)
    return noduplist

print(remove_duplicates(data))







# print(nums)
# del nums[2]

# print(nums)

# print(lens(nums))






# list1 = [1, 5, 6, 16, 20]
# print(list1)

# list2 = list1

# # print(list2)

# list2 = list1.copy()

# list2[1] = 99

# print(list2)