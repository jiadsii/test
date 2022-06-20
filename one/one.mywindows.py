from PyQt6.QtWidgets import QApplication, QWidget
import sys
# 导入PyQt6
app = QApplication(sys.argv)

window = QWidget()
window.show()

sys.exit(app.exec())