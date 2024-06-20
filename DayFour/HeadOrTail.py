import random

guess = int(input('Choose Head or Tail (0 for Head and 1 for tail)?'))
truth = random.randint(0, 1)

if guess == truth:
    print('You win')
else:
    print('You lose')
