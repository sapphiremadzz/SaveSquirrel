from PyQt6.QtWidgets import (QLabel, QWidget, QPushButton
, QFrame, QLineEdit, QComboBox, QMessageBox,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QDateEdit, QTabWidget, QTableWidgetItem,
                             QTableWidget, QHeaderView, QAbstractItemView, QDialog)
from PyQt6.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt, QDate

from features.savings_management.service import SavingsService
from features.savings_management.model import Savings

# dictionary, this is for the combobox
data = {
    "Income": ["Allowance", "Salary", "Pension", "Stipend", "Other"],
    "Expense": ["Transportation", "Food", "Bills", "Travels", "Shopping", "Tuition", "Other"]
}


# THIS CLASS IS FOR TRANSACTIONS VIEWING (WITH UI)
# this class inherit QFrame
class TransactionPage(QFrame):
    def __init__(self, service: SavingsService, dashboard_page=None):
        super().__init__()
        self.service = service

        self.setStyleSheet("background-color: white; border-radius: 10px; padding: 12px;")

        self.dashboard_page = dashboard_page
        self.initUI()

    def initUI(self):
        # the main layout
        self.transaction_layout = QVBoxLayout()
        self.setLayout(self.transaction_layout)

        self.header()

        self.transactionBox_layout()

    def header(self):
        # Main Page Title Header
        self.transaction_label = QLabel("Add Transaction", self)
        self.transaction_label.setFont(QFont('Arial', 30, weight=QFont.Weight.Bold))
        self.transaction_label.setStyleSheet("color: #19572a;")
        self.transaction_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.transaction_layout.addWidget(self.transaction_label)

    def transactionBox_layout(self):
        # this is the containter para sa mga input fields
        self.transaction_box = QFrame()
        self.transaction_box.setStyleSheet("background-color: #c5e3ce; border-radius: 8px;")

        # Set tight margins and vertical spacing inside the container
        box_layout = QVBoxLayout()
        box_layout.setContentsMargins(15, 15, 15, 15)  # reduced padding around the inside of the box
        box_layout.setSpacing(6)  # smaller vertical gap between rows
        box_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.transaction_box.setLayout(box_layout)

        # Grid layout for Type and Category
        type_cat_grid = QGridLayout()
        type_cat_grid.setSpacing(6)  # reduced grid spacing

        # labels for type and category
        self.type_label = QLabel("Type", self)
        self.type_label.setFont(QFont('Arial', 11, weight=QFont.Weight.Bold))
        self.type_label.setStyleSheet("color: #19572a;")
        self.type_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.category_label = QLabel("Category", self)
        self.category_label.setFont(QFont('Arial', 11, weight=QFont.Weight.Bold))
        self.category_label.setStyleSheet("color: #19572a;")
        self.category_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # THIS IS FOR THE COMBOBOXES
        self.model = QStandardItemModel()

        self.comboType = QComboBox()
        self.comboType.setFont(QFont('Arial', 10))
        self.comboType.setFixedHeight(32)  # fixed compact height
        self.comboType.setStyleSheet("background-color: white; color: #19572a; border-radius: 5px; padding: 2px 8px;")
        self.comboType.setModel(self.model)

        self.comboCategory = QComboBox()
        self.comboCategory.setFont(QFont('Arial', 10))
        self.comboCategory.setFixedHeight(32)  # fixed compact height
        self.comboCategory.setStyleSheet(
            "background-color: white; color: #19572a; border-radius: 5px; padding: 2px 8px;")
        self.comboCategory.setModel(self.model)

        # Custom category field
        self.edit_custom_category = QLineEdit()
        self.edit_custom_category.setPlaceholderText("Enter custom category...")
        self.edit_custom_category.setFont(QFont('Arial', 10))
        self.edit_custom_category.setFixedSize(400,30)
        self.edit_custom_category.setStyleSheet(
            "color: #19572a; background-color: white; border-radius: 4px; padding: 4px;")
        self.edit_custom_category.hide()

        self.comboCategory.currentIndexChanged.connect(self.on_category_changed)

        for k, v in data.items():
            type = QStandardItem(k)
            self.model.appendRow(type)
            for value in v:
                category = QStandardItem(value)
                type.appendRow(category)

        self.comboType.currentIndexChanged.connect(self.updateType_combo)
        self.updateType_combo(0)

        type_cat_grid.addWidget(self.type_label, 0, 0)
        type_cat_grid.addWidget(self.comboType, 1, 0)
        type_cat_grid.addWidget(self.category_label, 0, 1)
        type_cat_grid.addWidget(self.comboCategory, 1, 1)
        type_cat_grid.addWidget(self.edit_custom_category, 2, 1)

        # AMOUNT FIELD
        self.amount_label = QLabel("Enter amount", self)
        self.amount_label.setFont(QFont('Arial', 11, weight=QFont.Weight.Bold))
        self.amount_label.setStyleSheet("color: #19572a;")

        self.edit_amount = QLineEdit()
        self.edit_amount.setFont(QFont('Arial', 10))
        self.edit_amount.setFixedHeight(32)
        self.edit_amount.setStyleSheet("color: #19572a; background-color: white; border-radius: 4px; padding: 4px;")

        # DESCRIPTION FIELD
        self.description_label = QLabel("Description", self)
        self.description_label.setFont(QFont('Arial', 11, weight=QFont.Weight.Bold))
        self.description_label.setStyleSheet("color: #19572a;")

        self.edit_description = QLineEdit()
        self.edit_description.setFont(QFont('Arial', 10))
        self.edit_description.setPlaceholderText("(optional)")
        self.edit_description.setFixedHeight(32)
        self.edit_description.setStyleSheet(
            "color: #19572a; background-color: white; border-radius: 4px; padding: 4px;")

        # DATE FIELD
        self.date_label = QLabel("Date", self)
        self.date_label.setFont(QFont('Arial', 11, weight=QFont.Weight.Bold))
        self.date_label.setStyleSheet("color: #19572a;")

        self.date_box = QDateEdit()
        self.date_box.setFont(QFont('Arial', 10))
        self.date_box.setFixedHeight(32)
        self.date_box.setDate(QDate.currentDate())
        self.date_box.setCalendarPopup(True)
        self.date_box.setStyleSheet("color: #19572a; background-color: white; border-radius: 4px; padding: 4px;")

        # SUBMIT BUTTON
        self.submit_transaction = QPushButton("Submit Transaction", self)
        self.submit_transaction.setFont(QFont('Arial', 10, weight=QFont.Weight.Bold))
        self.submit_transaction.setFixedHeight(38)
        self.submit_transaction.setStyleSheet("color: white; background-color: #22573a; border-radius: 5px;")
        self.submit_transaction.clicked.connect(self.add_transactionClicked)

        # Add widgets directly into box_layout (no need for redundant extra sub-layouts)
        box_layout.addLayout(type_cat_grid)

        box_layout.addSpacing(4)
        box_layout.addWidget(self.amount_label)
        box_layout.addWidget(self.edit_amount)

        box_layout.addSpacing(4)
        box_layout.addWidget(self.description_label)
        box_layout.addWidget(self.edit_description)

        box_layout.addSpacing(4)
        box_layout.addWidget(self.date_label)
        box_layout.addWidget(self.date_box)

        box_layout.addSpacing(10)
        box_layout.addWidget(self.submit_transaction)

        self.transaction_layout.addWidget(self.transaction_box)
        self.transaction_layout.addStretch()  # Pushes everything to the top to prevent awkward vertical stretching

    # handles toggling visibility of the custom category line edit based on selected combobox text
    def on_category_changed(self):
        if self.comboCategory.currentText().strip().lower() == "other":
            self.edit_custom_category.show()
        else:
            self.edit_custom_category.hide()
            self.edit_custom_category.clear()

    # this function is responsible for changing the categories based on the selected transaction type.
    def updateType_combo(self, index):
        indx = self.model.index(index, 0, self.comboType.rootModelIndex())
        """sets the selected transaction type as the root index of the category ComboBox,
               allowing it to display only the child categories associated with that transaction type.
               so for example if users chooses expenses,
               then its categories [transportation, food, bills, etc...] will display"""
        self.comboCategory.setRootModelIndex(indx)
        self.comboCategory.setCurrentIndex(0)
        self.on_category_changed()  # check and update visibility of custom category input field

    # this part is on the transaction page where if the users click the submit button,
    # there is a messagebox that will pop up,
    def add_transactionClicked(self):
        trans_type = self.comboType.currentText()

        # check if category selected is 'Other', and extract text from custom category input line edit
        if self.comboCategory.currentText().strip().lower() == "other":
            custom_cat = self.edit_custom_category.text().strip()
            category = custom_cat if custom_cat else "Other"
        else:
            category = self.comboCategory.currentText()

        amount_text = self.edit_amount.text()
        description = self.edit_description.text()
        dates = self.date_box.date().toString("yyyy-MM-dd")

        msg_font = QFont("Arial", 11)
        # for style sheet
        white_bg_style = """
           QMessageBox {
               background-color: #5c826f;
           }
           QMessageBox QLabel {
               color: white;
               background-color: transparent;
               border: none;
               font-size: 13px;
           }
           QMessageBox QPushButton { 
               background-color: #ffffff; 
               color: #19572a; 
               border-radius: 4px; 
               min-width: 40px;
               min-height: 20px;
               padding: 4px 12px;
               font-weight: bold; 
               border: none;
           }
           QMessageBox QPushButton:hover { 
               background-color: #e0f2f1; 
           }
       """

        # Hand off logic and validation
        # before this save on the databases, we must validate if the amount enter is valid
        try:
            valid_amount = self.service.validate_amount(amount_text)
        except ValueError as e:
            msg = QMessageBox(QMessageBox.Icon.Warning, "Invalid Input", str(e))
            msg.setFont(msg_font)
            msg.setStyleSheet(white_bg_style)
            msg.exec()
            return

        # this is for the confirmation
        # this will pop up if your inputs are valid
        msg = QMessageBox(
            QMessageBox.Icon.Question,
            "Confirm",
            "Are you sure you want to submit this transaction?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,

        )
        msg.setFont(msg_font)
        msg.setStyleSheet(white_bg_style)

        if msg.exec() == QMessageBox.StandardButton.Yes:
            # instantiate the new Savings object and assign the form inputs to its attributes
            new_savings = Savings(
                trans_type=trans_type,
                category=category,
                amount=valid_amount,
                description=description,
                date=dates
            )
            # if users select yes, this will save to the database through service class

            self.service.add_transaction(new_savings)

            # update the dashboard page, especially if theres new transactions, amounts on the dashboard will also change
            if self.dashboard_page:
                self.dashboard_page.refresh_recent_transactions()

            # this will pop up if your transaction is success and save to the database
            info_msg = QMessageBox(
                QMessageBox.Icon.Information, "Success", "Transaction saved successfully!"
            )
            info_msg.setFont(msg_font)
            info_msg.setStyleSheet(white_bg_style)
            info_msg.exec()

            # for cleaning input fields after it save
            self.edit_amount.clear()
            self.edit_description.clear()
            self.edit_custom_category.clear()
            self.date_box.setDate(QDate.currentDate())
            self.comboType.setCurrentIndex(0)
            self.updateType_combo(0)
        else:
            # this will pop up if users select no, meaning transaction was failed or cancelled
            cancel_msg = QMessageBox(
                QMessageBox.Icon.Information, "Message", "Transaction Cancelled"
            )
            cancel_msg.setFont(msg_font)
            cancel_msg.setStyleSheet(white_bg_style)
            cancel_msg.exec()