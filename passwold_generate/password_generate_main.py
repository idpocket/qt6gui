import string
import sys
import string
import random
from PyQt6.QtWidgets import (QApplication,QDialog,QMessageBox)

from password import Ui_PasswoldGenerate




class MypasswordGenerate(Ui_PasswoldGenerate,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.select_new_passwold)
    def select_new_passwold(self):
        wolds =[]
        if self.checkBox.isChecked():
            wolds.append(string.digits*2)
        if self.checkBox_2.isChecked():
            wolds.append(string.ascii_uppercase*2)
        if self.checkBox_3.isChecked():
            wolds.append(string.ascii_lowercase*2)
        if self.checkBox_4.isChecked():
            wolds.append(string.punctuation*2)
        if not wolds:
            words = string.digits+string.ascii_uppercase+string.ascii_lowercase+string.punctuation
        else:
            wolds = "".join(wolds)
        wolds = random.sample(list(words),8)
        passwold = ''.join(wolds)
        self.lineEdit.setText(passwold)
    def new_passwold(self):
        '''生成随机密码'''
        words = string.digits+string.ascii_uppercase+string.ascii_lowercase+string.punctuation

        words = random.sample(list(words),12)
        password = "".join(words)

        self.lineEdit.setText(password)
        # QMessageBox.information(self,'提示','密码生成成功')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mypasswordGenerate = MypasswordGenerate()
    sys.exit(app.exec())