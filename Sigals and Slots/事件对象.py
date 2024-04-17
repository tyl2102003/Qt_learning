# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt


# 创建一个名为Example的窗口类
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.label = None
        self.initui()

    # 初始化UI界面
    def initui(self):
        grid = QGridLayout()  # 创建一个网格布局
        grid.setSpacing(15)  # 设置布局中部件之间的间距
        self.setLayout(grid)  # 设置窗口的布局为grid

        x = 0
        y = 0
        text = "x:{0}, y:{1}".format(x, y)  # 初始化标签显示的文本内容
        self.label = QLabel(text, self)  # 创建一个标签并设置初始文本
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)  # 将标签添加到布局中并设置对齐方式为顶部对齐

        self.setGeometry(500, 100, 600, 400)  # 设置窗口的位置和大小
        self.setWindowTitle("事件对象")  # 设置窗口标题
        self.show()  # 显示窗口

    # 处理鼠标移动事件的方法
    def mouseMoveEvent(self, e) -> None:
        x = e.x()
        y = e.y()
        text = "x: {0},  y: {1}".format(x, y)  # 根据鼠标的位置更新标签的文本内容
        self.label.setText(text)  # 更新标签的文本内容


# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建应用程序对象
    window = Example()  # 创建Example窗口对象
    sys.exit(app.exec_())  # 运行应用程序，进入事件循环
