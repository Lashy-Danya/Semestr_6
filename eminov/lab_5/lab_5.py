import sys
import numpy as np

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel,
    QLineEdit, QHBoxLayout, QWidget, QVBoxLayout, QTextBrowser, QGridLayout
)
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lab 5 GUI")
        self.setFixedWidth(640)

        # Create widgets
        label_size = QLabel('Введите размер массива:')
        label_size.setFont(QFont('Arial', 14))
        self.input_size = QLineEdit()
        font = self.input_size.font()
        font.setPointSize(16) 
        self.input_size.setFont(font)

        label_a = QLabel('Введите A:')
        label_a.setFont(QFont('Arial', 14))
        self.input_a = QLineEdit()
        font = self.input_a.font()
        font.setPointSize(16) 
        self.input_a.setFont(font)

        label_g = QLabel('Введите G:')
        label_g.setFont(QFont('Arial', 14))
        self.input_g = QLineEdit()
        font = self.input_g.font()
        font.setPointSize(16) 
        self.input_g.setFont(font)

        # self.array_display = QTextBrowser()

        self.button = QPushButton("Результат")

        # Create layout
        input_layout_size = QHBoxLayout()
        input_layout_size.addWidget(label_size)
        input_layout_size.addWidget(self.input_size)

        input_layout_a = QHBoxLayout()
        input_layout_a.addWidget(label_a)
        input_layout_a.addWidget(self.input_a)

        input_layout_g = QHBoxLayout()
        input_layout_g.addWidget(label_g)
        input_layout_g.addWidget(self.input_g)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button)

        self.array_layout = QGridLayout()

        self.output_layout = QGridLayout()

        layout = QVBoxLayout()
        layout.addLayout(input_layout_size)
        layout.addLayout(input_layout_a)
        layout.addLayout(input_layout_g)
        layout.addLayout(button_layout)
        # layout.addWidget(self.array_display)
        layout.addLayout(self.array_layout)
        layout.addLayout(self.output_layout)

        # Set layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Connect button to function
        self.button.clicked.connect(self.generate_array)

    def generate_array(self):
        size = int(self.input_size.text())
        a = int(self.input_a.text())
        mu = int(self.input_g.text())
        # new_array_np = np.zeros(size)
        # for i in range(size):
        #     array_np = np.random.rand(12)
        #     new_array_np[i] += array_np.sum() - 6
        new_array_np = np.random.rand(size, 12)
        new_array_np = np.sum(new_array_np, axis=1) - 6
        new_array_np = new_array_np * mu + a
        # self.array_display.setPlainText(str(new_array_np))

        for i in reversed(range(self.array_layout.rowCount())):
            for j in reversed(range(self.array_layout.columnCount())):
                item = self.array_layout.itemAtPosition(i, j)
                if item is not None:
                    widget_to_remove = item.widget()
                    self.array_layout.removeWidget(widget_to_remove)
                    widget_to_remove.setParent(None)

        for row in range(5):
            for col in range(4):
                if len(new_array_np) > (4 * row + col):
                    label = QLabel(str(np.around(new_array_np[4 * row + col], 8)))
                else:
                    label = QLabel('None')
                label.setFont(QFont('Arial', 14))
                self.array_layout.addWidget(label, row, col)

        Mx = a
        m = round(new_array_np.sum() / size, 8)
        d_1 = round(abs(Mx - m), 8)
        
        Dx = mu**2
        g = round((np.power(new_array_np, 2).sum() / (size - 1)) - (size / (size - 1)) * m**2, 8)
        d_2 = round(abs(Dx - g), 8)

        for i in reversed(range(self.output_layout.rowCount())):
            for j in reversed(range(self.output_layout.columnCount())):
                item = self.output_layout.itemAtPosition(i, j)
                if item is not None:
                    widget_to_remove = item.widget()
                    self.output_layout.removeWidget(widget_to_remove)
                    widget_to_remove.setParent(None)

        label_Mx = QLabel(f'Mx = {Mx}')
        label_Mx.setFont(QFont('Arial', 14))

        label_m = QLabel(f'm = {m}')
        label_m.setFont(QFont('Arial', 14))

        label_d1 = QLabel(f'd_1 = {d_1}')
        label_d1.setFont(QFont('Arial', 14))

        label_Dx = QLabel(f'Dx = {Dx}')
        label_Dx.setFont(QFont('Arial', 14))

        label_g = QLabel(f'g = {g}')
        label_g.setFont(QFont('Arial', 14))

        label_d2 = QLabel(f'd_2 = {d_2}')
        label_d2.setFont(QFont('Arial', 14))
        
        self.output_layout.addWidget(label_Mx, 0, 1)
        self.output_layout.addWidget(label_m, 0, 2)
        self.output_layout.addWidget(label_d1, 0, 3)

        self.output_layout.addWidget(label_Dx, 1, 1)
        self.output_layout.addWidget(label_g, 1, 2)
        self.output_layout.addWidget(label_d2, 1, 3)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()