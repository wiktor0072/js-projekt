import sys
from PySide6.QtWidgets import QApplication
from MainWindow import Ui_MainWindow


def run():
    app = QApplication(sys.argv)
    wn = Ui_MainWindow()
    app.exec()


if __name__ == '__main__':
    run()
