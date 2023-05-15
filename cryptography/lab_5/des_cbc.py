import codecs
import string
import os
import des
import matplotlib.pyplot as plt
from collections import Counter

cp866_chars = []
for i in range(256):
    try:
        char = codecs.decode(bytes([i]), 'cp866')
        cp866_chars.append(char)
    except UnicodeDecodeError:
        pass

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

        key = 'ключ64б!'
        iv = 'тестив01'

        # Режим ECB
        des = des.DES(key, 1, iv)
        shifr = des.crypt(text, 0)
        deshifr = des.crypt(shifr, 1)

        # Получаем частотный словарь символов
        freq_dict = Counter(shifr)

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
        ax2.set_title('Гистограмма зашифрованного текста используя режим CBC')
        ax2.set_xlabel('Символы')
        ax2.set_ylabel('Частота')

        ax3.bar([i for i in cp866_chars[128:]], [freq_dict.get(i, 0) for i in cp866_chars[128:]])
        ax3.set_xlabel('Символы')
        ax3.set_ylabel('Частота')

        plt.show()

    else:
        print('Такого файла нет')