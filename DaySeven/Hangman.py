import random
from HangmanWord import word_list
from HangmanArt import logo
from HangmanArt import stages

print(logo)
selected_word = random.choice(word_list)
#Testing code
print(f'Pssst, the solution is {selected_word}.')

display = []
life = 7
correct_guess = 0   

for a in range(0, len(selected_word)):
    display.append('_')

while(life != 0):
    guess = input("Guess a letter: ").lower()
    flag = 0
    for a in range(0, len(selected_word)):
        if(selected_word[a] == guess[0]):
            display[a] = guess[0]
            flag = 1
            correct_guess += 1
    print(display)
    if('_' not in display):
        break
    if(flag == 0):
        life -= 1
        print(stages[life])

if(life == 0):
    print("Game Over!")
elif('_' not in display):
    print("You Win!")
    

