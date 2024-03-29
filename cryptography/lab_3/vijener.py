import string
import os
import matplotlib.pyplot as plt
from collections import Counter
from itertools import cycle

"""
Пунт 1.1
с помощью способов традиционного шифрования, указанных  в таблице 2
"""

alphabet = [chr(letter) for letter in range(ord('а'), ord('я')+1)]

def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])

def vijn_encode(text, key):
    f = lambda arg: alphabet[(alphabet.index(arg[0])+alphabet.index(arg[1]))%len(alphabet)]
    return ''.join(map(f, zip(text, cycle(key))))

def vijn_decode(cipher_text, key):
    f = lambda arg: alphabet[(alphabet.index(arg[0])-alphabet.index(arg[1]))%len(alphabet)]
    return ''.join(map(f, zip(cipher_text, cycle(key))))

if __name__ == '__main__':
    # Получение пути к запускаемому файлу
    current_file_path = os.path.abspath(__file__)
    current_path = os.path.dirname(current_file_path)

    # Получение названия файла и путь к нему в папке с запускаемым скриптом
    file_name = input('Введите название файла формата txt: ')
    file_path = os.path.join(current_path, file_name)

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        spec_chars = string.punctuation

        key = 'Повадится овца не хуже козы'
        key = remove_chars_from_text(key.lower().replace(" ", ""), spec_chars)

        text = remove_chars_from_text(text.lower().replace(" ", "").replace('\n', ''), spec_chars)

        result = vijn_encode(text, key)
        print(f'Result encode: {result}', sep='\n', end='\n\n')
        print(f'Result decode: {vijn_decode(result, key)}')

        # Получаем частотный словарь символов
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

    else:
        print('Такого файла нет')