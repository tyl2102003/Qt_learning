# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStyle
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initui()

    def initui(self):
        self.setWindowTitle("重构键盘事件")
        self.setGeometry(500, 100, 600, 400)
        self.show()
        self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton))

    def keyPressEvent(self, e):
        # 注意此处要写成e.key(),不能忘记加圆括号
        if e.key() == Qt.Key_Escape:
            self.close()


"""此时如果按下 ESC 键程序就会退出。"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Example()
    sys.exit(app.exec_())
