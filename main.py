#!-*- coding: utf-8 -*-
import cv2
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtGui import QWheelEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QGraphicsPixmapItem, QGraphicsItem
from PyQt5.QtWidgets import QGraphicsView

import untitled


class GraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(self.AnchorUnderMouse)

    def wheelEvent(self, e: QWheelEvent):
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        if e.angleDelta().y() > 0:
            self.scale(1.1, 1.1)
        else:
            self.scale(1 / 1.1, 1 / 1.1)
        self.setTransformationAnchor(self.AnchorUnderMouse)


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.ui = untitled.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionopen.triggered.connect(self.showImage)
        #
        self.graphicsView = GraphicsView()
        self.ui.verticalLayout.addWidget(self.graphicsView)
        self.scene = QGraphicsScene()  # 创建画布
        self.graphicsView.setScene(self.scene)  # 把画布添加到窗口
        self.graphicsView.show()

    def showImage(self):
        qFile = QFileDialog.getOpenFileName(self, "Page Designer - Add Pixmap", "",
                                            "Pixmap Files (*.bmp *.jpg *.png *.xpm)")
        print(qFile)
        if not qFile[0]:
            print("no image select, to return")
            return
        img = cv2.imread(qFile[0])
        cvimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 把opencv 默认BGR转为通用的RGB
        y, x = img.shape[:-1]
        frame = QImage(cvimg, x, y, QImage.Format_RGB888)
        # 清除scene残留
        self.scene.clear()
        self.pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(QPixmap(frame))
        item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.scene.addItem(item)
        # # 平滑缩放，平滑后看不到像素点块
        # item.setTransformationMode(Qt.SmoothTransformation)
        # 让image填充显示窗口
        self.graphicsView.fitInView(item, Qt.KeepAspectRatio)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyMainWindow()
    main.show()
    sys.exit(app.exec_())
