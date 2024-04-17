# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initui()

    def initui(self):
        sld = QSlider(Qt.Horizontal, self)
        scd = QLCDNumber(self)
        vlayout = QVBoxLayout()
        vlayout.addWidget(sld)
        vlayout.addWidget(scd)
        self.setLayout(vlayout)

        sld.valueChanged.connect(scd.display)

        self.setGeometry(500, 100, 600, 400)
        self.setWindowTitle("signal and slots")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Example()
    sys.exit(app.exec_())
