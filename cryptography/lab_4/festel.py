import codecs
import os
import matplotlib.pyplot as plt
from collections import Counter
from itertools import cycle, islice

'''
Сети  Файстеля для блока 16 бит
'''

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

        fig1, (ax, ax1) = plt.subplots(2, 1, figsize=(16, 6))

        ax.bar([i for i in cp866_chars[:128]], \
               [freq_dict.get(i, 0) for i in cp866_chars[:128]])
        ax.set_title(f'Гистограмма шифрования текста. Раунд {i+1}')
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

        # График раунда
        freq_dict = Counter(''.join(defshifr))

        fig1, (ax, ax1) = plt.subplots(2, 1, figsize=(16, 6))

        ax.bar([i for i in cp866_chars[:128]], \
               [freq_dict.get(i, 0) for i in cp866_chars[:128]])
        ax.set_title(f'Гистограмма дешифрования текста. Раунд {i+1}')
        ax.set_xlabel('Символы')
        ax.set_ylabel('Частота')

        ax1.bar([i for i in cp866_chars[128:]], \
                [freq_dict.get(i, 0) for i in cp866_chars[128:]])
        ax1.set_xlabel('Символы')
        ax1.set_ylabel('Частота')

        plt.show()

    return ''.join(defshifr)

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

        key = 'Повадится овца не хуже козы'
        # key = 'Алексей'

        # шифровка текста
        result_encode = encode(text, key)
        print(f'Result encode: {result_encode}')

        # дешифровка текста
        result_decode = decode(result_encode, key)
        print(f'Result decode: {result_decode}')

    else:
        print('Такого файла нет')