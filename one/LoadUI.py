from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QGridLayout, QVBoxLayout, \
    QHBoxLayout, QMessageBox
import sys
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("windows.ui", self)


app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
