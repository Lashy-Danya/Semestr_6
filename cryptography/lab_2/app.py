import sys
import matplotlib.pyplot as plt
from math import gcd
from collections import Counter
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit,
                            QLabel, QPushButton, QTabWidget, QHBoxLayout)

class BBS:
    def __init__(self, seed, p=499, q=547):

        if p % 4 != 3 or q % 4 != 3:
            raise ValueError('p и q должны быть сравнимыми с 3 по модулю 4')

        self.p = p
        self.q = q
        self.m = p * q
        self.x = seed

        if gcd(seed, self.m) != 1:
            raise ValueError('seed и m должны быть взаимно простыми')
    
    def rand(self):
        self.x = (self.x ** 2) % self.m
        return self.x
        # return self.x & 0xFFFF  # выбираем 16 младших битов
    
    def generate_sequence(self, size):
        return [self.rand() for _ in range(size)]
    
    def generate_random_array(self, size, minimum, maximum):
        return [minimum + (self.rand() % (maximum - minimum + 1)) for _ in range(size)]

class LCG:
    def __init__(self, seed, a=1103515245, c=12345, m=2**31 - 1):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def rand(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def generate_sequence(self, size):
        return [self.rand() for _ in range(size)]
    
    def generate_random_array(self, size, minimum, maximum):
        return [minimum + (self.rand() / self.m) * (maximum - minimum) for _ in range(size)]

class LFSR:
    def __init__(self, seed, poly = 0b10100):
        self.state = seed
        self.poly = poly # порождающий полином: x^5 + x^3 + 1

    def rand(self):
        output = self.state & 1
        self.state >>= 1
        if output:
            self.state ^= self.poly
        return output

class InputHLayout(QHBoxLayout):
    def __init__(self, label, input):
        super().__init__()

        self.addWidget(label)
        self.addWidget(input)

class MyWindow(QWidget):
    def __init__(self, title, width, height):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedWidth(width)
        self.setMinimumHeight(height)

        layout = QVBoxLayout()

        # Создание QTabWidget
        tab_widget = QTabWidget()

        # Создание Widgets для вкладок
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()

        # Добавление вкладок в QTabWidget
        tab_widget.addTab(tab1, "BBS")
        tab_widget.addTab(tab2, "LCG")
        tab_widget.addTab(tab3, "LFSR")

        # Наполнение 1 Tab
        title_tab1 = QLabel("BBS")

        # Создание поля ввода seed
        seed_label_tab1, self.seed_input_tab1 = self.create_input('Ввод seed:')
        layout_tab1_seed_input = InputHLayout(seed_label_tab1, self.seed_input_tab1)

        # Создание поля ввода переменной P
        p_label_tab1, self.p_input_tab1 = self.create_input('Ввод переменной P:')
        layout_tab1_p_input = InputHLayout(p_label_tab1, self.p_input_tab1)

        # Создание поля ввода переменной Q
        q_label_tab1, self.q_input_tab1 = self.create_input('Ввод переменной Q:')
        layout_tab1_q_input = InputHLayout(q_label_tab1, self.q_input_tab1)

        # Создание кнопки
        input_button_tab1 = QPushButton("Получить график")
        input_button_tab1.clicked.connect(self.result_bbs)

        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(title_tab1)
        tab1_layout.addLayout(layout_tab1_seed_input)
        tab1_layout.addLayout(layout_tab1_p_input)
        tab1_layout.addLayout(layout_tab1_q_input)
        tab1_layout.addWidget(input_button_tab1)

        # Наполнение 2 Tab
        title_tab2 = QLabel("LCG")

        # Создание поля ввода seed
        seed_label_tab2, self.seed_input_tab2 = self.create_input('Ввод seed:')
        layout_tab2_seed_input = InputHLayout(seed_label_tab2, self.seed_input_tab2)

        # Создание поля ввода переменной A
        a_label_tab2, self.a_input_tab2 = self.create_input('Ввод переменной A:')
        layout_tab2_a_input = InputHLayout(a_label_tab2, self.a_input_tab2)

        # Создание поля ввода переменной C
        c_label_tab2, self.c_input_tab2 = self.create_input('Ввод переменной C:')
        layout_tab2_c_input = InputHLayout(c_label_tab2, self.c_input_tab2)

        # Создание кнопки
        input_button_tab2 = QPushButton("Получить график")
        input_button_tab2.clicked.connect(self.result_lcg)

        tab2_layout = QVBoxLayout(tab2)
        tab2_layout.addWidget(title_tab2)
        tab2_layout.addLayout(layout_tab2_seed_input)
        tab2_layout.addLayout(layout_tab2_a_input)
        tab2_layout.addLayout(layout_tab2_c_input)
        tab2_layout.addWidget(input_button_tab2)

        # Наполнение 3 Tab
        title_tab3 = QLabel("LFSR")

        # Создание поля ввода seed
        seed_label_tab3, self.seed_input_tab3 = self.create_input('Ввод seed:')
        layout_tab3_seed_input = InputHLayout(seed_label_tab3, self.seed_input_tab3)

        # Создание поля ввода переменной Poly
        poly_label_tab3, self.poly_input_tab3 = self.create_input('Ввод переменной Poly:')
        layout_tab3_poly_input = InputHLayout(poly_label_tab3, self.poly_input_tab3)

        # Создание кнопки
        input_button_tab3 = QPushButton("Получить график")
        input_button_tab3.clicked.connect(self.result_lfsr)

        tab3_layout = QVBoxLayout(tab3)
        tab3_layout.addWidget(title_tab3)
        tab3_layout.addLayout(layout_tab3_seed_input)
        tab3_layout.addLayout(layout_tab3_poly_input)
        tab3_layout.addWidget(input_button_tab3)

        # Добавление QTabWidget в главный QWidget
        layout.addWidget(tab_widget)

        self.setLayout(layout)

    def create_input(self, label_text):
        label = QLabel(label_text)
        input_field = QLineEdit()
        input_field.setStyleSheet("font-size: 18px")
        label.setStyleSheet("font-size: 18px; font-weight: bold")
        return label, input_field
    
    def result_bbs(self):
        seed = self.seed_input_tab1.text()
        p = self.p_input_tab1.text()
        q = self.q_input_tab1.text()

        alphabet = [chr(letter) for letter in range(ord('а'), ord('я')+1)]

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

        if not seed and not p and not q:
            bbs = BBS(12345)
        elif not p and not q:
            bbs = BBS(int(seed))
        elif not q:
            bbs = BBS(int(seed), int(p))
        else:
            bbs = BBS(int(seed), int(p), int(q))
        # Генерация текстовой последовательности длины 50 символов
        text_50 = ''.join([alphabet[bbs.rand() % 32] for _ in range(50)])
        # Получаем частотный словарь символов
        freq_dict_50 = Counter(text_50)
        
        ax1.bar([i for i in alphabet], [freq_dict_50.get(i, 0) for i in alphabet])
        ax1.set_title('Текст длиной 50 символов')

        if not seed and not p and not q:
            bbs = BBS(12345)
        elif not p and not q:
            bbs = BBS(int(seed))
        elif not q:
            bbs = BBS(int(seed), int(p))
        else:
            bbs = BBS(int(seed), int(p), int(q))
        # Генерация текстовой последовательности длины 100 символов
        text_100 = ''.join([alphabet[bbs.rand() % 32] for _ in range(100)])
        # Получаем частотный словарь символов
        freq_dict_100 = Counter(text_100)

        ax2.bar([i for i in alphabet], [freq_dict_100.get(i, 0) for i in alphabet])
        ax2.set_title('Текст длиной 100 символов')

        if not seed and not p and not q:
            bbs = BBS(12345)
        elif not p and not q:
            bbs = BBS(int(seed))
        elif not q:
            bbs = BBS(int(seed), int(p))
        else:
            bbs = BBS(int(seed), int(p), int(q))
        # Генерация текстовой последовательности длины 1000 символов
        text_1000 = ''.join([alphabet[bbs.rand() % 32] for _ in range(1000)])
        # Получаем частотный словарь символов
        freq_dict_1000 = Counter(text_1000)

        ax3.bar([i for i in alphabet], [freq_dict_1000.get(i, 0) for i in alphabet])
        ax3.set_title('Текст длиной 1000 символов')

        plt.show()

    def result_lcg(self):
        seed = self.seed_input_tab2.text()
        a = self.a_input_tab2.text()
        c = self.c_input_tab2.text()

        alphabet = [chr(letter) for letter in range(ord('а'), ord('я')+1)]

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

        if not seed and not a and not c:
            lcg = LCG(seed=123)
        elif not a and not c:
            lcg = LCG(int(seed))
        elif not c:
            lcg = LCG(int(seed), int(a))
        else:
            lcg = LCG(int(seed), int(a), int(c))
        # Генерация текстовой последовательности длины 50 символов
        text_50 = ''.join([alphabet[lcg.rand() % 32] for _ in range(50)])
        # Получаем частотный словарь символов
        freq_dict_50 = Counter(text_50)

        ax1.bar([i for i in alphabet], [freq_dict_50.get(i, 0) for i in alphabet])
        ax1.set_title('Текст длиной 50 символов')

        if not seed and not a and not c:
            lcg = LCG(seed=123)
        elif not a and not c:
            lcg = LCG(int(seed))
        elif not c:
            lcg = LCG(int(seed), int(a))
        else:
            lcg = LCG(int(seed), int(a), int(c))
        # Генерация текстовой последовательности длины 100 символов
        text_100 = ''.join([alphabet[lcg.rand() % 32] for _ in range(100)])
        # Получаем частотный словарь символов
        freq_dict_100 = Counter(text_100)

        ax2.bar([i for i in alphabet], [freq_dict_100.get(i, 0) for i in alphabet])
        ax2.set_title('Текст длиной 100 символов')

        if not seed and not a and not c:
            lcg = LCG(seed=123)
        elif not a and not c:
            lcg = LCG(int(seed))
        elif not c:
            lcg = LCG(int(seed), int(a))
        else:
            lcg = LCG(int(seed), int(a), int(c))
        # Генерация текстовой последовательности длины 1000 символов
        text_1000 = ''.join([alphabet[lcg.rand() % 32] for _ in range(1000)])
        # Получаем частотный словарь символов
        freq_dict_1000 = Counter(text_1000)

        ax3.bar([i for i in alphabet], [freq_dict_1000.get(i, 0) for i in alphabet])
        ax3.set_title('Текст длиной 1000 символов')

        plt.show()

    def result_lfsr(self):
        seed = self.seed_input_tab3.text()
        poly = self.poly_input_tab3.text()

        alphabet = [chr(letter) for letter in range(ord('а'), ord('я')+1)]

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

        if not seed and not poly:
            lfsr = LFSR(0b11011)
        elif not poly:
            lfsr = LFSR(int(seed))
        else:
            lfsr = LFSR(int(seed), int(poly))
        arr = []

        for i in range(50):
            rand_int = 0
            for j in range(5):
                rand_int |= lfsr.rand() << j
            arr.append(rand_int)
        # Генерация текстовой последовательности длины 50 символов
        text_50 = ''.join([alphabet[i] for i in arr])
        # Получаем частотный словарь символов
        freq_dict_50 = Counter(text_50)
        
        ax1.bar([i for i in alphabet], [freq_dict_50.get(i, 0) for i in alphabet])
        ax1.set_title('Текст длиной 50 символов')

        if not seed and not poly:
            lfsr = LFSR(0b11011)
        elif not poly:
            lfsr = LFSR(int(seed))
        else:
            lfsr = LFSR(int(seed), int(poly))
        arr = []

        for i in range(100):
            rand_int = 0
            for j in range(5):
                rand_int |= lfsr.rand() << j
            arr.append(rand_int)
        # Генерация текстовой последовательности длины 100 символов
        text_100 = ''.join([alphabet[i] for i in arr])
        # Получаем частотный словарь символов
        freq_dict_100 = Counter(text_100)

        ax2.bar([i for i in alphabet], [freq_dict_100.get(i, 0) for i in alphabet])
        ax2.set_title('Текст длиной 100 символов')

        if not seed and not poly:
            lfsr = LFSR(0b11011)
        elif not poly:
            lfsr = LFSR(int(seed))
        else:
            lfsr = LFSR(int(seed), int(poly))
        arr = []

        for i in range(1000):
            rand_int = 0
            for j in range(5):
                rand_int |= lfsr.rand() << j
            arr.append(rand_int)
        # Генерация текстовой последовательности длины 1000 символов
        text_1000 = ''.join([alphabet[i] for i in arr])
        # Получаем частотный словарь символов
        freq_dict_1000 = Counter(text_1000)

        ax3.bar([i for i in alphabet], [freq_dict_1000.get(i, 0) for i in alphabet])
        ax3.set_title('Текст длиной 1000 символов')

        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow("Лаба №1", 400, 200)
    window.show()
    sys.exit(app.exec())