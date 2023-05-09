import codecs
from itertools import cycle, islice

cp866_chars = []
for i in range(256):
    try:
        char = codecs.decode(bytes([i]), 'cp866')
        cp866_chars.append(char)
    except UnicodeDecodeError:
        pass

ROUNDS = 8

KEY = 'Алексей'
text = 'Куй железо не отходя от кассы'

block = []

if len(text) % 2 != 0:
    text = text + '.'

# Разделяем текст на блоки по 2 символа
for i in range(0, len(text), 2):
    block.append(text[i:i+2])

def festel_cript(L, R, key, iter):
    K = cp866_chars.index(key)
    temp = L ^ (((R + K) << 1) % len(cp866_chars))
    L = R
    R = temp
    if iter+1 != ROUNDS:
        end = (cp866_chars[L] + cp866_chars[R])
    else:
        end = (cp866_chars[R] + cp866_chars[L])
    return end

def festel_descript(L, R, key, iter):
    K = cp866_chars.index(key)
    temp = L ^ (((R + K) << 1) % len(cp866_chars))
    L = R
    R = temp
    if iter+1 != ROUNDS:
        end = (cp866_chars[R] + cp866_chars[L])
    else:
        end = (cp866_chars[L] + cp866_chars[R])
    return end

def encode(blocks, key):
    keys = list(islice(cycle(key), ROUNDS))

    for i in range(ROUNDS):
        shifr = []
        for block in blocks:
            item = festel_cript(cp866_chars.index(block[0]), cp866_chars.index(block[1]), keys[i], i)
            shifr.append(item)
        blocks = shifr
    return shifr

def decode(blocks, key):
    keys = list(islice(cycle(key), ROUNDS))[::-1]

    for i in range(ROUNDS):
        defshifr = []
        for block in blocks[::-1]:
            item = festel_cript(cp866_chars.index(block[0]), cp866_chars.index(block[1]), keys[i], i)
            defshifr.append(item)
        blocks = defshifr
    return defshifr

print(f'\nШифруем\n')

shifr = encode(block, KEY)
print(''.join(shifr))

print(f'\nДешифруем\n')

defshifr = decode(shifr, KEY)
print(''.join(defshifr))