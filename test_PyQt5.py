from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Dialog(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.resize(407, 311)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setGeometry(QtCore.QRect(20, 30, 278, 161))
        self.widget.setObjectName("widget")
        #self.widget.setStyleSheet("background: '#909090'")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.
                                           QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.verticalLayout.addLayout(self.horizontalLayout)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.
                                            QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.
                                            QSizePolicy.Minimum, QtWidgets.QSizePolicy.
                                            Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.scrollAreaTop = QtWidgets.QScrollArea(self.widget)
        self.scrollAreaTop.setWidgetResizable(True)
        self.scrollAreaTop.setFixedHeight(70)
        self.scrollAreaTop.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollAreaTop.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.verticalLayout.addWidget(self.scrollAreaTop)

        self.widget_top = QtWidgets.QWidget(self.scrollAreaTop)
        self.widget_top.setFixedWidth(1000)
        self.widget_top.setFixedHeight(100)
        self.widget_top.setStyleSheet('''
                        background: "#c6e4fb";
                        min-width: 5em;''')
        self.scrollAreaTop.setWidget(self.widget_top)

        self.label_part1 = QtWidgets.QLabel(self.widget_top)
        self.label_part1.setGeometry(QtCore.QRect(30, 20, 325, 24))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(12)
        self.label_part1.setFont(font)
        self.label_part1.setObjectName("label_part1")
        self.label_part1.setText("Укажите порядок выполнения работ.")

        self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Email Address"))
        self.pushButton.setText(_translate("Dialog", "Submit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
