from PyQt5.QtWidgets import QMenu, QMessageBox, QToolBar, QPushButton, QSpinBox, QMainWindow, QApplication
import sys


products = [
    {"name": "apple", "price": 1.0, "description": "Honeycrisp Apples"},
    {"name": "banana", "price": 1.5, "description": "Bunch of Organic Bananas"},
    {"name": "cherry", "price": 2.0, "description": "1lb Bag of Cherries"},
    {"name": "dates", "price": 3.0, "description": "1lb Bag of Dates"},
    {"name": "elderberry", "price": 4.0, "description": "1 Pint of Elderberries"},
]


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 500)
        self.setWindowTitle("Inventory")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()