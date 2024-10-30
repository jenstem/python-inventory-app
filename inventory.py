from PyQt5.QtWidgets import QMessageBox, QPushButton, QMainWindow, QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QLabel
import sqlite3
import sys


class MainWindow(QMainWindow):
    """
    Main application window for managing product inventory.
    """

    def __init__(self):
        """
        Initializes the MainWindow, sets up the database connection,
        creates the product table, and initializes the user interface.
        """
        super().__init__()

        self.conn = sqlite3.connect("products.db")
        self.create_table()
        self.initUI()


    def load_data(self):
        """
        Loads product data from the database and populates
        the table widget
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        self.table_widget.setRowCount(len(products))

        for row, product in enumerate(products):
            for col, value in enumerate(product):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)


    def create_table(self):
        """
        Creates the products table in the database if it does not exist.
        """
        cursor = self.conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER, description TEXT, quantity INTEGER)""")
        self.conn.commit()

    
    def initUI(self):
        """
        Initializes the user interface components and layout.
        """
        self.setGeometry(0, 0, 700, 500)
        self.setWindowTitle("Inventory")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.table_widget = QTableWidget(self)
        layout.addWidget(self.table_widget)

        self.table_widget.setColumnCount(5)

        self.table_widget.setHorizontalHeaderLabels(["ID", "Name", "Price", "Description", "Quantity"])

        self.load_data()

        # Input fields
        self.name_edit = QLineEdit(self)
        self.price_edit = QLineEdit(self)
        self.description_edit = QLineEdit(self)
        self.quantity_edit = QLineEdit(self)

        layout.addWidget(QLabel("Name: "))
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("Price: "))
        layout.addWidget(self.price_edit)
        layout.addWidget(QLabel("Description: "))
        layout.addWidget(self.description_edit)
        layout.addWidget(QLabel("Quantity: "))
        layout.addWidget(self.quantity_edit)

        # Button to add a product
        add_button = QPushButton("Add Product", self)
        add_button.clicked.connect(self.add_product)
        layout.addWidget(add_button)

        # Button to delete a product
        delete_button = QPushButton("Delete Product", self)
        delete_button.clicked.connect(self.delete_product)
        layout.addWidget(delete_button)

        # Button to update a product
        update_button = QPushButton("Update Product", self)
        update_button.clicked.connect(self.update_product)
        layout.addWidget(update_button)


    def update_product(self):
        """
        Updates the selected product in the table with new values from input fields.
        """
        current_row = self.table_widget.currentRow()
        if current_row < 0 or current_row >= self.table_widget.rowCount():
            return QMessageBox.warning(self, "No row selected")

        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()
        quantity = self.quantity_edit.text().strip()

        product_id = int(self.table_widget.item(current_row, 0).text())
        cursor = self.conn.cursor()
        cursor.execute("UPDATE products SET name = ?, price = ?, description = ?, quantity = ? WHERE id = ?", (name, price, description, quantity, product_id))
        self.conn.commit()

        self.name_edit.clear()
        self.price_edit.clear()
        self.description_edit.clear()
        self.quantity_edit.clear()

        self.load_data()


    def delete_product(self):
        """
        Deletes the selected product from the table and database.
        """
        current_row = self.table_widget.currentRow()
        if current_row < 0 or current_row >= self.table_widget.rowCount():
                return QMessageBox.warning(self, "No row selected")
        product_id = int(self.table_widget.item(current_row, 0).text())
        button = QMessageBox.question(self, "Delete Product", "Are you sure you want to delete this product?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if button == QMessageBox.StandardButton.Yes:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
            self.conn.commit()

            self.name_edit.clear()
            self.price_edit.clear()
            self.description_edit.clear()
            self.quantity_edit.clear()

            self.load_data()


    def add_product(self):
        """
        Adds a new product to the table and database using values from input fields.
        """
        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()
        quantity = self.quantity_edit.text().strip()

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO products (Name, Price, Description, Quantity) VALUES (?, ?, ?, ?)", (name, price, description, quantity))
        self.conn.commit()

        self.load_data()

        self.name_edit.clear()
        self.price_edit.clear()
        self.description_edit.clear()
        self.quantity_edit.clear()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
