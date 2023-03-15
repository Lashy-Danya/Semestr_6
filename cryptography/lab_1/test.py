import string
import matplotlib
from collections import Counter
import matplotlib.pyplot as plt
from math import log2
import numpy as np
import struct

matplotlib.use('TkAgg')

def remove_chars_from_text(text, chars):
    """
    Удаляет указанный набор символов из исходного текста
    """
    return "".join([ch for ch in text if ch not in chars])

# file_name = input('Введите название текстового файла: ')
# with open('file/' + file_name, "r", encoding="ascii") as file:
#     text = file.read().lower()
# spec_chars = string.punctuation + '\n«»\t—…'
# text = remove_chars_from_text(text, spec_chars)
# symbols_frequencies = Counter(symbol for symbol in text if symbol in string.ascii_lowercase)
# print(symbols_frequencies, end='\n')

# # Расчет информационной меры файла
# total_letters = sum(symbols_frequencies.values())
# letter_prob = {letter: freq/total_letters for letter, freq in symbols_frequencies.items()}
# print(letter_prob, end='\n')
# entropy = -sum(p * log2(p) for p in letter_prob.values())
# print(f'Entropy: {entropy}')

# sybol_data = [symbol for symbol, freq in symbols_frequencies.most_common()]
# freqs = [freq for symbol, freq in symbols_frequencies.most_common()]
# plt.bar(sybol_data, freqs)
# plt.xlabel("Symbols")
# plt.ylabel("Counter")
# plt.show()

file_name = input('Введите название файла изображения: ')
with open('file/' + file_name, "rb") as file:
    img_data = file.read()

encoding = 'utf-8'
header_data = np.array(struct.unpack('<2sIHHIIIIHHIIIIII', img_data[:54]))
print(f'Type file: {str(header_data[0], encoding)}')
print(f'Size file: {str(header_data[1], encoding)}')
print(f'Reserved 1: {str(header_data[2], encoding)}')
print(f'Reserved 2: {str(header_data[3], encoding)}')
print(f'Offset: {str(header_data[4], encoding)}')
print(f'DIB Header Size: {str(header_data[5], encoding)}')
print(f'Width: {str(header_data[6], encoding)}')
print(f'Height: {str(header_data[7], encoding)}')
print(f'Colour Planes: {str(header_data[8], encoding)}')
print(f'Bits per Pixel: {str(header_data[9], encoding)}')
print(f'Compression Method: {str(header_data[10], encoding)}')
print(f'Raw Image Size: {str(header_data[11], encoding)}')
print(f'Horizontal Resolution: {str(header_data[12], encoding)}')
print(f'Vertical Resolution: {str(header_data[13], encoding)}')
print(f'Number of Colours: {str(header_data[14], encoding)}')
print(f'Important Colours: {str(header_data[15], encoding)}', end='\n\n')

img_data = bytearray(img_data[54:])

color_tier = 0
mas_blue = []
mas_green = []
mas_red = []
w = 0

for pixel in img_data[0:]:
    if (color_tier == 0) & (int(pixel) == int(0)) & (w == int(header_data[6])):
        w = 0
        continue
    if color_tier == 0:
        mas_blue.append(pixel)
        color_tier = color_tier + 1
    elif color_tier == 1:
        mas_green.append(pixel)
        color_tier = color_tier + 1
    elif color_tier == 2:
        mas_red.append(pixel)
        color_tier = 0
        w = w + 1

mas_blue = Counter(mas_blue)
mas_green = Counter(mas_green)
mas_red = Counter(mas_red)

# print(mas_blue)
# print(mas_green)
# print(mas_red)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

color_data_blue = [color for color, freq in mas_blue.most_common()]
freqs_blue = [freq for color, freq in mas_blue.most_common()]
ax1.bar(color_data_blue, freqs_blue)
ax1.set_title('Blue')

color_data_green = [color for color, freq in mas_green.most_common()]
freqs_green = [freq for color, freq in mas_green.most_common()]
ax2.bar(color_data_green, freqs_green, color='g')
ax2.set_title('Green')

color_data_red = [color for color, freq in mas_red.most_common()]
freqs_red = [freq for color, freq in mas_red.most_common()]
ax3.bar(color_data_red, freqs_red, color='r')
ax3.set_title('Red')

# Информационная мера синего цвета
total_letters_blue = sum(mas_blue.values())
letter_prob_blue = {letter: freq/total_letters_blue for letter, freq in mas_blue.items()}
entropy_blue = -sum(p * log2(p) for p in letter_prob_blue.values())
print(f'Entropy Blue Color: {entropy_blue}')

# Информационная мера зеленого цвета
total_letters_green = sum(mas_green.values())
letter_prob_green = {letter: freq/total_letters_green for letter, freq in mas_green.items()}
entropy_green = -sum(p * log2(p) for p in letter_prob_green.values())
print(f'Entropy Green Color: {entropy_green}')

# Информационная мера красного цвета
total_letters_red = sum(mas_red.values())
letter_prob_red = {letter: freq/total_letters_red for letter, freq in mas_red.items()}
entropy_red = -sum(p * log2(p) for p in letter_prob_red.values())
print(f'Entropy Green Color: {entropy_red}')

plt.show()