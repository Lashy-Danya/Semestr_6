import os
import string
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from collections import Counter

matplotlib.use('TkAgg')

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

    symbols_ascii = string.printable + \
        ''.join([chr(letter) for letter in range(ord('а'), ord('я')+1)]) + \
        ''.join([chr(letter) for letter in range(ord('А'), ord('Я')+1)])

    # Удаляем пробелы и переходы на новую строку
    # text = text.replace('\n', '').replace(' ', '')

    # Получаем частотный словарь символов
    freq_dict = Counter(text)

    plt.bar([i for i in symbols_ascii], [freq_dict.get(i, 0) for i in symbols_ascii])
    plt.title('Гистограмма частоты символов ASCII')
    plt.xlabel('ASCII символ')
    plt.ylabel('Частота')

    plt.show()

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

    # red_entropy = -np.sum(red_freq * np.log2(red_freq))
    # print(f'Информационная мера красного цвета: {red_entropy:.2f} бит')

    # green_entropy = -np.sum(green_freq * np.log2(green_freq))
    # print(f'Информационная мера зеленого цвета: {green_entropy:.2f} бит')

    # blue_entropy = -np.sum(blue_freq * np.log2(blue_freq))
    # print(f'Информационная мера синего цвета: {blue_entropy:.2f} бит')

    # plt.bar(range(256), freq)
    # plt.title('Гистограмма частоты символов ASCII')
    # plt.xlabel('ASCII символ')
    # plt.ylabel('Частота')

    # fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

    # ax1.bar(range(256), red_freq, color='r')
    # ax1.set_title('Красный цвет')

    # ax2.bar(range(256), green_freq, color='g')
    # ax2.set_title('Зеленный цвет')

    # ax3.bar(range(256), blue_freq)
    # ax3.set_title('Синий цвет')

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

    plt.show()

if __name__ == '__main__':

    # Получение пути к запускаемому файлу
    current_file_path = os.path.abspath(__file__)
    current_path = os.path.dirname(current_file_path)

    # Получение названия файла и путь к нему в папке с запускаемым скриптом
    file_name = input('Введите название файла формата txt/bmp: ')
    file_path = os.path.join(current_path, 'file', file_name)

    # Проверка на существование данного файла
    if os.path.exists(file_path):
        file_name, file_extension = os.path.splitext(file_name)
        if file_extension == '.txt':
            frequency_analys_text(file_path)
        elif file_extension == '.bmp':
            frecuency_analys_bmp(file_path)
        else:
            print('Файл должен быть формата .txt или .bmp')

    else:
        print('Такого файла нет')