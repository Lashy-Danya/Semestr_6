import codecs
import string
import math
import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
from itertools import cycle, islice
from collections import Counter
from tkinter import filedialog

matplotlib.use('TkAgg')

def entropy_txt(data):
    data = data.replace(" ", "").replace("\n", "")
    counter = Counter(data)
    probabilities = [count / len(data) for count in counter.values()]

    return -sum(prob * math.log2(prob) for prob in probabilities)

def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars and not ch.isdigit()])

def get_file_path():
    file_path = filedialog.askopenfilename(
        filetypes=(("Text files", "*.txt"),)
    )
    if file_path:
        return file_path
    return ""

def write_to_file(filename, data):
    try:
        with open(filename, "w", encoding='utf-8') as file:
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

        # plt.show()

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

def encode_feistel():
        key = input_key.get()

        file_path = get_file_path()

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
        
        plt.show()

        write_to_file("encrypt_text.txt", result)
        
def decode_feistel():
        key = input_key.get()

        file_path = get_file_path()

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        result = decode(text, key)

        write_to_file("decode_text.txt", result)
        
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Лабораторная работа 3")
    # root.minsize(400, 200)
    root.geometry("400x200")
    root.resizable(False, False)
    
   # Создание пустых рамок для отступов
    top_frame = tk.Frame(root, height=20)
    top_frame.pack()

    bottom_frame = tk.Frame(root, height=20)
    bottom_frame.pack()
    
    key_frame = tk.Frame()
    key_frame.pack(pady=5)
    
    # Создание метки seed
    label_key = tk.Label(key_frame, text="Введите key:")
    label_key.pack(side="left", padx=5)
    label_key.config(font=("Arial", 11))

    # Создание поля ввода sedd
    input_key = tk.StringVar()
    entry_key = tk.Entry(key_frame, bd=3, textvariable=input_key)
    entry_key.pack(side="right")
    entry_key.config(font=("Arial", 11))
    
    input_button = tk.Button(root, text="Зашифровать текст", command=encode_feistel, width=16, height=2)
    input_button.pack(pady=5)
    input_button.config(font=("Arial", 10))
    
    output_button = tk.Button(root, text="Расшифровать текст", command=decode_feistel, width=16, height=2)
    output_button.pack(pady=5)
    output_button.config(font=("Arial", 10))
    
    root.mainloop()