import unittest
from Project_1_controller import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.hand_list = ['rock', 'paper', 'scissors']

    def tearDown(self):
        print('tearDown')
        del self.hand_list

    def test_get_computer_hand(self):
        random.seed(1)
        self.assertEqual(get_computer_hand(self.hand_list), ['rock'])
        self.assertEqual(get_computer_hand(self.hand_list), ['scissors'])
        self.assertEqual(get_computer_hand(self.hand_list), ['scissors'])
        self.assertEqual(get_computer_hand(self.hand_list), ['rock'])
        self.assertEqual(get_computer_hand(self.hand_list), ['paper'])

    def test_function_round_winner(self):
        user = 'rock'
        computer = 'rock'
        self.assertEqual(function_round_winner(self.hand_list, user, computer), 'tie')
        user = 'rock'
        computer = 'paper'
        self.assertEqual(function_round_winner(self.hand_list, user, computer), 'computer')
        user = 'rock'
        computer = 'scissors'
        self.assertEqual(function_round_winner(self.hand_list, user, computer), 'user')
        user = 'paper'
        computer = 'paper'
        self.assertEqual(function_round_winner(self.hand_list, user, computer), 'tie')
        user = 'paper'
        computer = 'scissors'
        self.assertEqual(function_round_winner(self.hand_list, user, computer), 'computer')
        user = 'paper'
        computer = 'rock'
        self.assertEqual(function_round_winner(self.hand_list, user, computer), 'user')
        user = 'scissors'
        computer = 'scissors'
        self.assertEqual(function_round_winner(self.hand_list, user, computer), 'tie')
        user = 'scissors'
        computer = 'rock'
        self.assertEqual(function_round_winner(self.hand_list, user, computer), 'computer')
        user = 'scissors'
        computer = 'paper'
        self.assertEqual(function_round_winner(self.hand_list, user, computer), 'user')

    def test_function_game_over(self):
        user = 2
        computer = 0
        self.assertEqual(function_game_over(user, computer), 'user')
        user = 1
        computer = 2
        self.assertEqual(function_game_over(user, computer), 'computer')
        user = 1
        computer = 1
        self.assertEqual(function_game_over(user, computer), 'tie')


if __name__ == '__main__':
    unittest.main()
