import codecs
import os
import matplotlib.pyplot as plt
from collections import Counter

'''
Режим шифрования DES: Режим простой замены (ECB, Electronic Coding Book)
'''

ROUNDS = 16

cp866_chars = []
for i in range(256):
    try:
        char = codecs.decode(bytes([i]), 'cp866')
        cp866_chars.append(char)
    except UnicodeDecodeError:
        pass

# Начальная перестановка IP
IP = [
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24,16, 8,
    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
]

# Таблица расширения для преобразования 32-битных блоков в 48-битные
EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# Таблицы S-box для преобразования из 48-бит в 32-бита
S_BOX = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
     10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11], 
]

# Таблица перестановки P, испольхуемая на выходе S-блоков
P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# Конечная перестановка IP^-1
FP = [
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25
]

# Число сдвига влево
LEFT_ROTATIONS = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

# Таблицы перестановки и перевода
K1P = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36
]

K2P = [
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]

# Таблицы CP для преобразования из 56-бит в 48-бит
CP = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

def string_to_bitList(text):
    '''Возвращает массив битов, где символ кодируется в кодировке cp866'''
    return [int(bit) for ch in bytes(text, 'cp866') \
            for bit in bin(ch)[2:].zfill(8)]

def bitList_to_string(data):
    '''Возращает строку, где массив битов декодируется в кодировке cp866'''
    bytes_hex = bytes([int(''.join(str(bit) for bit in data[i:i+8]), 2) \
                       for i in range(0, len(data), 8)])
    return bytes_hex.decode('cp866')

def permutation(data, table):
    '''Перестановка блока с указанной таблицей'''
    return list(map(lambda x: data[x - 1], table))

def round_feistel_cipher(data1, data2, key):
    temp = data2
    data2 = permutation(data2, EXPANSION_TABLE)
    data2 = list(map(lambda x, y: x ^ y, data2, key))
    s_box6b = [
        data2[:6], data2[6:12], data2[12:18], data2[18:24], 
        data2[24:30], data2[30:36], data2[36:42], data2[42:]
    ]
    box32b = [0] * 32
    pos = 0
    for i in range(8):
        m = (s_box6b[i][0] << 1) + s_box6b[i][5]
        n = (s_box6b[i][1] << 3) + (s_box6b[i][2] << 2) + (s_box6b[i][3] << 1) + s_box6b[i][4]

        v = S_BOX[i][(m << 4) + n]

        box32b[pos] = (v & 8) >> 3
        box32b[pos + 1] = (v & 4) >> 2
        box32b[pos + 2] = (v & 2) >> 1
        box32b[pos + 3] = v & 1

        pos += 4
    data2 = permutation(data2, P)
    data2 = list(map(lambda x, y: x ^ y, data1, data2))

    data1 = temp

    return data1, data2

def feistel_cipher(data1, data2, keys):
    for i in range(ROUNDS):
        data1, data2 = round_feistel_cipher(data1, data2, keys[i])
    data1, data2 = data2, data1
    return data1 + data2

def create_keys(key):

    keys = []

    bits = string_to_bitList(key)

    c = permutation(bits, K1P)
    d = permutation(bits, K2P)

    for i in range(16):
        j = 0

        while j < LEFT_ROTATIONS[i]:
            c.append(c[0])
            del c[0]

            d.append(d[0])
            del d[0]

            j += 1

        keys.append(permutation(c + d, CP))

    return keys

def des(bits, keys):

    result = []

    # дополняем нулями для получения целых блоков
    if len(bits) % 64 != 0:
        pad = -len(bits) % 64
        bits += [0] * pad

    for i in range(0, len(bits), 64):
        block64b = bits[i:i+64]
        # начальная перестановка
        block64b = permutation(block64b, IP)
        # разделяем блок на 2 блока по 32 бита
        block32b_1, block32b_2 = block64b[:32], block64b[32:]
        # выполнение 16 райндов фейстеля
        block64b = feistel_cipher(block32b_1, block32b_2, keys)
        # обратная перестановка
        block64b = permutation(block64b, FP)

        result += block64b
    
    result = bitList_to_string(result)

    return result

test = 'Шлепа, скажи кар!!! Kar. Че за nax?'
key = 'ключ64б!'

bits = string_to_bitList(test)

keys = create_keys(key)
result = des(bits, keys)

bits = string_to_bitList(result)

decode = des(bits, keys[::-1])

print(f'зашифрован: {result}')
print(f'расшифровка: {decode}')

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

    else:
        print('Такого файла нет')