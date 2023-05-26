import sys
import codecs
import string
import matplotlib.pyplot as plt
from collections import Counter
from itertools import cycle
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit,
                            QLabel, QPushButton, QTabWidget, QHBoxLayout,
                            QFileDialog)

cp866_chars = []
for i in range(256):
    try:
        char = codecs.decode(bytes([i]), 'cp866')
        cp866_chars.append(char)
    except UnicodeDecodeError:
        pass

def write_to_file(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)
        print("Данные успешно записаны в файл:", filename)
    except IOError:
        print("Ошибка при записи данных в файл:", filename)

class LFSR:
    def __init__(self, seed, poly):
        self.state = seed
        self.poly = poly # порождающий полином: x^5 + x^3 + 1

    def shift(self):
        output = self.state & 1
        self.state >>= 1
        if output:
            self.state ^= self.poly
        return output
    
    def rand(self):
        return sum(self.shift() << i for i in range(self.poly.bit_length()))
    
def encrypt_text_lfsr(text, seed, poly):
    lfsr = LFSR(seed, poly)
    f = lambda arg: cp866_chars[(cp866_chars.index(arg)+lfsr.rand())%len(cp866_chars)]
    return ''.join(map(f, text))

def decrypt_text_lfsr(text, seed, poly):
    lfsr = LFSR(seed, poly)
    f = lambda arg: cp866_chars[(cp866_chars.index(arg)-lfsr.rand())%len(cp866_chars)]
    return ''.join(map(f, text))

alphabet = [chr(letter) for letter in range(ord('а'), ord('я')+1)]

def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])

def vijn_encode(text, key):
    f = lambda arg: alphabet[(alphabet.index(arg[0])+alphabet.index(arg[1]))%len(alphabet)]
    return ''.join(map(f, zip(text, cycle(key))))

def vijn_decode(cipher_text, key):
    f = lambda arg: alphabet[(alphabet.index(arg[0])-alphabet.index(arg[1]))%len(alphabet)]
    return ''.join(map(f, zip(cipher_text, cycle(key))))

def caesae_encode(text, key):
    f = lambda arg: cp866_chars[(cp866_chars.index(arg)+key)%len(cp866_chars)]
    return ''.join(map(f, text))

def caesae_decode(text, key):
    f = lambda arg: cp866_chars[(cp866_chars.index(arg)-key)%len(cp866_chars)]
    return ''.join(map(f, text))

def encode_text(text, key):
    f = lambda arg: alphabet[(alphabet.index(arg[0])+alphabet.index(arg[1]))%len(alphabet)]
    return ''.join(map(f, zip(text, cycle(key))))

def decode_text(cipher_text, key):
    f = lambda arg: alphabet[(alphabet.index(arg[0])+len(alphabet)-alphabet.index(arg[1]))%len(alphabet)]
    return ''.join(map(f, zip(cipher_text, cycle(key))))

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
        tab4 = QWidget()

        # Добавление вкладок в QTabWidget
        tab_widget.addTab(tab1, "Vijener")
        tab_widget.addTab(tab2, "Цезарь")
        tab_widget.addTab(tab3, "Gamming")
        tab_widget.addTab(tab4, "ПСП")

        # Наполнение 1 Tab
        title_tab1 = QLabel("Vijener")

        # Создание поля ввода seed
        key_label_tab1, self.key_input_tab1 = self.create_input('Ввод Key:')
        layout_tab1_key_input = InputHLayout(key_label_tab1, self.key_input_tab1)

        # Создание кнопки
        input_button_tab1 = QPushButton("Зашифровать текст")
        input_button_tab1.clicked.connect(self.encode_vijn)

        output_button_tab1 = QPushButton("Расшифровать текст")
        output_button_tab1.clicked.connect(self.decode_vijn)

        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(title_tab1)
        tab1_layout.addLayout(layout_tab1_key_input)
        tab1_layout.addWidget(input_button_tab1)
        tab1_layout.addWidget(output_button_tab1)

        # Наполнение 2 Tab
        title_tab2 = QLabel("Цезарь")

        # Создание поля ввода seed
        key_label_tab2, self.key_input_tab2 = self.create_input('Ввод Key:')
        layout_tab2_key_input = InputHLayout(key_label_tab2, self.key_input_tab2)

        # Создание кнопки
        input_button_tab2 = QPushButton("Зашифровать текст")
        input_button_tab2.clicked.connect(self.encode_caesar)

        output_button_tab2 = QPushButton("Расшифровать текст")
        output_button_tab2.clicked.connect(self.decode_caesar)

        tab2_layout = QVBoxLayout(tab2)
        tab2_layout.addWidget(title_tab2)
        tab2_layout.addLayout(layout_tab2_key_input)
        tab2_layout.addWidget(input_button_tab2)
        tab2_layout.addWidget(output_button_tab2)

        # Наполнение 3 Tab
        title_tab3 = QLabel("Gamming")

        # Создание поля ввода seed
        key_label_tab3, self.key_input_tab3 = self.create_input('Ввод Key:')
        layout_tab3_key_input = InputHLayout(key_label_tab3, self.key_input_tab3)

        # Создание кнопки
        input_button_tab3 = QPushButton("Зашифровать текст")
        input_button_tab3.clicked.connect(self.encode_gamming)

        output_button_tab3 = QPushButton("Расшифровать текст")
        output_button_tab3.clicked.connect(self.decode_gamming)

        tab3_layout = QVBoxLayout(tab3)
        tab3_layout.addWidget(title_tab3)
        tab3_layout.addLayout(layout_tab3_key_input)
        tab3_layout.addWidget(input_button_tab3)
        tab3_layout.addWidget(output_button_tab3)

        # Наполнение 4 Tab
        title_tab4 = QLabel("ПСП")

        # Создание поля ввода seed
        seed_label_tab4, self.seed_input_tab4 = self.create_input('Ввод seed:')
        layout_tab4_seed_input = InputHLayout(seed_label_tab4, self.seed_input_tab4)

        # Создание поля ввода переменной Poly
        poly_label_tab4, self.poly_input_tab4 = self.create_input('Ввод переменной Poly:')
        layout_tab4_poly_input = InputHLayout(poly_label_tab4, self.poly_input_tab4)

        # Создание кнопки
        input_button_tab4 = QPushButton("Зашифровать текст")
        input_button_tab4.clicked.connect(self.encode_lfsr)

        output_button_tab4 = QPushButton("Расшифровать текст")
        output_button_tab4.clicked.connect(self.decode_lfsr)

        tab4_layout = QVBoxLayout(tab4)
        tab4_layout.addWidget(title_tab4)
        tab4_layout.addLayout(layout_tab4_seed_input)
        tab4_layout.addLayout(layout_tab4_poly_input)
        tab4_layout.addWidget(input_button_tab4)
        tab4_layout.addWidget(output_button_tab4)

        # Добавление QTabWidget в главный QWidget
        layout.addWidget(tab_widget)

        self.setLayout(layout)

    def create_input(self, label_text):
        label = QLabel(label_text)
        input_field = QLineEdit()
        input_field.setStyleSheet("font-size: 18px")
        label.setStyleSheet("font-size: 18px; font-weight: bold")
        return label, input_field
    
    def get_file_path(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Text Files (*.txt)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            return file_dialog.selectedFiles()[0]
        return ""
    
    # Задание 1
    def decode_vijn(self):
        key = self.key_input_tab1.text()

        file_path = self.get_file_path()

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        spec_chars = string.punctuation

        key = remove_chars_from_text(key.lower().replace(" ", ""), spec_chars)

        text = remove_chars_from_text(text.lower().replace(" ", "").replace('\n', ''), spec_chars)

        result = vijn_encode(text, key)

        write_to_file("decode_text.txt", result)

    def encode_vijn(self):
        key = self.key_input_tab1.text()

        file_path = self.get_file_path()

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        spec_chars = string.punctuation

        key = remove_chars_from_text(key.lower().replace(" ", ""), spec_chars)

        text = remove_chars_from_text(text.lower().replace(" ", "").replace('\n', ''), spec_chars)

        result = vijn_decode(text, key)

        write_to_file("encrypt_text.txt", result)

        freq_dict = Counter(result)
        freq_dict_text = Counter(text)

        fig1, ax = plt.subplots(1, 1, figsize=(16, 6))

        ax.bar([i for i in alphabet], [freq_dict_text.get(i, 0) for i in alphabet])
        ax.set_title('Гистограмма начального текста')
        ax.set_xlabel('Символы')
        ax.set_ylabel('Частота')

        fig1, ax1 = plt.subplots(1, 1, figsize=(16, 6))

        ax1.bar([i for i in alphabet], [freq_dict.get(i, 0) for i in alphabet])
        ax1.set_title('Гистограмма зашифрованного текста')
        ax1.set_xlabel('Символы')
        ax1.set_ylabel('Частота')

        plt.show()

    # задание 2
    def decode_caesar(self):
        key = int(self.key_input_tab2.text())

        file_path = self.get_file_path()

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        spec_chars = string.punctuation

        # text = remove_chars_from_text(text.replace(" ", "").replace('\n', ''), spec_chars)

        result = caesae_decode(text, key)

        write_to_file("decode_text.txt", result)

    def encode_caesar(self):
        key = int(self.key_input_tab2.text())

        file_path = self.get_file_path()

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        spec_chars = string.punctuation

        # text = remove_chars_from_text(text.replace(" ", "").replace('\n', ''), spec_chars)

        result = caesae_encode(text, key)

        write_to_file("encrypt_text.txt", result)

        freq_dict = Counter(result)
        freq_dict_text = Counter(text)

        fig1, (ax, ax1) = plt.subplots(2, 1, figsize=(16, 6))

        ax.bar([i for i in cp866_chars[:128]], [freq_dict_text.get(i, 0) for i in cp866_chars[:128]])
        ax.set_title('Гистограмма начального текста')
        ax.set_xlabel('Символы')
        ax.set_ylabel('Частота')

        ax1.bar([i for i in cp866_chars[128:]], [freq_dict_text.get(i, 0) for i in cp866_chars[128:]])
        ax1.set_xlabel('Символы')
        ax1.set_ylabel('Частота')

        fig2, (ax2, ax3) = plt.subplots(2, 1, figsize=(16, 6))

        ax2.bar([i for i in cp866_chars[:128]], [freq_dict.get(i, 0) for i in cp866_chars[:128]])
        ax2.set_title('Гистограмма зашифрованного текста')
        ax2.set_xlabel('Символы')
        ax2.set_ylabel('Частота')

        ax3.bar([i for i in cp866_chars[128:]], [freq_dict.get(i, 0) for i in cp866_chars[128:]])
        ax3.set_xlabel('Символы')
        ax3.set_ylabel('Частота')

        plt.show()

    # Задание 3
    def decode_gamming(self):
        key = self.key_input_tab3.text()

        file_path = self.get_file_path()

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        spec_chars = string.punctuation

        key = remove_chars_from_text(key.lower().replace(" ", ""), spec_chars)

        text = remove_chars_from_text(text.lower().replace(" ", "").replace('\n', ''), spec_chars)

        result = decode_text(text, key)

        write_to_file("decode_text.txt", result)

    def encode_gamming(self):
        key = self.key_input_tab3.text()

        file_path = self.get_file_path()

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        spec_chars = string.punctuation

        key = remove_chars_from_text(key.lower().replace(" ", ""), spec_chars)

        text = remove_chars_from_text(text.lower().replace(" ", "").replace('\n', ''), spec_chars)

        result = encode_text(text, key)

        write_to_file("encrypt_text.txt", result)    

        freq_dict = Counter(result)
        freq_dict_text = Counter(text)

        fig1, (ax, ax1) = plt.subplots(2, 1, figsize=(16, 6))

        ax.bar([i for i in alphabet], [freq_dict_text.get(i, 0) for i in alphabet])
        ax.set_title('Гистограмма начального текста')
        ax.set_xlabel('Символы')
        ax.set_ylabel('Частота')

        ax1.bar([i for i in alphabet], [freq_dict.get(i, 0) for i in alphabet])
        ax1.set_title('Гистограмма зашифрованного текста')
        ax1.set_xlabel('Символы')
        ax1.set_ylabel('Частота')

        plt.show()    

    # Задание 4
    def decode_lfsr(self):
        seed = self.seed_input_tab4.text()
        poly = self.poly_input_tab4.text()

        file_path = self.get_file_path()

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        if not seed and not poly:
            result = decrypt_text_lfsr(text, 0b11011000, 0b10111000)
        else:
            result = decrypt_text_lfsr(text, int(seed), int(poly))

        write_to_file("decode_text.txt", result)

    def encode_lfsr(self):
        seed = self.seed_input_tab4.text()
        poly = self.poly_input_tab4.text()

        file_path = self.get_file_path()
          
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        spec_chars = string.punctuation

        if not seed and not poly:
            result = encrypt_text_lfsr(text, 0b11011000, 0b10111000)
        else:
            result = encrypt_text_lfsr(text, int(seed), int(poly))

        write_to_file("encrypt_text.txt", result)

        freq_dict = Counter(result)
        freq_dict_text = Counter(text)

        fig1, (ax, ax1) = plt.subplots(2, 1, figsize=(16, 6))

        ax.bar([i for i in cp866_chars[:128]], [freq_dict_text.get(i, 0) for i in cp866_chars[:128]])
        ax.set_title('Гистограмма начального текста')
        ax.set_xlabel('Символы')
        ax.set_ylabel('Частота')

        ax1.bar([i for i in cp866_chars[128:]], [freq_dict_text.get(i, 0) for i in cp866_chars[128:]])
        ax1.set_xlabel('Символы')
        ax1.set_ylabel('Частота')

        fig2, (ax2, ax3) = plt.subplots(2, 1, figsize=(16, 6))

        ax2.bar([i for i in cp866_chars[:128]], [freq_dict.get(i, 0) for i in cp866_chars[:128]])
        ax2.set_title('Гистограмма зашифрованного текста')
        ax2.set_xlabel('Символы')
        ax2.set_ylabel('Частота')

        ax3.bar([i for i in cp866_chars[128:]], [freq_dict.get(i, 0) for i in cp866_chars[128:]])
        ax3.set_xlabel('Символы')
        ax3.set_ylabel('Частота')

        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow("Лаба №2", 400, 200)
    window.show()
    sys.exit(app.exec())