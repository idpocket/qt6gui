import sys
import string
import random
from PyQt6.QtWidgets import (QApplication,QDialog,QMessageBox)


from weather import Ui_weather

class MyWeather(Ui_weather,QDialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()




        self.pushButton.clicked.connect(self.chaxun)


    def chaxun(self):
        self.textBrowser.setText('查询后的天气')
        print(self.comboBox.currentText())
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWeather = MyWeather()
    sys.exit(app.exec())