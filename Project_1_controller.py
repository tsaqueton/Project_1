from PyQt5.QtWidgets import *
from GUI_RPS import Ui_MainWindow
from Project_1_module import *


class Controller(QMainWindow, Ui_MainWindow):
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

        self.Play_Again.clicked.connect(lambda: self.play_game())
        self.Choose.clicked.connect(lambda: self.choose_clicked())

        self.number_of_rounds = 3
        self.round = 0
        self.victory = self.number_of_rounds//2+1
        self.user_score = 0
        self.computer_score = 0
        self.hand_list = ['rock', 'paper', 'scissor']

    def button_config_1(self):
        self.Play_Again.setText("Play again?")
        self.Play_Again.show()
        self.Quit.show()
        self.Choose.hide()
        self.choose_hand.hide()
        self.radioRock.hide()
        self.radioPaper.hide()
        self.radioScissors.hide()

    def button_config_2(self):
        self.round_result.setText('')
        self.Play_Again.hide()
        self.Quit.hide()
        self.Choose.show()
        self.choose_hand.show()
        self.radioRock.show()
        self.radioPaper.show()
        self.radioScissors.show()

    def get_user_hand(self):
        if self.radioRock.isChecked():
            user_hand = self.radioRock.text()
        elif self.radioPaper.isChecked():
            user_hand = self.radioPaper.text()
        elif self.radioScissors.isChecked():
            user_hand = self.radioScissors.text()
        else:
            user_hand = 'Status_not_selected'
        return user_hand

    def get_computer_hand(self):
        return random.choices(self.hand_list)

    def round_winner(self, user, computer):
        if user == computer:
            self.round_result.setText(f'Computer is {computer}. You are {user}. You tie.')
        elif (user == 'rock' and computer == 'scissor') or \
                (user == 'paper' and computer == 'rock') or \
                (user == 'scissor' and computer == 'paper'):
            self.round_result.setText(f'Computer is {computer}. You are {user}. You win.')
            self.user_score += 1
        else:
            self.round_result.setText(f'Computer is {computer}. You are {user}. You lose.')
            self.computer_score += 1

    def display_score(self, user_score, computer_score):
        self.user_score_disply.setText(f"Your score:           {user_score}")
        self.computer_score_disply.setText(f"Computer score:    {computer_score}")

    def play_game(self):
        self.button_config_2()
        self.group.setExclusive(True)
        self.user_score = 0
        self.computer_score = 0
        self.round = 0
        self.display_score(self.user_score, self.computer_score)

    def choose_clicked(self):
        self.round += 1
        user_hand = self.get_user_hand()
        computer_hand = self.get_computer_hand()
        self.round_winner(user_hand, computer_hand[0])
        self.display_score(self.user_score, self.computer_score)
        if (self.round >= self.number_of_rounds or self.user_score >= self.victory) or \
                (self.computer_score >= self.victory):
            self.game_over()

    def game_over(self):
        self.button_config_1()
        if self.user_score > self.computer_score:
            self.round_result.setText('GAME OVER - YOU WIN')
        elif self.user_score == self.computer_score:
            self.round_result.setText('GAME OVER _ IT\'S A TIE')
        else:
            self.round_result.setText('GAME OVER - COMPUTER WINS')
        self.group.setExclusive(False)
        self.group.checkedButton().setChecked(False)
