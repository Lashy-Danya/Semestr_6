import sys
import numpy as np

from PyQt6.QtWidgets import (
    QApplication, QPushButton, QLabel, QTableWidget, QTableWidgetItem,
    QLineEdit, QHBoxLayout, QWidget, QVBoxLayout, QGridLayout
)
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt

class Table(QTableWidget):
    def __init__(self, row, column, size_row, size_height, max_height):
        super().__init__()

        self.setMaximumHeight(max_height)

        self.setRowCount(row)
        self.setColumnCount(column)

        for i in range(self.rowCount()):
            self.setRowHeight(i, size_height)

        for i in range(self.columnCount()):
            self.setColumnWidth(i, size_row)

        # self.setShowGrid(False)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)

        self.setStyleSheet('''
            QTableWidget {
                border: none;
                font-size: 16px;
                font-family: Arial;
            }
            QTableWidget::item {
                padding: 5px;
            }
        ''')

    def set_update_table(self, array):
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                if len(array) > (4 * row + col):
                    value = np.around(array[4 * row + col], 8)
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
                    self.setItem(row, col, item)
                else:
                    item = QTableWidgetItem('None')
                    item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
                    self.setItem(row, col, item)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lab 3 GUI")
        self.setFixedWidth(560)
        self.setMinimumHeight(420)


        # Создание поля ввода размера массива
        size_label, self.size_input = self.create_input('Введите размер массива:')
        layout_size_input = QHBoxLayout()
        layout_size_input.addWidget(size_label)
        layout_size_input.addWidget(self.size_input)

        # Создание поля ввода переменной A
        a_label, self.a_input = self.create_input('Введите переменную A:')
        layout_a_input = QHBoxLayout()
        layout_a_input.addWidget(a_label)
        layout_a_input.addWidget(self.a_input)

        # Создание поля ввода переменной B
        b_label, self.b_input = self.create_input('Введите переменную B:')
        layout_b_input = QHBoxLayout()
        layout_b_input.addWidget(b_label)
        layout_b_input.addWidget(self.b_input)

        self.button = QPushButton("Результат")
        self.button.clicked.connect(self.generate_array)

        # Создание таблицы для отображения массива
        self.array_table = Table(5, 4, 130, 40, 200)

        # Создание полей для вывода расчетов
        self.mx_label = QLabel()
        self.mx_label.setStyleSheet("font-size: 18px")

        self.dx_label = QLabel()
        self.dx_label.setStyleSheet("font-size: 18px")

        # Создание layout с добавлением других widget
        layout = QVBoxLayout()
        layout.addLayout(layout_size_input)
        layout.addLayout(layout_a_input)
        layout.addLayout(layout_b_input)
        layout.addWidget(self.button)
        layout.addWidget(self.array_table)
        layout.addWidget(self.mx_label)
        layout.addWidget(self.dx_label)

        self.setLayout(layout)

    def create_input(self, label_text):
        label = QLabel(label_text)
        input_field = QLineEdit()
        input_field.setValidator(QIntValidator())
        input_field.setStyleSheet("font-size: 18px")
        label.setStyleSheet("font-size: 18px; font-weight: bold")

        return label, input_field

    def generate_array(self):
        size = int(self.size_input.text())
        a = int(self.a_input.text())
        b = int(self.b_input.text())
        array_np = np.random.rand(size)
        new_array_np = a + array_np * (b - a)
        
        self.array_table.set_update_table(new_array_np)

        Mx = (a + b) / 2
        m = round(new_array_np.sum() / size, 8)
        d_1 = round(abs(Mx - m), 8)
        
        Dx = round(((b - a)**2) / 12, 8)
        g = round((np.power(new_array_np, 2).sum() / (size - 1)) - (size / (size - 1)) * m**2, 8)
        d_2 = round(abs(Dx - g), 8)

        self.mx_label.setText(f'Mx = {Mx} \t m = {m} \t d_1 = {d_1}')
        self.dx_label.setText(f'Dx = {Dx} \t g = {g} \t d_2 = {d_2}')

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()