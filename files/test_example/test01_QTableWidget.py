import sys
from PyQt5 import QtGui, QtCore, QtWidgets


class MyDelegate(QtWidgets.QItemDelegate):

    def __init__(self, parent, table):
        super(MyDelegate, self).__init__(parent)
        self.table = table

    def sizeHint(self, option, index):
        # Get full viewport size
        table_size = self.table.viewport().size()
        gw = 1  # Grid line width
        rows = self.table.rowCount() or 1
        cols = self.table.columnCount() or 1
        width = (table_size.width() - (gw * (cols - 1))) / cols
        height = (table_size.height() -  (gw * (rows - 1))) / rows
        return QtCore.QSize(width, height)


class Window(QtWidgets.QWidget):
    def __init__(self, rows, columns):
        super(Window, self).__init__()
        self.lay = QtWidgets.QVBoxLayout()
        self.setLayout(self.lay)
        self.table = QtWidgets.QTableWidget(rows, columns, self)
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lay.addWidget(self.table)
        self.delegate = MyDelegate(self, self.table)
        self.table.setItemDelegate(self.delegate)

    def showEvent(self, event):
        super(Window, self).showEvent(event)
        self.resizeTable()

    def resizeTable(self):
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()

    def resizeEvent(self, event):
        super(Window, self).resizeEvent(event)
        self.resizeTable()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window(200, 300)
    #w.resize(320, 240)
    w.show()
    sys.exit(app.exec_())