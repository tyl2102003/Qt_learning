# -*- coding: utf-8 -*-
import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class LogUi(QWidget):
    def __init__(self):
        super(LogUi, self).__init__()
        self.ui = None
        self.init_ui()
        
    def init_ui(self):
        self.ui = uic.loadUi("login.ui")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogUi()
    window.ui.show()
    sys.exit(app.exec_())
    