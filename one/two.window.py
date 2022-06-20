from PyQt6.QtWidgets import QApplication,QMainWindow
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.statusBar().showMessage("Welcome to PyQt")
window.menuBar().setNativeMenuBar(False)
window.menuBar().addMenu("File")
# mac上必须带

window.show()

sys.exit(app.exec())