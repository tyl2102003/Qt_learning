# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QInputDialog, QLineEdit, QHBoxLayout


class Dialog(QWidget):

    def __init__(self):
        super(Dialog, self).__init__()
        self.init_ui()

    def init_ui(self):
        dl = QPushButton("button")
        self.el = QLineEdit()
        dl.clicked.connect(self.show_dialog)

        hbox = QHBoxLayout()
        hbox.addWidget(dl)
        hbox.addWidget(self.el)
        self.setLayout(hbox)

    def show_dialog(self):
        text, ok = QInputDialog.getText(self, "input dialog", 'enter your name')
        if ok:
            self.el.setText(str(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
