from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication, QStyle)
import sys

'''QFileDialog 给用户提供文件或者文件夹选择的功能。能打开和保存文件'''

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()  # 开启状态栏，若没有无法显示openFile.setStatusTip('Open new File')

        # 设置动作与信号连接
        openFile = QAction(QApplication.style().standardIcon(QStyle.SP_DirOpenIcon), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        # 设置菜单栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        # 设置窗口大小与标题栏
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.', "(*.png *.jpg *.bmp)")
        if fname[0]:
            f = open(fname[0], 'r')
            print(fname[0])
            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
