import sys
import time

from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal, QThread
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow

from pyqt_01 import Ui_MainWindow



class MyThread(QThread):
    def __init__(self):
        super().__init__()
        pass
    def run(self) -> None:

        print(f'这是多线程')
        time.sleep(2)
        pass


class MyWindows(Ui_MainWindow, QMainWindow):
    # 声明一个信号 只能反正函数外面
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(self.check)
        self.my_signal.connect(self.my_sloat)
        self.pushButton_02.clicked.connect(self.check_2)
    def my_sloat(self, msg):
        print(f' 单线程')
        print(f'已接收到信息；{msg}')
        time.sleep(3)

    def check(self):
        print('正在发送信息，准备执行槽函数')
        self.my_signal.emit(f'正在发送信息，准备执行槽函数')
    def check_2(self):
        self.mythread = MyThread()
        self.mythread.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindows = MyWindows()
    # mywindows.show()
    app.exec()
