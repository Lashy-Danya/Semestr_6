import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
from collections import Counter

matplotlib.use('TkAgg')

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
        
def result_lfsr():
        seed = input_seed.get()
        poly = input_poly.get()

        alphabet = [chr(letter) for letter in range(ord('а'), ord('я')+1)]

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

        if not seed and not poly:
            lfsr = LFSR(0b11011)
        elif not poly:
            lfsr = LFSR(int(seed))
        else:
            lfsr = LFSR(int(seed), int(poly))
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

        if not seed and not poly:
            lfsr = LFSR(0b11011)
        elif not poly:
            lfsr = LFSR(int(seed))
        else:
            lfsr = LFSR(int(seed), int(poly))
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

        if not seed and not poly:
            lfsr = LFSR(0b11011)
        elif not poly:
            lfsr = LFSR(int(seed))
        else:
            lfsr = LFSR(int(seed), int(poly))
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
    
    poly_frame = tk.Frame(root)
    poly_frame.pack(pady=5)
    
    # Создание метки p
    label_poly = tk.Label(poly_frame, text="Введите poly:")
    label_poly.pack(side="left", padx=5)
    label_poly.config(font=("Arial", 11))

    # Создание поля ввода p
    input_poly = tk.StringVar()
    entry_poly = tk.Entry(poly_frame, bd=3, textvariable=input_poly)
    entry_poly.pack(side="right")
    entry_poly.config(font=("Arial", 11))
    
    button = tk.Button(root, text="Получить график", command=result_lfsr, width=16, height=2)
    button.pack(pady=5)
    button.config(font=("Arial", 10))
    
    root.mainloop()