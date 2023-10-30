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

    def get_data(self):
        date = self.date_input.text()

        if self.validate_date(date):
            file_path, _ = QFileDialog.getOpenFileName(self, 'Выберите файл dataset.csv', '', 'CSV files (*.csv)')

            if file_path:
                data_for_date = []
                with open(file_path, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    next(reader)  # Пропускаем заголовок, если он есть
                    data_for_date = [row[1] for row in reader if row[0] == date]

                if data_for_date:
                    result_text = f"Данные для даты {date}: {data_for_date[0]}"
                    QMessageBox.information(self, "Результат", result_text)
                else:
                    QMessageBox.warning(self, "Ошибка", "Данные для введенной даты отсутствуют.")
            else:
                QMessageBox.warning(self, "Ошибка", "Файл не выбран.")
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный формат даты. Введите в формате YYYY/MM/DD.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
