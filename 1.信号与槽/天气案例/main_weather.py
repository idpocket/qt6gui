import json
import sys
import datetime
import time

import requests
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal, QThread
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow

from weather import Ui_Weather



citys = {'温州':'101210701','宁波':'101210401'}


class My_Weather(QThread):
    '''
    多线程
    '''


    weather_signal = pyqtSignal(str)
    def __init__(self,id):
        super().__init__()
        self.id = id
    def run(self):



        # 查询指定城市的天气
        url = f"https://v.api.aa1.cn/api/api-tianqi-4/?id={self.id}"
        html = requests.get(url)

        # 用json的格式返回内容
        # j = json.loads(html.text)
        # print(j["code"])
        inf = json.loads(html.text)
        # 获取城市名字
        city = inf["city"]
        # 获取温度
        temp = inf["temp"]
        # 获得当前时间
        now = datetime.datetime.now()
        # 定义时间格式
        other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        inf = f" 城市：{city}\n 温度：{temp} ℃\n 时间：{other_StyleTime}\n"

        # print(json.loads(html.text))
        self.weather_signal.emit(inf)



class MyWindows(Ui_Weather, QMainWindow):
    # 声明一个信号 只能反正函数外面
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


        self.pushButton.clicked.connect(self.get_city)
        self.my_signal.connect(self.get_weather)
        # self.weather_signal.connect(self.upadate)

    def get_city(self):

        #获取 城市的名字 发送 id
        self.city = self.comboBox.currentText()
        self.id = citys.get(self.city)
        self.my_signal.emit(self.id)
    def get_weather(self,id):
        self.my_weather = My_Weather(id=id)


        self.my_weather.start()
        self.my_weather.weather_signal.connect(self.update)

    def update(self,inf) -> None:
        self.inf = inf
        self.textBrowser.setText(inf)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindows = MyWindows()
    app.exec()
