import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow

from pyqt_01 import Ui_MainWindow


class MyWindows(Ui_MainWindow,QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(self.kankan)
    def kankan(self):
        print('kankan')








if __name__ == '__main__':
    app =QApplication(sys.argv)
    mywindows =MyWindows()
    # mywindows.show()
    app.exec()