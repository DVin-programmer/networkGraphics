# coding: utf8
'''
Программа для построения сетевых графиков
-----------------------------------------
Автор: Винокурова Д.В.
'''
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from files.general_methods import StyleWidgets

# Преобразование LaTeX в http запрос
def httpText(strF):
    strF = strF.replace("\\", "%5C")
    strF = strF.replace("{", "%7B")
    strF = strF.replace("}", "%7D")
    strF = strF.replace(" ", "%20")
    strF = strF.replace("^", "%5E")
    strF = strF.replace("\n", "%0A")
    strF = strF.replace("&", "%26")

    strHTTP1 = "https://math.now.sh?from="
    strHTTP = strHTTP1 + strF + ".png"
    return strHTTP

# Генератор цвета
def colorGenerate():
    r = randint(43, 240)
    g = randint(72, 240)
    b = randint(70, 240)
    res_RGB = "#" + str(hex(r)[2:]) + str(hex(g)[2:]) + str(hex(b)[2:])
    return res_RGB

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Ui_MainWindow, self).__init__(*args, **kwargs)
        #self.setFixedSize(750, 728)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(11)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 181, 16))
        self.label.setObjectName("label")
        self.label.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.spinBox_num_jobs = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_num_jobs.setGeometry(QtCore.QRect(220, 39, 42, 22))
        self.spinBox_num_jobs.setValue(10)
        self.spinBox_num_jobs.setObjectName("spinBox_num_jobs")
        self.spinBox_num_jobs.setFont(font)

        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(290, 36, 75, 27))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_next.clicked.connect(self.create_table)
        self.pushButton_next.setFont(font)
        background_color = "#51d77a"
        border_color = "#2d8849"
        color = "#2d8849"
        background_color_hover = "#75e998"
        border_color_hover = "#2d8849"
        color_hover = "#2d8849"
        background_color_press = "#17c14b"
        border_color_press = "#2d8849"
        color_press = "#75e998"
        border_width = "1px"
        border_radius = "2px"
        button_style = StyleWidgets()
        button_style.properties_button(self.pushButton_next, background_color,
                                    border_color, color,
                                    background_color_hover, border_color_hover, color_hover,
                                    background_color_press, border_color_press, color_press,
                                    border_width, border_radius)

        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(390, 36, 85, 27))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.pushButton_reset.setFont(font)
        self.pushButton_reset.clicked.connect(self.clear_info)
        background_color = "#fa7070"
        border_color = "#9a2222"
        color = "#9a2222"
        background_color_hover = "#f3a5a5"
        border_color_hover = "#9a2222"
        color_hover = "#9a2222"
        background_color_press = "#d33a3a"
        border_color_press = "#9a2222"
        color_press = "#f3a5a5"
        border_width = "1px"
        border_radius = "2px"
        button_style.properties_button(self.pushButton_reset, background_color,
                                    border_color, color,
                                    background_color_hover, border_color_hover, color_hover,
                                    background_color_press, border_color_press, color_press,
                                    border_width, border_radius)

            #central_widget = QtWidgets.QWidget(self.centralwidget)
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

        self.table_jobs = QtWidgets.QTableWidget(self.centralwidget)  # Создаём таблицу
        self.table_jobs.setFont(font)
        self.table_jobs.setColumnCount(3)  # Устанавливаем 5 столбцов
        # Прописываем наименование столбцов
        self.table_jobs.setHorizontalHeaderLabels(["Номер \n работы", "Описание работы",
                                                        "Длительность \n(в днях)"])
        self.table_jobs.setVisible(False)
        self.table_jobs.resizeColumnsToContents()
        self.table_jobs.resizeRowsToContents()
        self.table_jobs.setGeometry(QtCore.QRect(20, 120, 530, 285))
        self.table_jobs.setColumnWidth(1, 350)


        self.pushButton_order_of_work = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_order_of_work.setText("Установить порядок \n выполнения работ")
        self.pushButton_order_of_work.setGeometry(QtCore.QRect(390, 450, 150, 54))
        self.pushButton_order_of_work.setObjectName("pushButton_order_of_work")
        self.pushButton_order_of_work.clicked.connect(self.check_table)
        self.pushButton_order_of_work.setFont(font)
        background_color = "#6cbef1"
        border_color = "#155b87"
        color = "#155b87"
        background_color_hover = "#bbe1f9"
        border_color_hover = "#155b87"
        color_hover = "#155b87"
        background_color_press = "#3a84b3"
        border_color_press = "#3a84b3"
        color_press = "#155b87"
        border_width = "1px"
        border_radius = "2px"
        button_style = StyleWidgets()
        button_style.properties_button(self.pushButton_order_of_work, background_color,
                                       border_color, color,
                                       background_color_hover, border_color_hover, color_hover,
                                       background_color_press, border_color_press, color_press,
                                       border_width, border_radius)
        self.pushButton_order_of_work.setVisible(False)


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
        self.pushButton_next.setText(_translate("MainWindow", "Далее"))
        self.pushButton_reset.setText(_translate("MainWindow", "Сбросить"))
        self.label.setText(_translate("MainWindow", "Выберите количество работ:"))

    def create_table(self):
        '''
        Создание таблицы с необходимым количеством строк,
        указанных в spinBox
        '''
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(11)

        self.msg_box = QtWidgets.QMessageBox()
        self.msg_box.setFixedSize(100, 500)
        self.msg_box.adjustSize()

        self.num_str_in_table = self.spinBox_num_jobs.value()
        if 0 <= self.num_str_in_table <= 4:
            print("Введите большее количество работ")
            self.msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            self.msg_box.setWindowTitle("Предупреждение")
            self.msg_box.setText("Введите большее количество работ!")
            self.msg_box.setFont(font)
            self.msg_box.exec()
        else:
            # Делаем кнопку неактивной, задаем стиль
            self.pushButton_next.setEnabled(False)
            self.pushButton_next.setStyleSheet('''
                    background-color: "#cccccc";
                    border-style: solid;
                    border-color: "#909090";
                    border-width: 1px;
                    border-radius: 2px;
                    color: "#909090";''')

            self.spinBox_num_jobs.setEnabled(False)
            self.pushButton_order_of_work.setVisible(True)

            self.table_jobs.setVisible(True)
            self.table_jobs.setRowCount(self.num_str_in_table)  # строки
            self.table_jobs.setFont(font)

            # Удаление номеров
            self.table_jobs.verticalHeader().setVisible(False)
            self.table_jobs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            # Устанавливаем выравнивание на заголовки
            for i in range(0, 3):
                self.table_jobs.horizontalHeaderItem(i).setTextAlignment(QtCore.Qt.AlignHCenter)

            # Заполнение номеров работ
            for i in range(0, self.num_str_in_table):
                num_jobs_table = QtWidgets.QTableWidgetItem(str(i + 1))
                # print(i)
                self.table_jobs.setItem(i, 0, num_jobs_table)
                num_jobs_table.setTextAlignment(QtCore.Qt.AlignCenter)
                num_jobs_table.setFlags(QtCore.Qt.ItemIsEnabled)

            # Заполнение остальных ячеек
            for i in range(0, self.num_str_in_table):
                for j in range(1, 3):
                    cell = QtWidgets.QTableWidgetItem("")
                    self.table_jobs.setItem(i, j, cell)
                    cell.setTextAlignment(QtCore.Qt.AlignCenter)
                    #cell.setFlags(QtCore.Qt.ItemIsEnabled)

    def check_table(self):
        '''
        Проверяет поля таблицы на корректность.
        '''
        print("Вызов метода check_table")
        # Проверка столбца "Описание работы"
        for i in range(0, self.num_str_in_table):
            cell = self.table_jobs.item(i, 1).text()
            print(cell)
            if cell == "":
                self.table_jobs.item(i, 1).setBackground(QtGui.QColor("#f78989"))
            else:
                self.table_jobs.item(i, 1).setBackground(QtGui.QColor("#ffffff"))

        # Проверка столбца "Длительность"
        self.table_jobs.setStyleSheet("QTableWidget::item:selected{ background-color: #4f7cfc}")
        for i in range(0, self.num_str_in_table):
            cell = self.table_jobs.item(i, 2).text()
            print(cell)
            if cell == "" or not(cell.isdigit()):
                self.table_jobs.item(i, 2).setBackground(QtGui.QColor("#f78989"))
            else:
                self.table_jobs.item(i, 2).setBackground(QtGui.QColor("#ffffff"))

    def clear_info(self):
        '''
        Метод возвращает окно в исходное состояние
        '''
        self.table_jobs.setRowCount(0)
        self.table_jobs.setVisible(False)
        self.pushButton_order_of_work.setVisible(False)
        self.spinBox_num_jobs.setEnabled(True)
        self.pushButton_next.setEnabled(True)
        background_color = "#51d77a"
        border_color = "#2d8849"
        color = "#2d8849"
        background_color_hover = "#75e998"
        border_color_hover = "#2d8849"
        color_hover = "#2d8849"
        background_color_press = "#17c14b"
        border_color_press = "#2d8849"
        color_press = "#75e998"
        border_width = "1px"
        border_radius = "2px"
        button_style = StyleWidgets()
        button_style.properties_button(self.pushButton_next, background_color,
                                       border_color, color,
                                       background_color_hover, border_color_hover, color_hover,
                                       background_color_press, border_color_press, color_press,
                                       border_width, border_radius)











if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Ui_MainWindow()
    #w.resize(320, 240)
    w.show()
    sys.exit(app.exec_())