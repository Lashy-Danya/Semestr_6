import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
from math import gcd
from collections import Counter

matplotlib.use('TkAgg')

class BBS:
    def __init__(self, seed, p=499, q=547):

        if p % 4 != 3 or q % 4 != 3:
            raise ValueError('p и q должны быть сравнимыми с 3 по модулю 4')

        self.p = p
        self.q = q
        self.m = p * q
        self.x = seed

        if gcd(seed, self.m) != 1:
            raise ValueError('seed и m должны быть взаимно простыми')
    
    def rand(self):
        self.x = (self.x ** 2) % self.m
        return self.x
        # return self.x & 0xFFFF  # выбираем 16 младших битов
        
def result_bbs():
        seed = input_seed.get()
        p = input_p.get()
        q = input_q.get()

        alphabet = [chr(letter) for letter in range(ord('а'), ord('я')+1)]

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

        if not seed and not p and not q:
            bbs = BBS(12345)
        elif not p and not q:
            bbs = BBS(int(seed))
        elif not q:
            bbs = BBS(int(seed), int(p))
        else:
            bbs = BBS(int(seed), int(p), int(q))
        # Генерация текстовой последовательности длины 50 символов
        text_50 = ''.join([alphabet[bbs.rand() % 32] for _ in range(50)])
        # Получаем частотный словарь символов
        freq_dict_50 = Counter(text_50)
        
        ax1.bar([i for i in alphabet], [freq_dict_50.get(i, 0) for i in alphabet])
        ax1.set_title('Текст длиной 50 символов')

        if not seed and not p and not q:
            bbs = BBS(12345)
        elif not p and not q:
            bbs = BBS(int(seed))
        elif not q:
            bbs = BBS(int(seed), int(p))
        else:
            bbs = BBS(int(seed), int(p), int(q))
        # Генерация текстовой последовательности длины 100 символов
        text_100 = ''.join([alphabet[bbs.rand() % 32] for _ in range(100)])
        # Получаем частотный словарь символов
        freq_dict_100 = Counter(text_100)

        ax2.bar([i for i in alphabet], [freq_dict_100.get(i, 0) for i in alphabet])
        ax2.set_title('Текст длиной 100 символов')

        if not seed and not p and not q:
            bbs = BBS(12345)
        elif not p and not q:
            bbs = BBS(int(seed))
        elif not q:
            bbs = BBS(int(seed), int(p))
        else:
            bbs = BBS(int(seed), int(p), int(q))
        # Генерация текстовой последовательности длины 1000 символов
        text_1000 = ''.join([alphabet[bbs.rand() % 32] for _ in range(1000)])
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
    
    p_frame = tk.Frame(root)
    p_frame.pack(pady=5)
    
    # Создание метки p
    label_p = tk.Label(p_frame, text="Введите p:")
    label_p.pack(side="left", padx=5)
    label_p.config(font=("Arial", 11))

    # Создание поля ввода p
    input_p = tk.StringVar()
    entry_p = tk.Entry(p_frame, bd=3, textvariable=input_p)
    entry_p.pack(side="right")
    entry_p.config(font=("Arial", 11))
    
    q_frame = tk.Frame(root)
    q_frame.pack()
    
    # Создание метки q
    label_q = tk.Label(q_frame, text="Введите q:")
    label_q.pack(side="left", padx=5)
    label_q.config(font=("Arial", 11))

    # Создание поля ввода q
    input_q = tk.StringVar()
    entry_q = tk.Entry(q_frame, bd=3, textvariable=input_q)
    entry_q.pack(side="right")
    entry_q.config(font=("Arial", 11))
    
    button = tk.Button(root, text="Получить график", command=result_bbs, width=16, height=2)
    button.pack(pady=5)
    button.config(font=("Arial", 10))
    
    root.mainloop()