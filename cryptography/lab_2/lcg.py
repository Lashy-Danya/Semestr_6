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
    
    import string
    import random

    alphabet = string.ascii_letters + string.digits + string.punctuation + " "
    lcg = LCG(seed=123)

    # Генерация текстовой последовательности длины 50 символов
    text_50 = ''.join([alphabet[lcg.rand() % 32] for _ in range(50)])
    print("Текст длины 50 символов: ", text_50)

    lcg = LCG(seed=123)
    # Генерация текстовой последовательности длины 100 символов
    text_100 = ''.join([alphabet[lcg.rand() % 32] for _ in range(100)])
    print("Текст длины 100 символов: ", text_100)

    lcg = LCG(seed=123)
    # Генерация текстовой последовательности длины 1000 символов
    text_1000 = ''.join([alphabet[lcg.rand() % 32] for _ in range(1000)])
    print("Текст длины 1000 символов: ", text_1000)
