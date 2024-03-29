import codecs
import string
import os
import matplotlib.pyplot as plt
from collections import Counter

"""
Пунт 1.2.1
Используя константу, равную номеру студента в списке
"""

cp866_chars = []
for i in range(256):
    try:
        char = codecs.decode(bytes([i]), 'cp866')
        cp866_chars.append(char)
    except UnicodeDecodeError:
        pass

def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])

def caesae_encode(text, key):
    f = lambda arg: cp866_chars[(cp866_chars.index(arg)+key)%len(cp866_chars)]
    return ''.join(map(f, text))

def caesae_decode(text, key):
    f = lambda arg: cp866_chars[(cp866_chars.index(arg)-key)%len(cp866_chars)]
    return ''.join(map(f, text))

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

        # text = remove_chars_from_text(text.replace(" ", "").replace('\n', ''), spec_chars)

        key = 1

        result = caesae_encode(text, key)
        print(f'Result encode: {result}', end='\n\n')
        print(f'Result decode: {caesae_decode(result, key)}')

        # Получаем частотный словарь символов
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

    else:
        print('Такого файла нет')