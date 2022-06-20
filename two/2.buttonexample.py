from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QMenu
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Button Example")
        # mac 不行
        # self.setWindowIcon(QIcon("python.png"))
        self.create_button()

    def create_button(self):
        # Mac OS X
        btn = QPushButton("Click Me", self)
        btn.setGeometry(100, 100, 130, 30)
        btn.setFont(QFont("Arial", 20))
        btn.setIcon(QIcon("python.png"))
        btn.setIconSize(QSize(36, 36))

        # pop menu
        menu = QMenu()
        menu.setFont(QFont("Arial", 20))
        menu.setStyleSheet("background-color: red")
        menu.addAction("Copy")
        menu.addAction("Paste")
        menu.addAction("Cut")
        btn.setMenu(menu)


app = QApplication(sys.argv)
# mac只能用 QApplication(sys.argv)
app.setWindowIcon(QIcon("python.png"))
window = Window()
window.show()
app.exec()
