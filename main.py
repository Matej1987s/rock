import random

options = ['Rock', 'Scissors', 'Paper']


def get_player_choice():
    print('1 for Rock, 2 for Scissors, 3 for Paper')
    user_input = input('What do you choose?')
    if user_input == '1':
        return 'Rock'
    elif user_input == '2':
        return 'Scissors'
    elif user_input == '3':
        return 'Paper'
    else:
        return get_player_choice()

def get_computer_choice():
    return random.choice(options)

def get_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'Draw !'
    elif (player_choice == 'Rock' and computer_choice == 'Scissors')  or \
            (player_choice == 'Scissors' and computer_choice == 'Paper') or \
            (player_choice == 'Paper' and computer_choice == 'Rock'):
        return 'Player win !'
    else:
        return 'Computer win !'

def play():
    player_choice = get_player_choice()
    print(f'Player choose {player_choice}')
    computer_choice = get_computer_choice()
    print(f'Computer choose {computer_choice}')
    result = get_result(player_choice, computer_choice)
    print(result)

play()

# TODO play game in a loop, asking if user wants to continue or not
# TODO add this repo to github








