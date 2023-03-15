import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

# Data
y = ['one', 'two', 'three', 'four', 'five']
x = [5, 24, 35, 67, 12]

# Create horizontal bar chart
plt.bar(y, x, color=['red', 'blue', 'green', 'orange', 'purple'])
plt.ylabel("Pen Sold")
plt.xlabel("Price")
plt.title("Horizontal Bar Graph")
plt.legend(["Price"], loc ="lower right")

plt.show()