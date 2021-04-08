

amount = float(input('Total bill amount?>>'))

service = input ('what is the level of service \n good, fair or bad? ')




if service == 'good':
    tip = 0.2

elif service == 'fair':
    tip = 0.15

elif service == 'bad':
    tip = 0.1


split = int(input('Split how many ways'))



tip_amount = amount * tip
print ('%.2f is the tip amount for your bill' % tip_amount)

# total = amount + tip_amount
# print('%.2f is your bill' % total)

# total_party = float(input('How will check get split?'))

# final_bill = (amount + tip_amount/ total_party)
# print('%.2f is your final bill'% final_bill)

total_per_person = (amount + tip_amount) / split
print('%.2f is the bill per person' % total_per_person)








