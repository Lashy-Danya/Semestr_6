def caesae_encode(text, key):
    
    result = ''

    for char in text:
        if char.isalpha():
            char_code = ord(char) - ord('а')
            shift_code = (char_code + key) % 32
            shift_char = chr(shift_code + ord('а'))
            result += shift_char

    return result

def caesae_decode(cipher_text, key):

    result = ''

    for char in cipher_text:
        if char.isalpha():
            char_code = ord(char) - ord('а')
            shift_code = (char_code - key) % 32
            shift_char = chr(shift_code + ord('а'))
            result += shift_char

    return result

if __name__ == '__main__':
    
    key = 1
    text = 'Мама мыла раму'

    result = caesae_encode(text.lower(), key)
    print(result)
    print(caesae_decode(result, key))