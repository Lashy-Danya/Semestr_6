import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
from collections import Counter

matplotlib.use('TkAgg')

class LCG:
    def __init__(self, seed, a=1103515245, c=12345, m=2**31 - 1):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def rand(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state
        
def result_lcg():
        seed = input_seed.get()
        a = input_a.get()
        c = input_c.get()

        alphabet = [chr(letter) for letter in range(ord('а'), ord('я')+1)]

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

        if not seed and not a and not c:
            lcg = LCG(seed=123)
        elif not a and not c:
            lcg = LCG(int(seed))
        elif not c:
            lcg = LCG(int(seed), int(a))
        else:
            lcg = LCG(int(seed), int(a), int(c))
        # Генерация текстовой последовательности длины 50 символов
        text_50 = ''.join([alphabet[lcg.rand() % 32] for _ in range(50)])
        # Получаем частотный словарь символов
        freq_dict_50 = Counter(text_50)

        ax1.bar([i for i in alphabet], [freq_dict_50.get(i, 0) for i in alphabet])
        ax1.set_title('Текст длиной 50 символов')

        if not seed and not a and not c:
            lcg = LCG(seed=123)
        elif not a and not c:
            lcg = LCG(int(seed))
        elif not c:
            lcg = LCG(int(seed), int(a))
        else:
            lcg = LCG(int(seed), int(a), int(c))
        # Генерация текстовой последовательности длины 100 символов
        text_100 = ''.join([alphabet[lcg.rand() % 32] for _ in range(100)])
        # Получаем частотный словарь символов
        freq_dict_100 = Counter(text_100)

        ax2.bar([i for i in alphabet], [freq_dict_100.get(i, 0) for i in alphabet])
        ax2.set_title('Текст длиной 100 символов')

        if not seed and not a and not c:
            lcg = LCG(seed=123)
        elif not a and not c:
            lcg = LCG(int(seed))
        elif not c:
            lcg = LCG(int(seed), int(a))
        else:
            lcg = LCG(int(seed), int(a), int(c))
        # Генерация текстовой последовательности длины 1000 символов
        text_1000 = ''.join([alphabet[lcg.rand() % 32] for _ in range(1000)])
        # Получаем частотный словарь символов
        freq_dict_1000 = Counter(text_1000)

        ax3.bar([i for i in alphabet], [freq_dict_1000.get(i, 0) for i in alphabet])
        ax3.set_title('Текст длиной 1000 символов')

        plt.show()
        
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Лабораторная работа 1")
    # root.minsize(400, 200)
    root.geometry("400x200")
    root.resizable(False, False)
    
   # Создание пустых рамок для отступов
    top_frame = tk.Frame(root, height=20)
    top_frame.pack()

    bottom_frame = tk.Frame(root, height=20)
    bottom_frame.pack()
    
    seed_frame = tk.Frame()
    seed_frame.pack(pady=5)
    
    # Создание метки seed
    label_seed = tk.Label(seed_frame, text="Введите seed:")
    label_seed.pack(side="left", padx=5)
    label_seed.config(font=("Arial", 11))

    # Создание поля ввода sedd
    input_seed = tk.StringVar()
    entry_seed = tk.Entry(seed_frame, bd=3, textvariable=input_seed)
    entry_seed.pack(side="right")
    entry_seed.config(font=("Arial", 11))
    
    a_frame = tk.Frame(root)
    a_frame.pack(pady=5)
    
    # Создание метки p
    label_a = tk.Label(a_frame, text="Введите a:")
    label_a.pack(side="left", padx=5)
    label_a.config(font=("Arial", 11))

    # Создание поля ввода p
    input_a = tk.StringVar()
    entry_a = tk.Entry(a_frame, bd=3, textvariable=input_a)
    entry_a.pack(side="right")
    entry_a.config(font=("Arial", 11))
    
    c_frame = tk.Frame(root)
    c_frame.pack()
    
    # Создание метки q
    label_c = tk.Label(c_frame, text="Введите c:")
    label_c.pack(side="left", padx=5)
    label_c.config(font=("Arial", 11))

    # Создание поля ввода q
    input_c = tk.StringVar()
    entry_c = tk.Entry(c_frame, bd=3, textvariable=input_c)
    entry_c.pack(side="right")
    entry_c.config(font=("Arial", 11))
    
    button = tk.Button(root, text="Получить график", command=result_lcg, width=16, height=2)
    button.pack(pady=5)
    button.config(font=("Arial", 10))
    
    root.mainloop()