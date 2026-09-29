from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QDoubleSpinBox, QDateEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QMessageBox, QDialog, QScrollArea, QWidget
)
from PyQt6.QtGui import QFont , QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt , QDate

from features.savings_goal.service3 import ServiceGoal
from features.savings_goal.model3 import SavingsGoal
from features.savings_management.service import SavingsService

class SavingsGoalPage(QFrame):
    def __init__(self, service_goal: ServiceGoal):
        super().__init__()
        self.service_goal = service_goal
        self.setStyleSheet("""
                    SavingsGoalPage {
                        background-color: white; 
                        border-radius: 10px; 
                        padding: 12px;
                    }
                    QPushButton {
                        background-color: #19572a;
                        color: white;
                        border-radius: 5px;
                        padding: 6px 10px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #144421;
                    }
                """)
        self.init_ui()

    def init_ui(self):

        self.goal_layout = QVBoxLayout()
        self.setLayout(self.goal_layout)

        header_layout = QHBoxLayout()

        self.savingsgoal_label = QLabel("Add Goals", self)
        self.savingsgoal_label.setFont(QFont('Arial', 30, weight=QFont.Weight.Bold))
        self.savingsgoal_label.setStyleSheet("color: #19572a;")
        header_layout.addWidget(self.savingsgoal_label)

        self.goalButton = QPushButton("Add Goal", self)
        self.goalButton.setObjectName("addGoalBtn")
        self.goalButton.setFixedHeight(40)
        self.goalButton.setFixedWidth(120)
        self.goalButton.clicked.connect(self.goals_box)
        header_layout.addWidget(self.goalButton, alignment=Qt.AlignmentFlag.AlignTop)

        self.goal_layout.addLayout(header_layout)

        self.goal_card = QFrame()
        self.goal_card.setStyleSheet("background-color: white; border: 1px solid #e0f2f1;")
        self.goal_card.setMinimumSize(600, 450)

        recent_layout = QVBoxLayout(self.goal_card)

        self.goals_label = QLabel("Active Goals", self)
        self.goals_label.setFont(QFont('Arial', 15, weight=QFont.Weight.Bold))
        self.goals_label.setStyleSheet("color: #19572a; border: none;")
        self.goals_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        recent_layout.addWidget(self.goals_label)

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setStyleSheet("background-color: transparent; border: none; outline: none;")

        self.scroll_content = QWidget()
        self.scroll_content.setStyleSheet("background-color: transparent; border: none;")
        self.goals_layout = QVBoxLayout(self.scroll_content)
        self.goals_layout.setSpacing(5)
        self.goals_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        scrollArea.setWidget(self.scroll_content)
        recent_layout.addWidget(scrollArea)

        self.goal_layout.addWidget(self.goal_card)
        self.goal_layout.addStretch()

    def goals_box(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Savings Goal")
        dialog.setStyleSheet("background-color: #E8F5E9")
        dialog.setFixedSize(320, 380)

        layout = QVBoxLayout(dialog)
        layout.setSpacing(4)
        layout.setContentsMargins(20, 20, 20, 20)

        self.head_label = QLabel("Add Savings Goal")
        self.head_label.setFont(QFont('Arial', 14, weight=QFont.Weight.Bold))
        self.head_label.setStyleSheet("color: #19572a;")
        self.head_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.head_label)

        layout.addSpacing(20)

        self.goalTitle = QLabel("Goal Title", self)
        self.goalTitle.setFont(QFont('Arial', 10, weight=QFont.Weight.Bold))
        self.goalTitle.setStyleSheet("color: #19572a;")
        layout.addWidget(self.goalTitle)

        self.title = QLineEdit()
        self.title.setStyleSheet("color: #19572a; font-size: 12px; background-color: white;")
        layout.addWidget(self.title)

        self.goal_amount = QLabel("Target Amount", self)
        self.goal_amount.setFont(QFont('Arial', 10, weight=QFont.Weight.Bold))
        self.goal_amount.setStyleSheet("color: #19572a;")
        layout.addWidget(self.goal_amount)

        self.target_amount = QLineEdit()
        self.target_amount.setStyleSheet("color: #19572a; font-size: 12px; background-color: white;")
        layout.addWidget(self.target_amount)

        self.date_label = QLabel("Target Date", self)
        self.date_label.setFont(QFont('Arial', 10, weight=QFont.Weight.Bold))
        self.date_label.setStyleSheet("color: #19572a;")
        layout.addWidget(self.date_label)

        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.date_box.setCalendarPopup(True)
        self.date_box.setStyleSheet("color: #19572a; font-size: 12px; background-color: white;")
        layout.addWidget(self.date_box)

        layout.addStretch()

        add_goal_btn = QPushButton("Add Goal")
        add_goal_btn.setFixedHeight(35)
        add_goal_btn.setStyleSheet("background-color: #22573a;")
        add_goal_btn.clicked.connect(lambda: self.add_goal(dialog))

        layout.addWidget(add_goal_btn)

        dialog.exec()

    def goals_frame(self , goals : SavingsGoal):
        self.item_frame_goal = QFrame()
        self.item_frame_goal.setFixedHeight(80)
        self.item_frame_goal.setStyleSheet("background-color: #f8fbf9; border: 1px solid #e0f2f1; border-radius: 8px;")

        item_goal_layout = QHBoxLayout(self.item_frame_goal)
        item_goal_layout.setContentsMargins(10, 0, 10, 0)
        item_goal_layout.setSpacing(8)
        item_goal_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        icon_label = QLabel("Goals")
        icon_label.setFont(QFont("Arial", 10, weight=QFont.Weight.Bold))
        icon_label.setFixedSize(40, 40)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setStyleSheet(f"background-color: green; color: white; border-radius: 0px; border: none;")
        item_goal_layout.addWidget(icon_label, 0, Qt.AlignmentFlag.AlignVCenter)

        text_container = QWidget()
        text_container.setStyleSheet("background-color: transparent; border: none;")
        text_layout = QVBoxLayout(text_container)
        text_layout.setSpacing(1)
        text_layout.setContentsMargins(0, 0, 0, 0)
        text_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)


        pass

    def add_goal(self, dialog) -> None:
        goal_title = self.title.text()
        target_amount = self.target_amount.text()
        target_date = self.date_box.date().toString("yyyy-MM-dd")

        msg_font = QFont("Arial", 11)
        white_bg_style = """
                                   QMessageBox {
                                       background-color: #5c826f;
                                   }
                                   QMessageBox QLabel {
                                       color: white;
                                       background-color: transparent;
                                       border: none;
                                   }
                                   QMessageBox QPushButton { 
                                       background-color: #ffffff; 
                                       color: #19572a; 
                                       border-radius: 4px; 
                                       min-width: 30px;
                                       min-height: 10px;
                                       font-weight: bold; 
                                       border: none;
                                   }
                                   QMessageBox QPushButton:hover { 
                                       background-color: #e0f2f1; 
                                   }
                               """

        try:
            new_goals = SavingsGoal(title=goal_title,
                               target_amount=target_amount,
                               target_date=target_date)
        except ValueError as e:
            msg = QMessageBox(QMessageBox.Icon.Warning, "Invalid Input", str(e))
            msg.setFont(msg_font)
            msg.setStyleSheet(white_bg_style)
            msg.exec()
            return

        #for confirmation
        msg = QMessageBox(
            QMessageBox.Icon.Question,
            "Confirm",
            "Are you sure you want to submit this transaction?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,

        )
        msg.setFont(msg_font)
        msg.setStyleSheet(white_bg_style)

        if msg.exec() == QMessageBox.StandardButton.Yes:

            self.service_goal.add_goal(new_goals)

            info_msg = QMessageBox(
                QMessageBox.Icon.Information, "Success", "Goals saved successfully!"
            )
            info_msg.setFont(msg_font)
            info_msg.setStyleSheet(white_bg_style)
            info_msg.exec()

            self.title.clear()
            self.target_amount.clear()
            self.date_box.setDate(QDate.currentDate())

        else:
            cancel_msg = QMessageBox(
                QMessageBox.Icon.Information, "Message", "Transaction Cancelled"
            )
        cancel_msg.setFont(msg_font)
        cancel_msg.setStyleSheet(white_bg_style)
        cancel_msg.exec()
        dialog.accept()

    def delete_goals(self) -> None:
        pass
