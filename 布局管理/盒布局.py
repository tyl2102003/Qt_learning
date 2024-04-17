from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QWidget

"""使用盒布局能让程序具有更强的适应性。这个才是布局一个应用的更合适的方式。
QHBoxLayout 和 QVBoxLayout 是基本的布局类，分别是水平布局和垂直布局。"""

class BoxLayout(QWidget):
    def __init__(self):
        super(BoxLayout, self).__init__()
        self.initui()

    def initui(self):
        # 水平布局
        # 注意QHBoxLayout()不能加参数self
        hlayout = QHBoxLayout()
        ok_button = QPushButton("OK", self)
        cancel_button = QPushButton('Cancel', self)
        hlayout.addStretch(1)
        hlayout.addWidget(ok_button)
        hlayout.addWidget(cancel_button)

        # 垂直布局
        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)

        self.setWindowTitle("盒子布局")
        self.setGeometry(500, 100, 600, 400)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = BoxLayout()
    app.exec_()
