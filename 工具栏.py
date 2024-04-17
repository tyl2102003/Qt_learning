from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QStyle, QTextEdit


class Toolbar(QMainWindow):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.initui()

    def initui(self):
        exiticon = QApplication.style().standardIcon(QStyle.SP_BrowserStop)
        exitact = QAction(exiticon, 'close', self)
        exitact.setShortcut('Crtl+Q')
        exitact.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('close')
        self.toolbar.addAction(exitact)

        self.setWindowTitle("工具栏")
        self.resize(800, 600)
        self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton))
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    windows = Toolbar()
    app.exec_()
