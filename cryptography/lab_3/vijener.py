import string
from itertools import cycle

"""
Пунт 1.2.2
Используя поговорку из таблицы по номеру в списке и алфавит Z_32 = (А...Я, е=ё)
"""

alpha_ru = [chr(ord('а')+i) for i in range(32)]

def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])

def vijn_encode(text, key):
    f = lambda arg: alpha_ru[(alpha_ru.index(arg[0])+alpha_ru.index(arg[1]))%32]
    return ''.join(map(f, zip(text, cycle(key))))

def vijn_decode(cipher_text, key):
    f = lambda arg: alpha_ru[(alpha_ru.index(arg[0])-alpha_ru.index(arg[1]))%32]
    return ''.join(map(f, zip(cipher_text, cycle(key))))

if __name__ == '__main__':

    spec_chars = string.punctuation

    key = 'Повадится овца не хуже козы'
    key = remove_chars_from_text(key.lower().replace(" ", ""), spec_chars)

    text = "абвгд"
    text = remove_chars_from_text(text.lower().replace(" ", ""), spec_chars)

    result = vijn_encode(text, key)
    print(result)