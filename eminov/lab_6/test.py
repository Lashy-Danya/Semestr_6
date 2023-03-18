from PyQt6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_edit = QPlainTextEdit()
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.on_submit)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.submit_button)

        self.setCentralWidget(central_widget)

    def on_submit(self):
        text = self.text_edit.toPlainText()
        nums = list(map(int, text.split()))
        print(nums)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
