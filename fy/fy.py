# Form implementation generated from reading ui file 'fy.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_fy(object):
    def setupUi(self, fy):
        fy.setObjectName("fy")
        fy.resize(633, 388)
        self.layoutWidget = QtWidgets.QWidget(fy)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 70, 522, 235))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_us = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_us.setObjectName("comboBox_us")
        self.comboBox_us.addItem("")
        self.comboBox_us.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_us)
        self.comboBox_en = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_en.setObjectName("comboBox_en")
        self.comboBox_en.addItem("")
        self.comboBox_en.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_en)
        self.pushButton_get = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_get.setEnabled(True)
        self.pushButton_get.setObjectName("pushButton_get")
        self.horizontalLayout.addWidget(self.pushButton_get)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_input = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_input.setObjectName("textEdit_input")
        self.horizontalLayout_2.addWidget(self.textEdit_input)
        self.textEdit_out = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_out.setObjectName("textEdit_out")
        self.horizontalLayout_2.addWidget(self.textEdit_out)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(fy)
        QtCore.QMetaObject.connectSlotsByName(fy)

    def retranslateUi(self, fy):
        _translate = QtCore.QCoreApplication.translate
        fy.setWindowTitle(_translate("fy", "翻译软件"))
        self.comboBox_us.setItemText(0, _translate("fy", "英文"))
        self.comboBox_us.setItemText(1, _translate("fy", "中文"))
        self.comboBox_en.setItemText(0, _translate("fy", "中文"))
        self.comboBox_en.setItemText(1, _translate("fy", "英文"))
        self.pushButton_get.setText(_translate("fy", "查询"))
        self.textEdit_input.setHtml(_translate("fy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">输入文本</p></body></html>"))
        self.textEdit_out.setHtml(_translate("fy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">翻译</p></body></html>"))
