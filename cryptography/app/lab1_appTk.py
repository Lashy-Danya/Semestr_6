import tkinter as tk
import os
import string
import math
import codecs
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from PIL import Image
from collections import Counter
from tkinter import filedialog

matplotlib.use('TkAgg')

cp866_chars = []
for i in range(256):
    try:
        char = codecs.decode(bytes([i]), 'cp866')
        cp866_chars.append(char)
    except UnicodeDecodeError:
        pass
    
def choose_file():
    file_path = filedialog.askopenfilename(
        filetypes=(("Text files", "*.txt"), ("Bitmap files", "*.bmp"))
    )
    if file_path:
        return file_path
    return ""

def select_file():
        file_path = choose_file()
        if file_path:
            process_file(file_path)
            
def process_file(file_path):
        file_name = os.path.basename(file_path)
        file_name, file_extension = os.path.splitext(file_name)

        if file_extension == ".bmp":
            result, plt = frecuency_analys_bmp(file_path)
            message1 = f"Выбран файл BMP: {file_name}"
            message2 = f"Информационная мера файла: {result:.2f} бит"
            output_label.config(text=f"{message1}\n{message2}")
            plt.show()
        elif file_extension == ".txt":
            result, plt = frequency_analys_text(file_path)
            message1 = f"Выбран файл TXT: {file_name}"
            message2 = f"Информационная мера файла: {result:.2f} бит"
            output_label.config(text=f"{message1}\n{message2}")
            plt.show()
        else:
            output_label.config(text="Файл не выбран")
    
def entropy_txt(data):
    data = data.lower()
    data = data.translate(str.maketrans('', '', string.punctuation + string.digits))
    counter = Counter(data)
    probabilities = [float(count) / len(data) for count in counter.values()]

    return -sum(prob * math.log(prob, 2) for prob in probabilities)

def frequency_analys_text(file_name):
    """Частотный анализ текстового файла"""

    # Открывем файл на чтение
    with open(file_name, 'r') as f:
        # Считываем содержимое файла
        text = f.read()

    info_measure = entropy_txt(text)
    print(f'Информационная мера файла: {info_measure:.2f} бит')

    # Удаляем пробелы и переходы на новую строку
    # text = text.replace('\n', '').replace(' ', '')

    # Получаем частотный словарь символов
    freq_dict_text = Counter(text)

    fig1, (ax, ax1) = plt.subplots(2, 1, figsize=(16, 6))

    ax.bar([i for i in cp866_chars[:128]], [freq_dict_text.get(i, 0) for i in cp866_chars[:128]])
    ax.set_title('Гистограмма начального текста')
    ax.set_xlabel('Символы')
    ax.set_ylabel('Частота')

    ax1.bar([i for i in cp866_chars[128:]], [freq_dict_text.get(i, 0) for i in cp866_chars[128:]])
    ax1.set_xlabel('Символы')
    ax1.set_ylabel('Частота')

    return info_measure, plt

def frecuency_analys_bmp(file_name):
    """Частотный анализ изображения типа .bmp"""

    with open(file_name, 'rb') as f:
        data = f.read()

    freq = [0] * 256

    for i in range(54, len(data)):
        freq[data[i]] += 1

    total_pixels = sum(freq)

    # entropy = -sum(p * math.log2(p) for count in freq if (p := count / total_pixels) != 0)

    entropy = 0
    for count in freq:
        p = count / total_pixels
        if p != 0:
            entropy -= p * math.log2(p)

    print(f'Информационная мера файла: {entropy:.2f} бит')

    img = Image.open(file_name)
    data = np.array(img)

    red_channel = data[:, :, 0]
    green_channel = data[:, :, 1]
    blue_channel = data[:, :, 2]

    freq = np.zeros(256)
    red_freq = np.zeros(256)
    green_freq = np.zeros(256)
    blue_freq = np.zeros(256)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            freq[data[i, j]] += 1
            red_freq[red_channel[i, j]] += 1
            green_freq[green_channel[i, j]] += 1
            blue_freq[blue_channel[i, j]] += 1

    # с наложением на одном графике
    fig, ax = plt.subplots()

    ax.bar(range(256), red_freq, color='r', align='center', label='Красный')
    ax.bar(range(256), green_freq, bottom=red_freq, color='g', align='center', label='Зеленый')
    ax.bar(range(256), blue_freq, bottom=red_freq+green_freq, align='center', label='Синий')

    ax.set_xlabel('Цвет')
    ax.set_ylabel('Частота')
    ax.set_title('Гистограмма частоты цвета')
    ax.legend()

    fig2, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

    ax1.bar(range(256), red_freq, color='r')
    ax1.set_title('Гистограмма красного цвета')
    ax1.set_xlabel('Цвет')
    ax1.set_ylabel('Частота')

    ax2.bar(range(256), green_freq, color='g')
    ax2.set_title('Гистограмма зеленного цвета')
    ax2.set_xlabel('Цвет')
    ax2.set_ylabel('Частота')

    ax3.bar(range(256), blue_freq)
    ax3.set_title('Гистограмма синего цвета')
    ax3.set_xlabel('Цвет')
    ax3.set_ylabel('Частота')

    return entropy, plt

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Лабораторная работа 0")
    # root.minsize(300, 140)
    root.geometry("300x180")
    root.resizable(True, False)
    
    # Создание пустых рамок для отступов
    top_frame = tk.Frame(root, height=20)
    top_frame.pack()

    bottom_frame = tk.Frame(root, height=20)
    bottom_frame.pack()
    
    # Создание метки для вывода данных
    output_label = tk.Label(root, text="Файл не выбран")
    output_label.pack()
    output_label.config(font=("Arial", 10))
    
    button = tk.Button(root, text="Выбрать файл", command=select_file, width=12, height=2)
    button.pack()
    button.config(font=("Arial", 10))
    
    root.mainloop()