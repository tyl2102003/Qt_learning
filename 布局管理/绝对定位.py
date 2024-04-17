import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

"""我们使用 move() 方法定位了每一个元素，使用 x、y 坐标。x、y 坐标的原点是程序的左上角。"""

class Absolute(QWidget):
    def __init__(self):
        super(Absolute, self).__init__()
        self.initui()

    def initui(self):
        label1 = QLabel("first label", self)
        label1.move(50, 50)
        label2 = QLabel("second label", self)
        label2.move(100, 100)
        label3 = QLabel("third label", self)
        label3.move(150, 150)

        self.setWindowTitle("绝对定位")
        self.setGeometry(500, 100, 600, 400)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Absolute()
    sys.exit(app.exec_())