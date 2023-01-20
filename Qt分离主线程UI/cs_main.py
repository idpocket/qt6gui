import time

from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QDialog


from cs import Ui_cs
import sys


a = 0
class Mycs(Ui_cs,QDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.c)
    def c(self):

        global a
        a = a+1

        self.pushButton.setText(f'点击了{a}次')
        # time.sleep(5)
        pass





class WorkThread(QThread):
    fs = pyqtSignal(str)
    def __init__(self,ip,port,parent=None):
        super(WorkThread,self).__init__(parent)
        self.ip = ip
        self.port = port
    def run(self):
        '''
        重写
        :return:
        '''
        print(f'ip:{self.ip},port:{self.port}')
        time.sleep(2)
        self.fs.emit("this is test")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWeather = Mycs()
    sys.exit(app.exec())