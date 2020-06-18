import random

hands = ['rock', 'scissors', 'paper']

player_hand = int(input("Pick the hand 0.rock 1. scissors 2. paper "))
if player_hand >= 0 and player_hand < 3:
    print("Your hand is " + hands[player_hand])

    computer_hand = random.randint(0,2)
    print("Computer hand is "  + hands[computer_hand])

    if player_hand == computer_hand:
        print("Even")
    elif player_hand == 0 and computer_hand == 1:
        print("You win")
    elif player_hand == 1 and computer_hand == 2:
        print("You win")
    elif player_hand == 2 and computer_hand == 0:
        print("You win")
    else:
        print("You lose")
else:
    print("Type number between 0 to 2")


name = "My name is Python"
def reverse_name(str):
    str = str.split(' ')
    str.reverse()
    new_str = ' '.join(str)
    print(new_str)

reverse_name(name)




