from PyQt5.QtWidgets import QMenu, QMessageBox, QToolBar, QPushButton, QSpinBox, QMainWindow, QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QLabel
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.products = [
        {"Name": "Apple", "Price": 1.0, "Description": "Honeycrisp Apples"},
        {"Name": "Banana", "Price": 1.5, "Description": "Bunch of Organic Bananas"},
        {"Name": "Cherry", "Price": 2.0, "Description": "1lb Bag of Cherries"},
        {"Name": "Dates", "Price": 3.0, "Description": "1lb Bag of Dates"},
        {"Name": "Elderberry", "Price": 4.0, "Description": "1 Pint of Elderberries"},
]
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 500)
        self.setWindowTitle("Inventory")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.table_widget = QTableWidget(self)
        layout.addWidget(self.table_widget)

        self.table_widget.setRowCount(len(self.products))
        self.table_widget.setColumnCount(len(self.products[0]))

        self.table_widget.setHorizontalHeaderLabels(self.products[0].keys())

        for row, product in enumerate(self.products):
            for col, value in enumerate(product.values()):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Input fields
        self.name_edit = QLineEdit(self)
        self.price_edit = QLineEdit(self)
        self.description_edit = QLineEdit(self)

        layout.addWidget(QLabel("Name: "))
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("Price: "))
        layout.addWidget(self.price_edit)
        layout.addWidget(QLabel("Description: "))
        layout.addWidget(self.description_edit)

        # Button to add product
        add_button = QPushButton("Add Product", self)
        add_button.clicked.connect(self.add_product)
        layout.addWidget(add_button)

    # Add product to the table
    def add_product(self):
        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()

        new_product = {"Name": name, "Price": price, "Description": description}
        self.products.append(new_product)

        row_position = len(self.products) - 1
        self.table_widget.insertRow(row_position)
        for col, value in enumerate(new_product.values()):
            item = QTableWidgetItem(str(value))
            self.table_widget.setItem(row_position, col, item)
            self.name_edit.clear()
            self.price_edit.clear()
            self.description_edit.clear()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()