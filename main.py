import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QFileDialog
from datetime import datetime

import csv

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ввод даты для получения данных')
        self.setGeometry(300, 200, 400, 200)

        layout = QVBoxLayout()

        self.date_input = QLineEdit(self)
        layout.addWidget(QLabel("Введите дату (YYYY/MM/DD):"))
        layout.addWidget(self.date_input)

        self.get_data_button = QPushButton("Получить данные", self)
        self.get_data_button.clicked.connect(self.get_data)
        layout.addWidget(self.get_data_button)

        self.setLayout(layout)

    def validate_date(self, date_text):
        try:
            datetime.strptime(date_text, '%Y/%m/%d')
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
