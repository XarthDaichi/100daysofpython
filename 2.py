print('Welcome to the tip calculator!')
bill_total = int(input('What was the total bill? $'))
tip = input('How much tip would you like to give? 10, 12, or 15? ')
if tip == '15':
    tip_percentage = 1.15
elif tip == '12':
    tip_percentage = 1.12
elif tip == '10':
    tip_percentage = 1.10
else:
    print('Error cannot tip that')
    exit()
num_people = int(input('How many people to split the bill? '))

print('Each person should pay: ', round(bill_total * tip_percentage/num_people, 2))
