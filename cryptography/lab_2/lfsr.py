class LFSR:
    def __init__(self, seed, poly = 0b101001):
        self.state = seed
        self.poly = poly # порождающий полином: x^5 + x^3 + 1

    def rand(self):
        output = self.state & 1
        self.state >>= 1
        if output:
            self.state ^= self.poly
        return output
    
    def generate_sequence(self, size):
        return [self.rand() for _ in range(size)]

if __name__ == '__main__':

    lfsr = LFSR(0b10101)  # начальное значение регистра
    text_lengths = [50, 100, 1000]

    for length in text_lengths:
        # генерация псевдослучайной последовательности битов
        bits = lfsr.generate_sequence(length*5)
        
        # преобразование последовательности битов в текстовую строку
        text = ""
        for i in range(length):
            char_code = 0
            for j in range(5):
                char_code += bits[i*5+j] * (2**(4-j))
            char = chr(char_code + ord('а'))
            text += char
        
        print(f"Тестирование на текстовой последовательности длиной {length} символов:")
        print(text)