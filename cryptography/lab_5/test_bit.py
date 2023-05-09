import codecs

cp866_chars = []
for i in range(256):
    try:
        char = codecs.decode(bytes([i]), 'cp866')
        cp866_chars.append(char)
    except UnicodeDecodeError:
        pass

string = 'Шлепа кар!?'

data = [cp866_chars.index(ch) for ch in string]

list_bit = len(data) * 8
result = [0] * list_bit
pos = 0
for ch in data:
    i = 7
    while i >= 0:
        if ch & (1 << i) != 0:
            result[pos] = 1
        else:
            result[pos] = 0
        pos += 1
        i -= 1

print(f'Индексы: {data}')
print(f'Перевод в биты: {result}')

result_bytes = [int(bit) for ch in bytes(string, 'cp866') for bit in bin(ch)[2:].zfill(8)]
print(f'Перевод в биты 2 способ: {result_bytes}')

data = []
pos = 0
c = 0
while pos < len(result):
    c += result[pos] << (7 - (pos % 8))
    if (pos % 8) == 7:
        data.append(c)
        c = 0
    pos += 1

print(f'Перевод в символы: {"".join([cp866_chars[c] for c in data])}')

result_string = bytes([int(''.join(str(bit) for bit in result_bytes[i:i+8]), 2) for i in range(0, len(result_bytes), 8)])
print(result_string)
result_string = result_string.decode('cp866')

print(f'Перевод в символы 2 способ: {result_string}')

print(0x00)
pad = 3
null_bytes = [0] * (pad * 8)
null_bytes = bytes(int(''.join(str(bit) for bit in null_bytes[i:i+8]), 2) for i in range(0, len(null_bytes), 8))
text = 'Кар'
arr = b'\x00' * pad
print(arr)
print(len(text + arr.decode('cp866')))
text += null_bytes.decode('cp866')
print(len(text))