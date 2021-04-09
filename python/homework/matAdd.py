



m1 = [[1, 3], [2, 4]]
m2 = [[5, 2],[1, 0]]
mSum = []



# [0][0] + [0][0]
# [0][1] + [0][1]
# [1][0] + [1][0]
# [1][1] + [1][1]

for i1 in range(2):
    m3 = []
    for i2 in range(0, 2, 1):
        m3.append(m1[i1][i2] + m2[i1][i2]) 

    mSum.append(m3)


print(mSum)










