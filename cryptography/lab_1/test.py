import string
import matplotlib
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use('TkAgg')

def remove_chars_from_text(text, chars):
    """
    Удаляет указанный набор символов из исходного текста
    """
    return "".join([ch for ch in text if ch not in chars])

file_name = input('Input text file name: ')
with open('file/' + file_name, "r", encoding="ascii") as file:
    text = file.read()
text = text.lower()
spec_chars = string.punctuation + '\n«»\t—…'
text = remove_chars_from_text(text, spec_chars)
symbols_frequencies = Counter(symbol for symbol in text if symbol in string.ascii_lowercase)
print(symbols_frequencies)

x_data = [i for i in range(len(symbols_frequencies))]
y_data = [symbols_frequencies[key]  for key in sorted(symbols_frequencies.keys())]
sns.histplot(symbols_frequencies)
# plt.bar(x_data, y_data)
# plt.xticks(x_data, symbols_frequencies)
# plt.show()