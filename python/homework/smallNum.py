

numbers = [30, 23, 12, 15, 10, 20]


def smallest(numbers):
    smallest = numbers[0]
    for i in numbers:
        if i <= smallest:
            smallest = i
    print('This is the smallest number: ', smallest )
smallest(numbers)




