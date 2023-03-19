import sys
import numpy as np
from scipy import stats

from PyQt6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QPushButton, QMainWindow,
    QVBoxLayout, QLabel, QLineEdit, QTabWidget
)
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Лабораторная работа №6')

        # Создание поля ввода последовательности
        label_input_array = QLabel('Введите массив значений:')
        label_input_array.setFont(QFont('Arial', 12))
        self.input_array = QLineEdit()
        self.set_font(self.input_array)

        layout_input_array = QHBoxLayout()
        layout_input_array.addWidget(label_input_array)
        layout_input_array.addWidget(self.input_array)

        # Создание поля ввода количества интервалов
        label_input_k = QLabel("Введите количество интервалов:")
        label_input_k.setFont(QFont('Arial', 12))
        self.input_k = QLineEdit()
        self.set_font(self.input_k)

        layout_input_k = QHBoxLayout()
        layout_input_k.addWidget(label_input_k)
        layout_input_k.addWidget(self.input_k)

        # Создание кнопки
        input_button = QPushButton("Результат")
        input_button.clicked.connect(self.output_result)

        # Создание главного Widget и устанавливаем вертикальный layout
        general_widget = QWidget()
        layout = QVBoxLayout(general_widget)

        # Добавление в layout полей ввода и кнопки
        layout.addLayout(layout_input_array)
        layout.addLayout(layout_input_k)
        layout.addWidget(input_button)

        # Создание QTabWidget
        tab_widget = QTabWidget(self)

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
        self.stat_tab1 = QLabel()
        self.stat_tab1.setStyleSheet("font-size: 16px")
        self.crit_tab1 = QLabel()
        self.crit_tab1.setStyleSheet("font-size: 16px")
        self.result_tab1 = QLabel()
        self.result_tab1.setStyleSheet("font-size: 16px")

        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(title_tab1)
        tab1_layout.addWidget(self.stat_tab1)
        tab1_layout.addWidget(self.crit_tab1)
        tab1_layout.addWidget(self.result_tab1)

        # Наполнение 2 Tab
        title_tab2 = QLabel("Показательное распределение")
        title_tab2.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px")
        self.stat_tab2 = QLabel()
        self.stat_tab2.setStyleSheet("font-size: 16px")
        self.crit_tab2 = QLabel()
        self.crit_tab2.setStyleSheet("font-size: 16px")
        self.result_tab2 = QLabel()
        self.result_tab2.setStyleSheet("font-size: 16px")

        tab2_layout = QVBoxLayout(tab2)
        tab2_layout.addWidget(title_tab2)
        tab2_layout.addWidget(self.stat_tab2)
        tab2_layout.addWidget(self.crit_tab2)
        tab2_layout.addWidget(self.result_tab2)

        # Наполнение 3 Tab
        title_tab3 = QLabel("Нормальное распределение")
        title_tab3.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 15px")
        self.stat_tab3 = QLabel()
        self.stat_tab3.setStyleSheet("font-size: 16px")
        self.crit_tab3 = QLabel()
        self.crit_tab3.setStyleSheet("font-size: 16px")
        self.result_tab3 = QLabel()
        self.result_tab3.setStyleSheet("font-size: 16px")

        tab3_layout = QVBoxLayout(tab3)
        tab3_layout.addWidget(title_tab3)
        tab3_layout.addWidget(self.stat_tab3)
        tab3_layout.addWidget(self.crit_tab3)
        tab3_layout.addWidget(self.result_tab3)

        # Добавление QTabWidget в главный QWidget
        layout.addWidget(tab_widget)

        self.setCentralWidget(general_widget)

    def set_font(self, widget, size=12):
        font = widget.font()
        font.setPointSize(size)
        widget.setFont(font)

    def result_uniform(self, k, array_list, alpha):

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

        self.stat_tab1.setText(f'Статистика критерия Пирсона: {str(np.around(stat, 8))}')
        self.crit_tab1.setText(f'Критическое значение Хи-квадрат: {str(np.around(crit, 8))}')

        # Сравнение Статистики Хи-квадрат с Критическим значением
        if stat < crit:
            self.result_tab1.setText("Нулевая гипотеза принимается\n(данные соответствуют равномерному распределению)")
        else:
            self.result_tab1.setText("Нулевая гипотеза отвергается\n(данные не соответствуют нормальному распределению)")

    def result_exponential(self, k, array_list, alpha):

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
        df = k - 1 - 1
        crit = stats.chi2.ppf(1 - alpha, df)

        self.stat_tab2.setText(f'Статистика критерия Пирсона: {str(np.around(stat, 8))}')
        self.crit_tab2.setText(f'Критическое значение Хи-квадрат: {str(np.around(crit, 8))}')

        # Сравнение Статистики Хи-квадрат с Критическим значением
        if stat < crit:
            self.result_tab2.setText("Нулевая гипотеза принимается\n(данные соответствуют показательному распределению)")
        else:
            self.result_tab2.setText("Нулевая гипотеза отвергается\n(данные не соответствуют показательному распределению)")

    def result_normal(self, k, array_list, alpha):
        pass

    def output_result(self):
        array_list = np.array([float(num) for num in self.input_array.text().split()])
        k = int(self.input_k.text())

        alpha = 0.05

        self.result_uniform(k, array_list, alpha)
        self.result_exponential(k, array_list, alpha)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()