


amount = float(input('Total bill amount?'))

service = input ('what is the level of service? ')


if service == 'good':
    tip = 0.2

elif service == 'fair':
    tip = 0.15

elif service == 'bad':
    tip = 0.1


tip_amount = amount * tip
print ('%.2f is the tip amount for your bill' % tip_amount)

total = amount + tip_amount
print('%.2f is your bill' % total)