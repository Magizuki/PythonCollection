import random
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

fContinue = True

while fContinue:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card1 = 21
    card2 = 21
    while card1 + card2 > 21:
        card1 = random.choice(cards)
        card2 = random.choice(cards)

    computer_card = [random.choice(cards)] 
    my_card =  [card1, card2]
    print(f'Your cards: {my_card}')
    print(f'Computer first card: {computer_card[0]}')
    choice = input('Type ''y'' to get another card, type ''n'' to pass:')
    sum_my_card = 0
    if(choice.lower() == 'y'):
        my_card.append(random.choice(cards))

    my_card.sort()
    for i in range(0, len(my_card)):
        if (my_card[i] == 11 and sum_my_card + my_card[i] > 21):
            my_card[i] = 1
            sum_my_card += 1
        else:
            sum_my_card += my_card[i]
    if (sum_my_card > 21):
        print(f'Your cards: ${my_card}')
        print(f'Computer cards: ${computer_card}')
        print('You Lose')
        choice = input('Do you want to continue ?')
        if (choice == 'no'):
            fContinue = False
        continue
    sum_computer_card = 0
    computer_card.append(random.choice(cards))
    while sum(computer_card) < 17:
        draw_card = random.choice(cards)
        if (draw_card == 11 and draw_card + sum(computer_card) > 21):
            draw_card = 1
        computer_card.append(draw_card)
    computer_card.sort()
    for i in range(0, len(computer_card)):
        if (computer_card[i] == 11 and sum_my_card + computer_card[i] > 21):
            computer_card[i] = 1
            sum_computer_card += 1
        else:
            sum_computer_card += computer_card[i]

    print(f'Your cards: ${my_card}')
    print(f'Computer cards: ${computer_card}')
    print(sum_my_card)
    print(sum_computer_card)
    if (sum_my_card == sum_computer_card):
        print('Draw')
    elif (sum_my_card > sum_computer_card):
        print('You Win')
    elif (sum_my_card < sum_computer_card and sum_computer_card <= 21):
        print('You Lose')
    else:
        print('You Win')
    
    choice = input('Do you want to continue ?')
    if (choice == 'no'):
        fContinue = False  

    