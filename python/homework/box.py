

num1 = int(input('input height: '))

num2 = int(input('input width: '))

for height in range(num1):
    for width in range(num2):
        if height == 0 or height == num1 - 1 or width == 0 or width == num2 - 1:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()




