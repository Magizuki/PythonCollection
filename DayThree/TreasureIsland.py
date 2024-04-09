print('Welcome to Treasure Island. Your mission is to find the treasure')
left_or_right = input('Left or Right?')

if left_or_right.lower() == 'right':
    print('Game Over')
else:
    swim_or_wait = input('swim or wait?')
    if swim_or_wait.lower() == 'swim':
        print('Game Over')
    else:
        door = input("which door? red, blue, or yellow?")
        if door.lower() == 'yellow':
            print('You Win!')
        else:
            print('Game Over')
input()
