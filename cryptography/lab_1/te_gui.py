# from PyQt5 import QtCore, QtWidgets

# app = QtWidgets.QApplication([])

# wb_patch = QtWidgets.QFileDialog.getOpenFileName()[0]
# print(wb_patch)

# Не обязательно нужен чтобы только путь получить,
# но при создании виджетов станет обязательным
# app.exec()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 104)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 50, 321, 23))
        self.pushButton.setObjectName("pushButton")
#        self.pushButton.clicked.connect(self.on_click)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

#    def on_click(self):
#        file, _ = QFileDialog.getOpenFileName(self,'Open file',None,"Image (*.png *.jpg *jpeg)")[0]
#        file, _ = QFileDialog.getOpenFileName(None, 'Open File', './', "Image (*.png *.jpg *jpeg)")


class Demo(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Demo, self).__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
#        file, _ = QFileDialog.getOpenFileName(self,'Open file',None,"Image (*.png *.jpg *jpeg)")[0]
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', "Image (*.png *.jpg *jpeg)")

        if file:
            print(file)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = Demo()
#    ui = Ui_Form()
#    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())