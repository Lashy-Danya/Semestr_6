class LCG:
    def __init__(self, seed, a=1103515245, c=12345, m=2**31 - 1):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def rand(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def generate_sequence(self, size):
        return [self.rand() for _ in range(size)]
    
    def generate_random_array(self, size, minimum, maximum):
        return [minimum + (self.rand() / self.m) * (maximum - minimum) for _ in range(size)]

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from collections import Counter
    
    alphabet = [chr(letter) for letter in range(ord('а'), ord('я')+1)]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

    lcg = LCG(seed=123)
    # Генерация текстовой последовательности длины 50 символов
    text_50 = ''.join([alphabet[lcg.rand() % 32] for _ in range(50)])
    # Получаем частотный словарь символов
    freq_dict_50 = Counter(text_50)

    ax1.bar([i for i in alphabet], [freq_dict_50.get(i, 0) for i in alphabet])
    ax1.set_title('Текст длиной 50 символов')

    lcg = LCG(seed=123)
    # Генерация текстовой последовательности длины 100 символов
    text_100 = ''.join([alphabet[lcg.rand() % 32] for _ in range(100)])
    # Получаем частотный словарь символов
    freq_dict_100 = Counter(text_100)

    ax2.bar([i for i in alphabet], [freq_dict_100.get(i, 0) for i in alphabet])
    ax2.set_title('Текст длиной 100 символов')

    lcg = LCG(seed=123)
    # Генерация текстовой последовательности длины 1000 символов
    text_1000 = ''.join([alphabet[lcg.rand() % 32] for _ in range(1000)])
    # Получаем частотный словарь символов
    freq_dict_1000 = Counter(text_1000)

    ax3.bar([i for i in alphabet], [freq_dict_1000.get(i, 0) for i in alphabet])
    ax3.set_title('Текст длиной 1000 символов')

    plt.show()