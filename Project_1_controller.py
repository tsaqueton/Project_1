from PyQt5.QtWidgets import *
from GUI_RPS import Ui_MainWindow
import random


class Controller(QMainWindow, Ui_MainWindow):
    """
    class Controller controls GUI_RPS.py (GUI for rock-paper-scissors program)
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.group = QButtonGroup()

        self.group.addButton(self.radioRock)
        self.group.addButton(self.radioPaper)
        self.group.addButton(self.radioScissors)

        self.Choose.hide()
        self.choose_hand.hide()
        self.radioRock.hide()
        self.radioPaper.hide()
        self.radioScissors.hide()

        self.radioRock.toggled.connect(self.show_choose_button)
        self.radioPaper.toggled.connect(self.show_choose_button)
        self.radioScissors.toggled.connect(self.show_choose_button)

        self.Play_Again.clicked.connect(lambda: self.play_game())
        self.Quit.clicked.connect(lambda: self.close())  # closes program when selected
        self.Choose.clicked.connect(lambda: self.choose_clicked())

        self.number_of_rounds = 3
        self.round = 0
        self.victory = self.number_of_rounds // 2 + 1
        self.user_score = 0
        self.computer_score = 0
        self.hand_list = [self.radioRock.text(), self.radioPaper.text(), self.radioScissors.text()]

    def button_config_1(self):
        """
        method button_config_1 configures the button format on GUI_RPS.py to
        show buttons "Play" or "Quit" and hides all other buttons
        """
        self.Play_Again.setText("Play again?")
        self.Play_Again.show()
        self.Quit.show()
        self.radioRock.hide()
        self.radioPaper.hide()
        self.radioScissors.hide()

    def button_config_2(self):
        """
        method button_config_2 configures the button format on GUI_RPS.py to show "Choose a hand"
        text, radio buttons, and hides all other buttons.
        """
        self.round_result.setText('')
        self.Play_Again.hide()
        self.Quit.hide()
        self.choose_hand.show()
        self.radioRock.show()
        self.radioPaper.show()
        self.radioScissors.show()

    def show_choose_button(self):
        """
        method show_choose_button connects radioRock, radioPaper, or radioScissors. When buttons are
        toggled, the method shows the "Choose" button
        """
        self.Choose.show()

    def get_user_hand(self):
        """
        method get_user_hand reads which radio button (radioRock, radioPaper, radioScissors) the user
        selected and returns it to method choose_clicked.
        :return: string (either 'rock', 'paper', or 'scissors')
        """
        if self.radioRock.isChecked():
            user_hand = self.radioRock.text()
        elif self.radioPaper.isChecked():
            user_hand = self.radioPaper.text()
        elif self.radioScissors.isChecked():
            user_hand = self.radioScissors.text()
        return user_hand

    def get_computer_hand(self):
        """
        method get_computer_hand uses random to choose from the class attribute list (hand_list) and returns it
        to method choose_clicked.
        :return: string ('rock', 'paper', or 'scissors')
        """
        return random.choices(self.hand_list)

    def round_winner(self, user, computer):
        """
        method round_winner determines the winner per rock-paper-scissors round and increments either
        self.user_score, self.computer_score, or neither depending on the respective hands.
        :param user: string (user_hand)
        :param computer:  string (computer_hand)
        """
        if user == computer:
            self.round_result.setText(f'Computer is {computer}. You are {user}. You tie.')
        elif (user == self.hand_list[0] and computer == self.hand_list[2]) or \
                (user == self.hand_list[1] and computer == self.hand_list[0]) or \
                (user == self.hand_list[2] and computer == self.hand_list[1]):
            self.round_result.setText(f'Computer is {computer}. You are {user}. You win.')
            self.user_score += 1
        else:
            self.round_result.setText(f'Computer is {computer}. You are {user}. You lose.')
            self.computer_score += 1

    def display_score(self, user_score, computer_score):
        """
        method display_score updates the user score and computer scores.
        :param user_score: integer (self.user_score)
        :param computer_score: integer (self.computer_score)
        """
        self.user_score_disply.setText(f"Your score:           {user_score}")
        self.computer_score_disply.setText(f"Computer score:    {computer_score}")

    def play_game(self):
        """
        method play_game sets up a new rock-paper-scissors game, resets button configuration
        (and text) and clears user/computer score (and round)
        :return:
        """
        self.choose_hand.setText('Choose a hand:')
        self.button_config_2()
        random.seed(1)
        self.user_score = 0
        self.computer_score = 0
        self.round = 0
        self.display_score(self.user_score, self.computer_score)

    def choose_clicked(self):
        """
        method choose_clicked occurs when the "Choose" button is clicked. It uses method self.get_user_hand
        and method self.get_computer_hand to retrieve respective hands. Then, it uses method self.round_winner
        to determine the victor of the round. Then it updates the score and clears the radio button selection
        and hides the "Choose" button. If all rounds are played or if a victor is determined based on points,
        this method calls the self.game_over method.
        """
        self.round += 1
        user_hand = self.get_user_hand()
        computer_hand = self.get_computer_hand()
        self.round_winner(user_hand, computer_hand[0])
        self.display_score(self.user_score, self.computer_score)
        self.group.setExclusive(False)
        self.group.checkedButton().setChecked(False)
        self.group.setExclusive(True)
        self.Choose.hide()
        if (self.round >= self.number_of_rounds or self.user_score >= self.victory) or \
                (self.computer_score >= self.victory):
            self.game_over()

    def game_over(self):
        """
        method game_over determines the game winner (whoever has higher points) or if the game is tie (equal points).
        The self.choose_hand text is changed to 'GAME OVER' and displays the game result. Then it calls method
        self.button_config_1 to show "Play again?" and "Quit" buttons and hides all other buttons.
        """
        self.button_config_1()
        if self.user_score > self.computer_score:
            self.choose_hand.setText('GAME OVER - YOU WIN')
        elif self.user_score == self.computer_score:
            self.choose_hand.setText('GAME OVER _ IT\'S A TIE')
        else:
            self.choose_hand.setText('GAME OVER - COMPUTER WINS')
