import random

print('Rock, Paper, Or Scissor ? 1 for rock, 2 for paper, 3 for scissor')
user_choice = int(input())
cpu_choice = random.randint(1, 3)
if user_choice == 1:
    print('you choose rock')
elif user_choice == 2:
    print('you choose paper')
elif user_choice == 3:
    print('you choose scissor')

if cpu_choice == 1:
    print('computer choose rock')
elif cpu_choice == 2:
    print('computer choose paper')
elif cpu_choice == 3:
    print('computer choose scissor')

if user_choice == 1:
    if cpu_choice == 1:
        print('draw')
    if cpu_choice == 2:
        print('you lose')
    if cpu_choice == 3:
        print('you win')
elif user_choice == 2:
    if cpu_choice == 1:
        print('you win')
    if cpu_choice == 2:
        print('draw')
    if cpu_choice == 3:
        print('you lose')
elif user_choice == 3:
    if cpu_choice == 1:
        print('you lose')
    if cpu_choice == 2:
        print('you win')
    if cpu_choice == 3:
        print('draw')

input()
