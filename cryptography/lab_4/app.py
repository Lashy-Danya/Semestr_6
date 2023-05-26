import sys
import codecs
import string
import math
import matplotlib.pyplot as plt
from collections import Counter
from itertools import cycle, islice
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit,
                             QFileDialog, QLabel, QPushButton, QHBoxLayout)

# def entropy_txt(data):
#     data = data.replace(" ", "").replace("\n", "")
#     counter = Counter(data)
#     probabilities = [count / len(data) for count in counter.values()]

#     return -sum(prob * math.log2(prob) for prob in probabilities)

def entropy_txt(data):
    text = data
    text = text.translate(str.maketrans('', '', string.punctuation + string.digits))
    letter_counts = Counter(text)
    total_letters = sum(letter_counts.values())
    letter_frequencies = {}
    for letter, count in letter_counts.items():
        letter_frequencies[letter] = count / total_letters * 100
    symbols = list(letter_frequencies.keys())
    counts = list(letter_frequencies.values())
    entropy = 0
    for count in letter_counts.values():
        p = count / total_letters
        entropy -= p * math.log2(p)
    return entropy

def write_to_file(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)
        print("Данные успешно записаны в файл:", filename)
    except IOError:
        print("Ошибка при записи данных в файл:", filename)

ROUNDS = 8

cp866_chars = []
for i in range(256):
    try:
        char = codecs.decode(bytes([i]), 'cp866')
        cp866_chars.append(char)
    except UnicodeDecodeError:
        pass

def festel(L, R, key, iter):
    K = cp866_chars.index(key)
    temp = L ^ (((R + K) << 1) % len(cp866_chars))
    L = R
    R = temp
    if iter+1 != ROUNDS:
        return (cp866_chars[L] + cp866_chars[R])

    return (cp866_chars[R] + cp866_chars[L])

def encode(text, key):
    if len(text) % 2 != 0:
        text += '.'

    blocks = []

    for i in range(0, len(text), 2):
        blocks.append(text[i:i+2])

    keys = list(islice(cycle(key), ROUNDS))

    for i in range(ROUNDS):
        shifr = []
        for block in blocks:
            item = festel(cp866_chars.index(block[0]), \
                          cp866_chars.index(block[1]), keys[i], i)
            shifr.append(item)
        blocks = shifr

        # График раунда
        freq_dict = Counter(''.join(shifr))

        info_measure = entropy_txt(''.join(shifr))

        fig1, (ax, ax1) = plt.subplots(2, 1, figsize=(16, 6))

        ax.bar([i for i in cp866_chars[:128]], \
               [freq_dict.get(i, 0) for i in cp866_chars[:128]])
        ax.set_title(f'Гистограмма шифрования текста. Раунд {i+1}. Энтропия текста: {info_measure:.2f}')
        ax.set_xlabel('Символы')
        ax.set_ylabel('Частота')

        ax1.bar([i for i in cp866_chars[128:]], \
                [freq_dict.get(i, 0) for i in cp866_chars[128:]])
        ax1.set_xlabel('Символы')
        ax1.set_ylabel('Частота')

        plt.show()

    return ''.join(shifr)

def decode(text, key):
    blocks = []

    for i in range(0, len(text), 2):
        blocks.append(text[i:i+2])

    keys = list(islice(cycle(key), ROUNDS))[::-1]

    for i in range(ROUNDS):
        defshifr = []
        for block in blocks[::-1]:
            item = festel(cp866_chars.index(block[0]), \
                          cp866_chars.index(block[1]), keys[i], i)
            defshifr.append(item)
        blocks = defshifr

    return ''.join(defshifr)

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

        title = QLabel("Vijener")

        # Создание поля ввода seed
        key_label, self.key_input = self.create_input('Ввод Key:')
        layout_key_input = InputHLayout(key_label, self.key_input)

        # Создание кнопки
        input_button = QPushButton("Зашифровать текст")
        input_button.clicked.connect(self.encode_feistel)

        output_button = QPushButton("Расшифровать текст")
        output_button.clicked.connect(self.decode_feistel)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addLayout(layout_key_input)
        layout.addWidget(input_button)
        layout.addWidget(output_button)

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
    
    def decode_feistel(self):
        key = self.key_input.text()

        file_path = self.get_file_path()

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        result = decode(text, key)

        write_to_file("decode_text.txt", result)

    def encode_feistel(self):
        key = self.key_input.text()

        file_path = self.get_file_path()

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        freq_dict_text = Counter(text)

        info_measure = entropy_txt(text)

        fig1, (ax, ax1) = plt.subplots(2, 1, figsize=(16, 6))

        ax.bar([i for i in cp866_chars[:128]], [freq_dict_text.get(i, 0) for i in cp866_chars[:128]])
        ax.set_title(f'Гистограмма начального текста. Энтропия текста: {info_measure:.2f}')
        ax.set_xlabel('Символы')
        ax.set_ylabel('Частота')

        ax1.bar([i for i in cp866_chars[128:]], [freq_dict_text.get(i, 0) for i in cp866_chars[128:]])
        ax1.set_xlabel('Символы')
        ax1.set_ylabel('Частота')

        result = encode(text, key)

        write_to_file("encrypt_text.txt", result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow("Лаба №3", 400, 200)
    window.show()
    sys.exit(app.exec())
