from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt6.QtCore import QStringListModel
import sys


class ListViewDemo(QWidget):
    def __init__(self, parent=None):
        super(ListViewDemo, self).__init__(parent)
        self.setWindowTitle("QListView 例子")
        self.resize(300, 270)
        layout = QVBoxLayout()

        listview = QListView()
        listModel = QStringListModel()
        self.list = ["列表项1", "列表项2", "列表项3","列表项4"]

        listModel.setStringList(self.list)

        listview.setModel(listModel)
        listview.clicked.connect(self.onClickedListView)
        layout.addWidget(listview)

        self.setLayout(layout)

    def onClickedListView(self, item):
        QMessageBox.information(self, "QListView", "您选择了：" + self.list[item.row()])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec())
