from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QIcon, QFont, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Tutorial")
        self.setWindowIcon(QIcon("python.png"))

        '''
        label = QLabel(self)
        pixmap = QPixmap("python.png")
        label.setPixmap(pixmap)
        '''

        label = QLabel(self)
        movie = QMovie("sky.gif")
        movie.setSpeed(100)
        label.setMovie(movie)
        movie.start()

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())