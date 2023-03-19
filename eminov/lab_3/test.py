from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sys

class ArrayWidget(QWidget):
    def __init__(self, array):
        super().__init__()
        self.array = array
        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)
        self.init_table()

    def init_table(self):
        # установка количества строк и столбцов таблицы
        self.table.setRowCount(len(self.array))
        self.table.setColumnCount(1)
        # заполнение таблицы данными из массива
        for i in range(len(self.array)):
            item = QTableWidgetItem(str(self.array[i]))
            self.table.setItem(i, 0, item)

    def update_array(self, new_array):
        self.array = new_array
        # обновление данных в таблице
        for i in range(len(self.array)):
            item = QTableWidgetItem(str(self.array[i]))
            self.table.setItem(i, 0, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    array = [1, 2, 3, 4, 5]
    widget = ArrayWidget(array)
    widget.show()
    # изменение данных в массиве
    array[2] = 10
    widget.update_array(array)
    sys.exit(app.exec())
