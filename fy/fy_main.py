import sys
import string
import random
from PyQt6.QtWidgets import (QApplication,QDialog,QMessageBox)
from fy import Ui_fy

from func import YDDict

class MyFy(Ui_fy,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton_get.clicked.connect(self.getwolds)

    def getwolds(self):
        yd = YDDict()
        key = self.textEdit_input.toPlainText()

        self.textEdit_out.setText(yd.translate(keyword=key))



if __name__ == '__main__':

    app = QApplication(sys.argv)
    myFy = MyFy()
    sys.exit(app.exec())
