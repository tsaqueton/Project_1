import random
from Project_1_module import *


def main():
    random.seed(1)
    heading()
    score = 0
    for num in range(0, 3):
        user_hand = get_user_hand()
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