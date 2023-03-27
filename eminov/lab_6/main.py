import sys
import numpy as np
from scipy import stats

from PyQt6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QPushButton,
    QVBoxLayout, QLabel, QLineEdit, QTabWidget, QTableWidget, QTableWidgetItem
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator

class Table(QTableWidget):
    def __init__(self, row, column, size_row, size_height):
        super().__init__()

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
        for row_ in range(self.rowCount()):
            for col_ in range(self.columnCount()):
                if len(array) > (4 * row_ + col_):
                    value = np.around(array[4 * row_ + col_], 8)
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
                    self.setItem(row_, col_, item)
                else:
                    item = QTableWidgetItem('None')
                    item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
                    self.setItem(row_, col_, item)

class InputHLayout(QHBoxLayout):
    def __init__(self, label, input):
        super().__init__()

        self.addWidget(label)
        self.addWidget(input)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Лабораторная работа №6')

        layout = QVBoxLayout()

        # Создание QTabWidget
        tab_widget = QTabWidget()

        # Создание Widgets для вкладок
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()

        # Добавление вкладок в QTabWidget
        tab_widget.addTab(tab1, "Равномерное")
        tab_widget.addTab(tab2, "Показательное")
        tab_widget.addTab(tab3, "Нормальное")

        # Наполнение 1 Tab
        title_tab1 = QLabel("Равномерное распределение")
        title_tab1.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px")

        # Создание поля ввода размера массива
        size_label_tab1, self.size_input_tab1 = self.create_input('Введите размер массива:')
        layout_tab1_size_input = InputHLayout(size_label_tab1, self.size_input_tab1)

        # Создание поля ввода переменной A
        a_label_tab1, self.a_input_tab1 = self.create_input('Введите переменную A:')
        layout_tab1_a_input = InputHLayout(a_label_tab1, self.a_input_tab1)


        # Создание поля ввода переменной B
        b_label_tab1, self.b_input_tab1 = self.create_input('Введите переменную B:')
        layout_tab1_b_input = InputHLayout(b_label_tab1, self.b_input_tab1)

        # Создание поля ввода количества интервалов
        k_label_tab1, self.k_input_tab1 = self.create_input('Введите количество интервалов:')
        layout_tab1_k_input = InputHLayout(k_label_tab1, self.k_input_tab1)

        # Создание кнопки
        input_button_tab1 = QPushButton("Результат")
        input_button_tab1.clicked.connect(self.result_uniform)

        self.array_table_tab1 = Table(6, 5, 130, 40)

        # Создание полей для вывода расчетов
        self.mx_label_tab1 = self.create_output_label()
        self.dx_label_tab1 = self.create_output_label()

        self.stat_tab1 = self.create_output_label()
        self.crit_tab1 = self.create_output_label()
        self.result_tab1 = self.create_output_label()

        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(title_tab1)
        tab1_layout.addLayout(layout_tab1_size_input)
        tab1_layout.addLayout(layout_tab1_a_input)
        tab1_layout.addLayout(layout_tab1_b_input)
        tab1_layout.addLayout(layout_tab1_k_input)
        tab1_layout.addWidget(input_button_tab1)
        tab1_layout.addWidget(self.array_table_tab1)
        tab1_layout.addWidget(self.mx_label_tab1)
        tab1_layout.addWidget(self.dx_label_tab1)
        tab1_layout.addWidget(self.stat_tab1)
        tab1_layout.addWidget(self.crit_tab1)
        tab1_layout.addWidget(self.result_tab1)

        # Наполнение 2 Tab
        title_tab2 = QLabel("Показательное распределение")
        title_tab2.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px")

        # Создание поля ввода размера массива
        size_label_tab2, self.size_input_tab2 = self.create_input('Введите размер массива:')
        layout_tab2_size_input = InputHLayout(size_label_tab2, self.size_input_tab2)

        # Создание поля ввода переменной Lamda
        lambda_label_tab2, self.lambda_input_tab2 = self.create_input('Введите переменную Lambda:')
        layout_tab2_lambda_input = InputHLayout(lambda_label_tab2, self.lambda_input_tab2)

        # Создание поля ввода количества интервалов
        k_label_tab2, self.k_input_tab2 = self.create_input('Введите количество интервалов:')
        layout_tab2_k_input = InputHLayout(k_label_tab2, self.k_input_tab2)

        # Создание кнопки
        input_button_tab2 = QPushButton("Результат")
        input_button_tab2.clicked.connect(self.result_exponential)

        self.array_table_tab2 = Table(6, 5, 130, 40)

        # Создание полей для вывода расчетов
        self.mx_label_tab2 = self.create_output_label()
        self.dx_label_tab2 = self.create_output_label()

        self.stat_tab2 = self.create_output_label()
        self.crit_tab2 = self.create_output_label()
        self.result_tab2 = self.create_output_label()

        tab2_layout = QVBoxLayout(tab2)
        tab2_layout.addWidget(title_tab2)
        tab2_layout.addLayout(layout_tab2_size_input)
        tab2_layout.addLayout(layout_tab2_lambda_input)
        tab2_layout.addLayout(layout_tab2_k_input)
        tab2_layout.addWidget(input_button_tab2)
        tab2_layout.addWidget(self.array_table_tab2)
        tab2_layout.addWidget(self.mx_label_tab2)
        tab2_layout.addWidget(self.dx_label_tab2)
        tab2_layout.addWidget(self.stat_tab2)
        tab2_layout.addWidget(self.crit_tab2)
        tab2_layout.addWidget(self.result_tab2)

        # Наполнение 3 Tab
        title_tab3 = QLabel("Нормальное распределение")
        title_tab3.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 15px")

        # Создание поля ввода размера массива
        size_label_tab3, self.size_input_tab3 = self.create_input('Введите размер массива:')
        layout_tab3_size_input = InputHLayout(size_label_tab3, self.size_input_tab3)

        # Создание поля ввода переменной A
        a_label_tab3, self.a_input_tab3 = self.create_input('Введите переменную A:')
        layout_tab3_a_input = InputHLayout(a_label_tab3, self.a_input_tab3)

        # Создание поля ввода переменной G
        g_label_tab3, self.g_input_tab3 = self.create_input('Введите переменную G:')
        layout_tab3_g_input = InputHLayout(g_label_tab3, self.g_input_tab3)

        # Создание поля ввода количества интервалов
        k_label_tab3, self.k_input_tab3 = self.create_input('Введите количество интервалов:')
        layout_tab3_k_input = InputHLayout(k_label_tab3, self.k_input_tab3)

        # Создание кнопки
        input_button_tab3 = QPushButton("Результат")
        input_button_tab3.clicked.connect(self.result_normal)

        self.array_table_tab3 = Table(6, 5, 130, 40)

        # Создание полей для вывода расчетов
        self.mx_label_tab3 = self.create_output_label()
        self.dx_label_tab3 = self.create_output_label()

        self.stat_tab3 = self.create_output_label()
        self.crit_tab3 = self.create_output_label()
        self.result_tab3 = self.create_output_label()

        tab3_layout = QVBoxLayout(tab3)
        tab3_layout.addWidget(title_tab3)
        tab3_layout.addLayout(layout_tab3_size_input)
        tab3_layout.addLayout(layout_tab3_a_input)
        tab3_layout.addLayout(layout_tab3_g_input)
        tab3_layout.addLayout(layout_tab3_k_input)
        tab3_layout.addWidget(input_button_tab3)
        tab3_layout.addWidget(self.array_table_tab3)
        tab3_layout.addWidget(self.mx_label_tab3)
        tab3_layout.addWidget(self.dx_label_tab3)
        tab3_layout.addWidget(self.stat_tab3)
        tab3_layout.addWidget(self.crit_tab3)
        tab3_layout.addWidget(self.result_tab3)

        # Добавление QTabWidget в главный QWidget
        layout.addWidget(tab_widget)

        self.setLayout(layout)

    def create_input(self, label_text):
        label = QLabel(label_text)
        input_field = QLineEdit()
        input_field.setStyleSheet("font-size: 18px")
        label.setStyleSheet("font-size: 18px; font-weight: bold")

        return label, input_field
    
    def create_output_label(self):
        label = QLabel()
        label.setStyleSheet("font-size: 18px")

        return label

    def result_uniform(self):
        size = int(self.size_input_tab1.text())
        k = int(self.k_input_tab1.text())
        a = int(self.a_input_tab1.text())
        b = int(self.b_input_tab1.text())

        array_list = np.random.rand(size)
        array_list = a + array_list * (b - a)
        
        self.array_table_tab1.set_update_table(array_list)

        Mx = (a + b) / 2
        m = round(array_list.sum() / size, 8)
        d_1 = round(abs(Mx - m), 8)
        
        Dx = round(((b - a)**2) / 12, 8)
        g = round((np.power(array_list, 2).sum() / (size - 1)) - (size / (size - 1)) * m**2, 8)
        d_2 = round(abs(Dx - g), 8)

        self.mx_label_tab1.setText(f'Mx = {Mx} \t m = {m} \t d_1 = {d_1}')
        self.dx_label_tab1.setText(f'Dx = {Dx} \t g = {g} \t d_2 = {d_2}\n')

        alpha = 0.05

        # Вычисляем ожидаемые значения для каждого интервала
        low, high = np.min(array_list), np.max(array_list)
        intervals = np.linspace(low, high, k+1)
        # вычисляем наблюдаемые частоты в каждой группе
        observed, _ = np.histogram(array_list, bins=intervals)
        # вычисляем ожидаемые частоты в каждой группе для равномерного распределения
        expected = np.ones(k) * len(array_list) / k

        # Вычисляем статистику критерия Пирсона
        stat = np.sum((observed - expected) ** 2 / expected)

        # Вычисляем критическое значение
        df = k - 1
        crit = stats.chi2.ppf(1 - alpha, df)

        self.stat_tab1.setText(f'<p>Статистика критерия Пирсона: &#967;<sup>2</sup> = {str(np.around(stat, 8))}</p>')
        self.crit_tab1.setText(f'Критическое значение Хи-квадрат:  {str(np.around(crit, 8))}')

        # Сравнение Статистики Хи-квадрат с Критическим значением
        if stat < crit:
            self.result_tab1.setText("Нулевая гипотеза принимается\n(данные соответствуют равномерному распределению)")
        else:
            self.result_tab1.setText("Нулевая гипотеза отвергается\n(данные не соответствуют нормальному распределению)")

    def result_exponential(self):
        size = int(self.size_input_tab2.text())
        k = int(self.k_input_tab2.text())
        lambd = float(self.lambda_input_tab2.text())

        array_list = np.random.rand(size)
        array_list = np.log(1 - array_list) / -lambd
        
        self.array_table_tab2.set_update_table(array_list)

        Mx = 1 / lambd
        m = round(array_list.sum() / size, 8)
        d_1 = round(abs(Mx - m), 8)
        
        Dx = round(1 / (lambd**2), 8)
        g = round((np.power(array_list, 2).sum() / (size - 1)) - (size / (size - 1)) * m**2, 8)
        d_2 = round(abs(Dx - g), 8)

        self.mx_label_tab2.setText(f'Mx = {Mx} \t m = {m} \t d_1 = {d_1}')
        self.dx_label_tab2.setText(f'Dx = {Dx} \t g = {g} \t d_2 = {d_2}\n')

        alpha = 0.05

        # Вычисляем параметр lambda показательного распределения
        lambda_estimate = 1 / np.mean(array_list)
        # Вычисляем ожидаемые значения для каждого интервала
        low, high = np.min(array_list), np.max(array_list)
        intervals = np.linspace(low, high, k+1)
        # Вычисляем наблюдаемые значения для каждой категории
        observed, _ = np.histogram(array_list, bins=intervals)
        # Вычисляем ожидаемые частоты в каждой группе
        # expected = [len(array_list) * stats.expon.cdf(intervals[i + 1], scale=1/lambda_estimate) - 
                    # len(array_list) * stats.expon.cdf(intervals[i], scale=1/lambda_estimate) for i in range(k)]
        
        expected = stats.expon.pdf((intervals[:-1] + intervals[1:]) / 2, loc=low, scale=np.mean(array_list) - low)
        expected *= len(array_list) * (intervals[1] - intervals[0])
        
        # Вычисляем статистику критерия Пирсона
        stat = np.sum((observed - expected) ** 2 / expected)

        # Вычисляем критическое значение
        # df = k - 1
        df = k - 1 - 2
        crit = stats.chi2.ppf(1 - alpha, df)

        self.stat_tab2.setText(f'<p>Статистика критерия Пирсона: &#967;<sup>2</sup> {str(np.around(stat, 8))}</p>')
        self.crit_tab2.setText(f'Критическое значение Хи-квадрат: {str(np.around(crit, 8))}')

        # Сравнение Статистики Хи-квадрат с Критическим значением
        if stat < crit:
            self.result_tab2.setText("Нулевая гипотеза принимается\n(данные соответствуют показательному распределению)")
        else:
            self.result_tab2.setText("Нулевая гипотеза отвергается\n(данные не соответствуют показательному распределению)")

    def result_normal(self):
        size = int(self.size_input_tab3.text())
        k = int(self.k_input_tab3.text())
        a = int(self.a_input_tab3.text())
        mu = int(self.g_input_tab3.text())

        array_list = np.random.rand(size, 12)
        array_list = np.sum(array_list, axis=1) - 6
        array_list = array_list * mu + a

        self.array_table_tab3.set_update_table(array_list)

        Mx = a
        m = round(array_list.sum() / size, 8)
        d_1 = round(abs(Mx - m), 8)
        
        Dx = mu**2
        g = round((np.power(array_list, 2).sum() / (size - 1)) - (size / (size - 1)) * m**2, 8)
        d_2 = round(abs(Dx - g), 8)

        self.mx_label_tab3.setText(f'Mx = {Mx} \t m = {m} \t d_1 = {d_1}')
        self.dx_label_tab3.setText(f'Dx = {Dx} \t g = {g} \t d_2 = {d_2}\n')

        alpha = 0.05

        # Вычисляем ожидаемые значения для каждого интервала
        low, high = np.min(array_list), np.max(array_list)
        intervals = np.linspace(low, high, k+1)
        # вычисляем наблюдаемые частоты в каждой группе
        observed, _ = np.histogram(array_list, bins=intervals)
        # вычисляем ожидаемые частоты в каждой группе для равномерного распределения
        expected = np.ones(k) * len(array_list) / k

        # Вычисляем статистику критерия Пирсона
        stat = np.sum((observed - expected) ** 2 / expected)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyleSheet('''
        QWidget {
            background-color: #F5F5F5;
            color: #333333;
        }
        QLabel {
            color: #3D3D3D;
        }
    ''')

    window = MainWindow()
    window.show()

    app.exec()