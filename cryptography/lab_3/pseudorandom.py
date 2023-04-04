# Генерация ПСП с помощью LFSR
def generate_pseudo_random_sequence(register, feedback_coefficients, sequence_length):
    sequence = []
    for i in range(sequence_length):
        # Получаем следующий бит из LFSR
        next_bit = 0
        for coefficient in feedback_coefficients:
            next_bit ^= register[-coefficient]
        sequence.append(next_bit)
        # Сдвигаем регистр на один бит вправо и добавляем next_bit в крайнее правое положение
        register = [next_bit] + register[:-1]
    return sequence

# Преобразование текста в последовательность битов
def text_to_bits(text):
    bits = []
    for char in text:
        bits.extend([int(bit) for bit in bin(ord(char))[2:].zfill(8)])
    return bits

# Шифрование текста с помощью ПСП
def encrypt_text(text, feedback_coefficients, sequence_length):
    register = [1, 0, 1, 1, 0, 1]
    pseudo_random_sequence = generate_pseudo_random_sequence(register, feedback_coefficients, sequence_length)
    text_bits = text_to_bits(text)
    encrypted_bits = [text_bit ^ pseudo_random_bit for text_bit, pseudo_random_bit in zip(text_bits, pseudo_random_sequence)]
    return encrypted_bits

# Расшифровка текста с помощью ПСП
def decrypt_text(encrypted_bits, feedback_coefficients, sequence_length):
    register = [1, 0, 1, 1, 0, 1]
    pseudo_random_sequence = generate_pseudo_random_sequence(register, feedback_coefficients, sequence_length)
    decrypted_bits = [encrypted_bit ^ pseudo_random_bit for encrypted_bit, pseudo_random_bit in zip(encrypted_bits, pseudo_random_sequence)]
    decrypted_text = ''.join([chr(int(''.join([str(bit) for bit in decrypted_bits[i:i+8]]), 2)) for i in range(0, len(decrypted_bits), 8)])
    return decrypted_text




if __name__ == '__main__':

    # text = 'Мама мыла раму'

    key = '10101010'
    text = 'Hello, world!'

    feedback_coefficients = [6, 5, 4, 1]
    sequence_length = 100

    encrypted_bits = encrypt_text(text, feedback_coefficients, sequence_length)
    print('Зашифрованные биты:', encrypted_bits)

    decrypted_text = decrypt_text(encrypted_bits, feedback_coefficients, sequence_length)
    print('Расшифрованный текст:', decrypted_text)


