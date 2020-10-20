# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Ui_MainWindow, self).__init__(*args, **kwargs)
        #self.setFixedSize(750, 728)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(180, 40, 42, 22))
        self.spinBox.setObjectName("spinBox")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 40, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 181, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)


        central_widget = QtWidgets.QWidget(self.centralwidget)
        #self.setCentralWidget(central_widget)
        #self.setWindowTitle("Сведения об экзаменуемых")

        '''self.left = 20
        self.top = 70
        self.width = 700
        self.height = 200
        self.setGeometry(self.left, self.top, self.width, self.height)'''

        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(11)

        #grid_layout = QtWidgets.QGridLayout()
        #central_widget.setLayout(grid_layout)

        table_info_exam = QtWidgets.QTableWidget(self.centralwidget)  # Создаём таблицу
        table_info_exam.setColumnCount(3)  # Устанавливаем 5 столбцов
        table_info_exam.setRowCount(30)  # строки
        table_info_exam.setFont(font)

        # Устанавливаем заголовки таблицы
        table_info_exam.setHorizontalHeaderLabels(["Номер \n работы", "Описание работы",
                                                   "Длительность (в днях)"])
        # Удаление номеров
        table_info_exam.verticalHeader().setVisible(False)
        table_info_exam.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # Устанавливаем выравнивание на заголовки
        for i in range(0, 3):
            table_info_exam.horizontalHeaderItem(i).setTextAlignment(QtCore.Qt.AlignHCenter)

        # Заполнение номеров работ
        for i in range(0, 30):
            num_jobs_table = QtWidgets.QTableWidgetItem(str(i+1))
            print(i)
            table_info_exam.setItem(i, 0, num_jobs_table)
            num_jobs_table.setTextAlignment(QtCore.Qt.AlignCenter)
            num_jobs_table.setFlags(QtCore.Qt.ItemIsEnabled)

        for i in range(0, 30):
            for j in range(1, 3):
                cell = QtWidgets.QTableWidgetItem(str(i-j*10))
                print(i, j, 30)
                table_info_exam.setItem(i, j, cell)
                cell.setTextAlignment(QtCore.Qt.AlignCenter)
                cell.setFlags(QtCore.Qt.ItemIsEnabled)

        table_info_exam.resizeColumnsToContents()
        table_info_exam.resizeRowsToContents()
        #grid_layout.addWidget(table_info_exam, 0, 0)
        table_info_exam.setGeometry(QtCore.QRect(20, 120, 520, 300))
        table_info_exam.setColumnWidth(1, 310)
        #table_info_exam.move(120, 20)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Далее"))
        self.pushButton_2.setText(_translate("MainWindow", "Сбросить"))
        self.label.setText(_translate("MainWindow", "Выберите количество работ:"))



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Ui_MainWindow()
    #w.resize(320, 240)
    w.show()
    sys.exit(app.exec_())
