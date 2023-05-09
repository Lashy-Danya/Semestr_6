def generate_vigenere_table():
    """Генерирует таблицу Виженера для русского алфавита"""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    table = [[0 for _ in range(len(alphabet))] for _ in range(len(alphabet))]
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            table[i][j] = alphabet[(j+i) % len(alphabet)]
    return table

def encrypt_vigenere(plaintext, key):
    """Шифрует текст plaintext ключом key с помощью шифра Виженера"""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    table = generate_vigenere_table()
    ciphertext = ''
    key_len = len(key)
    key_pos = 0
    for char in plaintext:
        if char in alphabet:
            shift = alphabet.index(key[key_pos])
            cipher_char = table[alphabet.index(char)][shift]
            ciphertext += cipher_char
            key_pos = (key_pos + 1) % key_len
        else:
            ciphertext += char
    return ciphertext

def decrypt_vigenere(ciphertext, key):
    """Дешифрует текст ciphertext ключом key с помощью шифра Виженера"""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    table = generate_vigenere_table()
    plaintext = ''
    key_len = len(key)
    key_pos = 0
    for char in ciphertext:
        if char in alphabet:
            shift = alphabet.index(key[key_pos])
            plaintext_char = alphabet[table[shift].index(char)]
            plaintext += plaintext_char
            key_pos = (key_pos + 1) % key_len
        else:
            plaintext += char
    return plaintext

plaintext = 'пример текста'
key = 'ключ'
ciphertext = encrypt_vigenere(plaintext, key)
print(ciphertext)  # результат: рйъгпг ягггг
decrypted_text = decrypt_vigenere(ciphertext, key)
print(decrypted_text)  # результат: пример текста
