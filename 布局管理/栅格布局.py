import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

"""最常用的还是栅格布局了。这种布局是把窗口分为行和列。创建和使用栅格布局，需要使用 QGridLayout 模块。"""


class GridLayout(QWidget):
    def __init__(self):
        super(GridLayout, self).__init__()
        self.initui()

    def initui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            button.setMinimumHeight(60)
            grid.addWidget(button, *position)

        self.setWindowTitle("栅格布局")
        self.setGeometry(500, 100, 600, 400)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GridLayout()
    sys.exit(app.exec_())
