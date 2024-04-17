# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, qApp, QMenu, QStyle, QTextEdit
from PyQt5.QtGui import QIcon


class Meau_Status(QMainWindow):
    def __init__(self):
        super(Meau_Status, self).__init__()
        self.initui()

    def initui(self):
        # 状态栏
        self.statusBar().showMessage('hello bar')

        # 菜单栏
        exitAct = QAction('Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        edit_Menu = menubar.addMenu("Edit")
        menubar.addMenu("Play")
        menubar.addMenu("Sing")
        fileMenu.addAction(exitAct)

        # 子菜单
        edit_img = QMenu("Edit image", self)
        img_act = QAction("Rotate", self)
        compute_img = QAction("compute images", self)
        edit_img.addAction(img_act)
        edit_Menu.addMenu(edit_img)
        edit_Menu.addAction(compute_img)

        # 勾选菜单
        view_Menu = menubar.addMenu("View")
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        view_Menu.addAction(viewStatAct)

        # 工具栏
        exiticon = QApplication.style().standardIcon(QStyle.SP_BrowserStop)
        exitact = QAction(exiticon, 'close', self)
        exitact.setShortcut('Crtl+Q')
        exitact.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('close')
        self.toolbar.addAction(exitact)

        # 文本编辑区
        text_edit = QTextEdit()
        self.setCentralWidget(text_edit)

        # 设置标题和窗口大小
        self.setWindowTitle("状态栏和菜单")
        self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton))
        self.setGeometry(500, 100, 600, 600)
        self.show()

        # 右键菜单
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Meau_Status()
    sys.exit(app.exec_())
