import random


def heading():
    print('-' * 22)
    print('Rock - Paper - Scissor')
    print('-' * 22)


def get_hand():
    hand_list = ['rock', 'paper', 'scissor']
    return random.choices(hand_list)


def get_user_hand():
    user_hand = input('Enter response: ').lower().strip()
    while user_hand != 'paper' and user_hand != 'rock' and user_hand != 'scissor':
        user_hand = input('Enter valid response: ').lower().strip()
    return user_hand


def round_winner(user, computer):
    if user == computer:
        print(f'Computer is {computer}. You are {user}. You tie.')
        return 0
    elif (user == 'rock' and computer == 'scissor') or \
            (user == 'paper' and computer == 'rock') or \
            (user == 'scissor' and computer == 'paper'):
        print(f'Computer is {computer}. You are {user}. You win.')
        return 1
    else:
        print(f'Computer is {computer}. You are {user}. You lose.')
        return -1


def main():
    random.seed(1)
    heading()
    score = 0
    for num in range(0, 3):
        user_hand = input('Enter response: ').lower().strip()
        while user_hand != 'paper' and user_hand != 'rock' and user_hand != 'scissor':
            user_hand = input('Enter valid response: ').lower().strip()
        computer_hand = get_hand()
        score += round_winner(user_hand, computer_hand[0])
        if score == 2 or score == -2:
            break
    if score > 0:
        print('GAME OVER - YOU WIN')
    elif score == 0:
        print('GAME OVER _ IT\'S A TIE')
    else:
        print('GAME OVER - COMPUTER WINS')


if __name__ == '__main__':
    main()
