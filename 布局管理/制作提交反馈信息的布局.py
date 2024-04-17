import sys
from  PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QTextEdit, QLabel

"""组件能跨列和跨行展示，这个例子里，"""

class Reviewer(QWidget):
    def __init__(self):
        super(Reviewer, self).__init__()
        self.initui()

    def initui(self):
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(20)

        question = QLabel("question")
        author = QLabel("author")
        review = QLabel("review edit")

        q_line = QLineEdit()
        q_line.setMinimumHeight(50)
        a_line = QLineEdit()
        edit  = QTextEdit()

        grid.addWidget(question, 0, 0)
        grid.addWidget(q_line, 0, 1)
        grid.addWidget(author, 1, 0)
        grid.addWidget(a_line, 1, 1)
        grid.addWidget(review, 2, 0)
        grid.addWidget(edit, 2, 1, 5, 1)

        self.setWindowTitle("Review")
        self.setGeometry(500, 100, 600, 400)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Reviewer()
    sys.exit(app.exec_())
