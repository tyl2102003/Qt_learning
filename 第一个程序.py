# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initui()

    def initui(self):
        self.resize(800, 600)
        self.setWindowTitle("first application")
        self.show()
        # window = QMainWindow()
        # window.resize(800, 600)
        # window.setWindowTitle("first")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    sys.exit(app.exec_())
