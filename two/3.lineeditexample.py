from PyQt6.QtGui import QAction, QIcon, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox, QWidget, QLineEdit
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("LineEdit Example")

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Arial", 20))
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("python"))
window = Window()
window.show()
sys.exit(app.exec())