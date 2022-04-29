import pytest
from Project_1_controller import *
from GUI_RPS import *


class Test:
    """
    class for testing methods in Project_1_controller.py
    """

    def setup_method(self):
        """
        method
        """
        self.rps = Controller()

    def teardown_method(self):
        """
        method
        """
        del self.rps

    def test_round_winner(self):
        self.rps.round_winner('rock', 'paper')
        assert self.rps.user_score == 0
        assert self.rps.computer_score == 1

    """
    actual = ['rock', 'paper', 'scissors']
    expected = ['rock', 'paper', 'scissors']
    
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])
    
    print(all([a == b for a, b in zip(actual, expected)]))
    """

