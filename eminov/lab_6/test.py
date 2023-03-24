from PyQt6.QtWidgets import QLabel, QApplication
import sys

app = QApplication(sys.argv)

label = QLabel()
label.setText("Обозначение хи-квадрат: <font color='red'>&#967;</font><sup><font color='red'>2</font></sup>")
label.show()

sys.exit(app.exec())