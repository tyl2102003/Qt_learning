# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QColorDialog, QFrame, QPushButton, QHBoxLayout
from PyQt5.QtGui import QColor

'''QColorDialog 提供颜色的选择'''


class ColorSelect(QWidget):
    def __init__(self):
        super(ColorSelect, self).__init__()
        self.init_ui()

    def init_ui(self):
        bt = QPushButton('Color Select')
        self.pannel = QFrame()
        bt.clicked.connect(self.showDialog)

        # 初始化 QtGui.QFrame 的背景颜色。
        color = QColor(0, 0, 0)
        self.pannel.setStyleSheet("QWidget { background-color: %s }"
                                  % color.name())
        # 添加布局
        hbox = QHBoxLayout()
        hbox.addWidget(bt)
        hbox.addWidget(self.pannel)
        self.setLayout(hbox)

    # 我们可以预览颜色，如果点击取消按钮，没有颜色值返回，如果颜色是我们想要的，就从取色框里选择这个颜色。
    def showDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.pannel.setStyleSheet("QWidget { background-color: %s }"
                                      % color.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ColorSelect()
    win.show()
    sys.exit(app.exec_())
