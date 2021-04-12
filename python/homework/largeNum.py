

numbers = [38, 6, 16, 25, 16, 50]


def largest(numbers):
    largest = numbers[0]
    for i in numbers:
        if i >= largest:
            largest = i
    print('This is the largest number: ', largest )
largest(numbers)