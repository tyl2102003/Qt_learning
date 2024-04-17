import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QHBoxLayout, QVBoxLayout

"""有时候我们会想知道是哪个组件发出了一个信号，PyQt5 里的 sender() 方法能搞定这件事,
sender() 方法返回发出信号的组件对象，我们可以用它来确定是哪个按钮被按下了。"""


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)
        btn1.move(50, 50)
        btn2.move(250, 50)

        # 布局这段代码无效，因为继承的是QMainwindow
        # hlayout = QHBoxLayout()
        # hlayout.addStretch(1)
        # hlayout.addWidget(btn1)
        # hlayout.addWidget(btn2)
        # vlayout = QVBoxLayout()
        # vlayout.addStretch(1)
        # vlayout.addLayout(hlayout)
        # self.setLayout(vlayout)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)



        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
