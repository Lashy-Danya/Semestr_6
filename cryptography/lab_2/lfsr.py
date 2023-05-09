class LFSR:
    def __init__(self, seed, poly = 0b10100):
        self.state = seed
        self.poly = poly # порождающий полином: x^5 + x^3 + 1

    def rand(self):
        output = self.state & 1
        self.state >>= 1
        if output:
            self.state ^= self.poly
        return output

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from collections import Counter

    alphabet = [chr(letter) for letter in range(ord('а'), ord('я')+1)]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

    lfsr = LFSR(0b11011)
    arr = []

    for i in range(50):
        rand_int = 0
        for j in range(5):
            rand_int |= lfsr.rand() << j
        arr.append(rand_int)
    # Генерация текстовой последовательности длины 50 символов
    text_50 = ''.join([alphabet[i] for i in arr])
    # Получаем частотный словарь символов
    freq_dict_50 = Counter(text_50)
    
    ax1.bar([i for i in alphabet], [freq_dict_50.get(i, 0) for i in alphabet])
    ax1.set_title('Текст длиной 50 символов')

    lfsr = LFSR(0b11011)
    arr = []

    for i in range(100):
        rand_int = 0
        for j in range(5):
            rand_int |= lfsr.rand() << j
        arr.append(rand_int)
    # Генерация текстовой последовательности длины 100 символов
    text_100 = ''.join([alphabet[i] for i in arr])
    # Получаем частотный словарь символов
    freq_dict_100 = Counter(text_100)

    ax2.bar([i for i in alphabet], [freq_dict_100.get(i, 0) for i in alphabet])
    ax2.set_title('Текст длиной 100 символов')

    lfsr = LFSR(0b11011)
    arr = []

    for i in range(1000):
        rand_int = 0
        for j in range(5):
            rand_int |= lfsr.rand() << j
        arr.append(rand_int)
    # Генерация текстовой последовательности длины 1000 символов
    text_1000 = ''.join([alphabet[i] for i in arr])
    # Получаем частотный словарь символов
    freq_dict_1000 = Counter(text_1000)

    ax3.bar([i for i in alphabet], [freq_dict_1000.get(i, 0) for i in alphabet])
    ax3.set_title('Текст длиной 1000 символов')

    plt.show()