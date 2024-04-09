print('The Love Calculator is calculating your score...')
name1 = input()
name2 = input()

t = name1.count('t') + name2.count('t') + name1.count('T') + name2.count('T')
r = name1.count('r') + name2.count('r') + name1.count('R') + name2.count('R')
u = name1.count('u') + name2.count('u') + name1.count('U') + name2.count('U')
e = name1.count('e') + name2.count('e') + name1.count('E') + name2.count('E')
left = t + r + u + e

l = name1.count('l') + name2.count('l') + name1.count('L') + name2.count('L')
o = name1.count('o') + name2.count('o') + name1.count('O') + name2.count('O')
v = name1.count('v') + name2.count('v') + name1.count('V') + name2.count('V')
e = name1.count('e') + name2.count('e') + name1.count('E') + name2.count('E')
right = l + o + v + e

love_score = int(str(left) + str(right))
if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and menos')
elif love_score > 40 and love_score < 50:
    print(f'Your score is {love_score}, you alright together')
else:
    print(f'Your score is {love_score}')

input()
