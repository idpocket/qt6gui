import sys

from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow

from pyqt_01 import Ui_MainWindow


class MyWindows(Ui_MainWindow, QMainWindow):
    # 声明一个信号 只能反正函数外面
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(self.check)

        self.my_signal.connect(self.my_sloat)

    def kankan(self):
        print('kankan')

    def my_sloat(self, msg):
        print(f'已接收到信息；{msg}')

    def check(self):
        print('正在发送信息，准备执行槽函数')
        self.my_signal.emit(f'正在发送信息，准备执行槽函数')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindows = MyWindows()
    # mywindows.show()
    app.exec()
