import os
import string
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import struct
import math

while 1:
    option = int(input('What do you want to process:\n1)Text(.txt)\n2)Image(.bmp)\n3)Exit\n'))
    if option == 1:
        file_name = input('Input text file name: ')
        print('\n')
        file = open('file/' + file_name, "r", encoding="ascii")
        text = file.read()
        text = text.lower()
        spec_chars = string.punctuation + '\n\t'
        text = "".join([ch for ch in text if ch not in spec_chars])
        mas_char = []
        for symbol in text:
            mas_char.append(symbol)
        with open('temp.csv', 'w') as csvfile:
            fieldnames = ['char']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            temp = int(0)
            while len(mas_char) > temp:
                writer.writerow({'char': mas_char[temp]})
                temp = temp + 1
        info = pd.read_csv('temp.csv')
        plt.figure(figsize=(14, 5))
        sns.countplot(x='char', data=info)
        plt.grid()
        plt.show()
        os.remove('temp.csv')
        information_weight = float(0)
        info_size = int(0)
        for c in info.value_counts():
            info_size = info_size + c
        for c in info.value_counts():
            information_weight = information_weight + float(c) / float(info_size) * math.log2(float(info_size) / float(c))
        print('Information weight = ', information_weight)
    elif option == 2:
        # bmp picture color format BGR
        file_name = input('Input text file name: ')
        print('\n')
        bmp = open(file_name, 'rb')
        print('Type:', bmp.read(2).decode())
        print('Size: %s' % struct.unpack('I', bmp.read(4)))
        print('Reserved 1: %s' % struct.unpack('H', bmp.read(2)))
        print('Reserved 2: %s' % struct.unpack('H', bmp.read(2)))
        print('Offset: %s' % struct.unpack('I', bmp.read(4)))
        print('DIB Header Size: %s' % struct.unpack('I', bmp.read(4)))
        wight = struct.unpack('I', bmp.read(4))
        print('Width: %s' % wight)
        print('Height: %s' % struct.unpack('I', bmp.read(4)))
        print('Colour Planes: %s' % struct.unpack('H', bmp.read(2)))
        print('Bits per Pixel: %s' % struct.unpack('H', bmp.read(2)))
        print('Compression Method: %s' % struct.unpack('I', bmp.read(4)))
        print('Raw Image Size: %s' % struct.unpack('I', bmp.read(4)))
        print('Horizontal Resolution: %s' % struct.unpack('I', bmp.read(4)))
        print('Vertical Resolution: %s' % struct.unpack('I', bmp.read(4)))
        print('Number of Colours: %s' % struct.unpack('I', bmp.read(4)))
        print('Important Colours: %s' % struct.unpack('I', bmp.read(4)))
        data = bytearray(bmp.read())
        color_tier = 0
        mas_blue = []
        mas_green = []
        mas_red = []
        w = 0
        for pixel in data[0:]:
            if (color_tier == 0) & (int(pixel) == int(0)) & (w == int(wight[0])):
                w = 0
                continue
            if color_tier == 0:
                mas_blue.append(pixel)
                color_tier = color_tier + 1
            elif color_tier == 1:
                mas_green.append(pixel)
                color_tier = color_tier + 1
            elif color_tier == 2:
                mas_red.append(pixel)
                color_tier = 0
                w = w + 1
        print('COMPLETED READING IMAGE DATA')
        with open('temp_blue.csv', 'w') as csvfile:
            fieldnames = ['blue_color']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            temp = int(0)
            while len(mas_blue) > temp:
                writer.writerow({'blue_color': mas_blue[temp]})
                temp = temp + 1
        print('COMPLETED WRITING BLUE IMAGE DATA')
        with open('temp_green.csv', 'w') as csvfile:
            fieldnames = ['green_color']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            temp = int(0)
            while len(mas_green) > temp:
                writer.writerow({'green_color': mas_green[temp]})
                temp = temp + 1
        print('COMPLETED WRITING GREEN IMAGE DATA')
        with open('temp_red.csv', 'w') as csvfile:
            fieldnames = ['red_color']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            temp = int(0)
            while len(mas_red) > temp:
                writer.writerow({'red_color': mas_red[temp]})
                temp = temp + 1
        print('COMPLETED WRITING RED IMAGE DATA')
        info_blue = pd.read_csv('temp_blue.csv')
        info_green = pd.read_csv('temp_green.csv')
        info_red = pd.read_csv('temp_red.csv')
        plt.figure(figsize=(14, 5))
        plt.hist(info_blue, bins=20, edgecolor = 'black')
        plt.grid()
        plt.title('Histogram of blue color')
        plt.xlabel('Code of blue color')
        plt.ylabel('Count')
        plt.show()
        os.remove('temp_blue.csv')
        plt.figure(figsize=(14, 5))
        plt.hist(info_green, bins=20, edgecolor = 'black')
        plt.grid()
        plt.title('Histogram of green color')
        plt.xlabel('Code of green color')
        plt.ylabel('Count')
        plt.show()
        os.remove('temp_green.csv')
        plt.figure(figsize=(14, 5))
        plt.hist(info_red, bins=20, edgecolor = 'black')
        plt.grid()
        plt.title('Histogram of red color')
        plt.xlabel('Code of red color')
        plt.ylabel('Count')
        plt.show()
        os.remove('temp_red.csv')
        information_weight_blue = float(0)
        info_size_blue = int(0)
        for c in info_blue.value_counts():
            info_size_blue = info_size_blue + c
        for c in info_blue.value_counts():
            information_weight_blue = information_weight_blue + float(c) / float(info_size_blue) * math.log2(float(info_size_blue) / float(c))
        information_weight_green = float(0)
        info_size_green = int(0)
        for c in info_green.value_counts():
            info_size_green = info_size_green + c
        for c in info_green.value_counts():
            information_weight_green = information_weight_green + float(c) / float(info_size_green) * math.log2(float(info_size_green) / float(c))
        information_weight_red = float(0)
        info_size_red = int(0)
        for c in info_red.value_counts():
            info_size_red = info_size_red + c
        for c in info_red.value_counts():
            information_weight_red = information_weight_red + float(c) / float(info_size_red) * math.log2(float(info_size_red) / float(c))
        print('Information weight of BLUE color = ', information_weight_blue)
        print('Information weight of GREEN color = ', information_weight_green)
        print('Information weight of RED color = ', information_weight_red)
    elif option == 3:
        exit()
    else:
        print('There is no such option\n\n')