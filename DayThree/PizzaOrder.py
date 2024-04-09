print('Thank you for choosing Python Pizza Deliveries!')
size = input()
add_pepperoni = input()
extra_cheese = input()

prize = 0

if size == 'S': prize += 15
elif size == 'M': prize +=20
elif size == 'L': prize +=25

if add_pepperoni == 'Y' and size == 'S' : prize += 2

if add_pepperoni == 'Y' and (size == 'M' or size == 'L') : prize += 3

if extra_cheese == 'Y': prize += 1

print(f'Thank you for choosing Python Pizza Deliveries! Your final bill is: ${prize}')
input()


