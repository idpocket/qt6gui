import sys

from PyQt6.QtWidgets import QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox

def show_msg():
    QMessageBox.information(window,"提示",'你点击了我')

if __name__ == "__main__":
    app = QApplication(sys.argv)


    window = QDialog()
    window.resize(400,800)

    hbox = QHBoxLayout()
    button = QPushButton('点击我')
    button.clicked.connect(show_msg)

    hbox.addWidget(button)
    window.setLayout(hbox)
 

    window.show()
    sys.exit(app.exec())