




strings = ['work', 'bills', 'family', 'vacation', 'money']


def longest(strings):
    longest = strings[0]
    for i in strings:
        if i >= longest:
            longest = i
    print('This is the longest string:', longest )
longest(strings)





