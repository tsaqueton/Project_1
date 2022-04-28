
from Project_1_controller import *


def main():
    """
    function main is the model which runs the rock-paper-scissors program (opens window, controller, and closes window)
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
