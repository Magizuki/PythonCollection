import random

line1 = ['o', 'o', 'o']
line2 = ['o', 'o', 'o']
line3 = ['o', 'o', 'o']
map = [line1, line2, line3]
print('Hiding your treasure! X marks the spot.')
position = input()

if position[0].lower() == 'a':
    x = 0
elif position[0].lower() == 'b':
    x = 1
elif position[0].lower() == 'c':
    x = 2

# print(position[1])
map[x][int(position[1])] = 'x'

print(f'{line1}\n{line2}\n{line3}')
input()