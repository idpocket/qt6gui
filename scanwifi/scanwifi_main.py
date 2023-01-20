
import sys
import macwifi
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import (QApplication, QDialog, QMessageBox, QWidget, QListView)
from PyQt6.QtCore import QStringListModel

from scanwifi import Ui_ScanWifi
class ScanWifi(Ui_ScanWifi,QDialog):
    def __init__(self, parent=None):
        super(ScanWifi,self).__init__(parent)


        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.showwifi)
        self.pushButton_2.clicked.connect(self.passwordwifi)



        # self.listView.clicked.connect(self.onClickedListView)




    def showwifi(self):

        '''
        1.创建数据模型对象
        2.数据
        3.数据填入模型
        4.模型给listview
        '''

        listModel = QStringListModel()
        self.list = macwifi.name()

        listModel.setStringList(self.list)

        self.listView.setModel(listModel)
        self.listView.clicked.connect(self.onClickedListView)
        pass
    def passwordwifi(self):

        pass
    def onClickedListView(self, item):
        # print(self.list[item.row()])
        wifiname = self.list[item.row()]
        pwd = '18005875656'
        macwifi.connect(wifiname, pwd)

        QMessageBox.information(self, "QListView", self.list[item.row()]+"链接成功")
        # QMessageBox.information(self, "QListView", "链接成功")



if __name__ == '__main__':

    app = QApplication(sys.argv)
    sc = ScanWifi()
    sys.exit(app.exec())