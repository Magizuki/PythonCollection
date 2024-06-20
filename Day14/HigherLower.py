from game_data import data
from art import logo
from art import vs
from os import system
import random

fCorrect= True
fContinue= True
score = 0
fSelected = {}

while fContinue:
    system('cls')
    while fCorrect:
        system('cls')
        print(logo) 
        if (score > 0):
            print(f"You're right! current score: {score}")
        if (fSelected == {}):
            fSelected = random.choice(data)
        print(f'compare A: {fSelected['name']} a {fSelected['description']}, from {fSelected['country']}')
        print(vs)
        fSelected2 = random.choice(data)
        while fSelected['name'] == fSelected2['name']:
            fSelected2 = random.choice(data)
        print(f'Against B: {fSelected2['name']} a {fSelected2['description']}, from {fSelected2['country']}')
        choice = input("who has more followers? Type 'A' or 'B': ")
        if (choice.lower() == 'a' and fSelected['follower_count'] > fSelected2['follower_count']):
            score += 1
        elif (choice.lower() == 'b' and fSelected['follower_count'] < fSelected2['follower_count']):
            score += 1
            fSelected = fSelected2
        else:
            system('cls')
            print(logo)
            print(f'Sorry, thats wrong. Final score: {score}')
            score = 0
            fCorrect = False
            fChoice2 = input('Do you want to continue?')
            if fChoice2.lower() == 'n' or fChoice2.lower() == 'no':
                fContinue = False
                break
            else:
                fCorrect = True
                fSelected = {}
                fSelected2 = {}
                continue

