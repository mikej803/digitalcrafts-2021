







strings = ['work', 'bills', 'family', 'vacation', 'money']


def shortest(strings):
    shortest = strings[0]
    for i in strings:
        if i <= shortest:
            shortest = i
    print('This is the shortest string:', shortest )
shortest(strings)



