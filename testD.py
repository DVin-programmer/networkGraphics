# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testD.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from functools import partial
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import full_name_exam
from datetime import datetime as dt, timedelta as td


# Дата для файла
def Data():
    return dt.now().strftime("%Y-%m-%d_%H.%M.%S")


# Отсчет времени для студента (добавлено 3 минуты)
def Time():
    return dt.now()


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        global data
        lstTime = []

        data = Data()
        file = open("files\\InfoStud\\" + data + "_tikets.txt", "w", encoding="utf-8")
        file.close()

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QtCore.QSize(560, 500))

        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(13)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # Надпись времени на подготовку
        self.label_time_to_prepare = QtWidgets.QLabel(self.centralwidget)
        self.label_time_to_prepare.setGeometry(QtCore.QRect(35, 28, 230, 20))
        self.label_time_to_prepare.setFont(font)

        # Выпадающий список для установки часов
        lst_hours = []
        for i in range(0, 5):
            hours_zero_str = "0" + str(i)
            lst_hours.append(hours_zero_str)
        self.combobox_hours = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_hours.addItems(lst_hours)
        self.combobox_hours.setCurrentIndex(1)
        self.combobox_hours.move(255, 28)
        self.combobox_hours.resize(45, 25)
        self.combobox_hours.setFont(font)

        # Надпись возле выпадающего списка с значениями часов
        self.label_hours = QtWidgets.QLabel(self.centralwidget)
        self.label_hours.setGeometry(QtCore.QRect(305, 28, 230, 20))
        self.label_hours.setFont(font)

        # Выпадающий список для установки минут
        lst_minutes = []
        minutes_zero_str = ""
        for i in range(0, 60):
            if i <= 9:
                minutes_zero_str = "0" + str(i)
            else:
                minutes_zero_str = str(i)
            lst_minutes.append(minutes_zero_str)
        # combobox_minutes = ComboBox(lst_minutes, 0, self, 305, 17)
        self.combobox_minutes = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_minutes.addItems(lst_minutes)
        self.combobox_minutes.setCurrentIndex(0)
        self.combobox_minutes.move(340, 28)
        self.combobox_minutes.resize(45, 25)
        self.combobox_minutes.setFont(font)

        # Надпись возле выпадающего списка со значениями минут
        self.label_minutes = QtWidgets.QLabel(self.centralwidget)
        self.label_minutes.setGeometry(QtCore.QRect(392, 28, 230, 20))
        self.label_minutes.setFont(font)

        # Надпись возле ввода количества билетов
        self.label_sum_tickets = QtWidgets.QLabel(self.centralwidget)
        self.label_sum_tickets.setGeometry(QtCore.QRect(35, 81, 230, 20))
        self.label_sum_tickets.setFont(font)

        # Поле ввода количества билетов
        self.line_edit_sum_tickets = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_sum_tickets.move(245, 80)
        self.line_edit_sum_tickets.resize(50, 29)
        self.line_edit_sum_tickets.setPlaceholderText("0")
        self.line_edit_sum_tickets.setFont(font)
        self.line_edit_sum_tickets.setStyleSheet('''
                  background-color: "#ffffff";
                  border-style: solid;
                  border-color: "#909090";
                  border-width: 1px;
                  border-radius: 2px;
                  color: "#909090";''')

        # Кнопка "Далее"
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(310, 78, 90, 32))
        self.nextButton.setFont(font)
        bg_color = "#51d77a"
        border_color = "#2d8849"
        color = "#2d8849"
        bg_color_h = "#75e998"
        border_color_h = "#2d8849"
        color_h = "#2d8849"
        bg_color_p = "#17c14b"
        border_color_p = "#2d8849"
        color_p = "#75e998"
        border_width = "2px"
        border_radius = "2px"
        self.properties_button(self.nextButton, bg_color,
                               border_color, color,
                               bg_color_h, border_color_h, color_h,
                               bg_color_p, border_color_p, color_p,
                               border_width, border_radius)

        # Кнопка "Очистить"
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(410, 78, 100, 32))
        self.clearButton.setFont(font)
        bg_color = "#fa7070"
        border_color = "#9a2222"
        color = "#9a2222"
        bg_color_h = "#f3a5a5"
        border_color_h = "#9a2222"
        color_h = "#9a2222"
        bg_color_p = "#d33a3a"
        border_color_p = "#9a2222"
        color_p = "#f3a5a5"
        border_width = "2px"
        border_radius = "2px"
        self.properties_button(self.clearButton, bg_color, border_color, color,
                               bg_color_h, border_color_h, color_h,
                               bg_color_p, border_color_p, color_p,
                               border_width, border_radius)

        # r = self.btn(MainWindow)
        # self.nextButton.clicked.connect(self.buttonClicked)
        # self.nextButton.clicked.connect(partial(self.buttonClicked, MainWindow))
        # self.nextButton.clicked.connect(self.btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 21))

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_4 = QtWidgets.QMenu(self.menubar)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionTickets = QtWidgets.QAction(MainWindow)
        #self.menu.addAction(self.actionTickets)
        self.create_win_info_exam_table = win_InfoExamTable(self)
        self.actionTickets.triggered.connect(self.open_table_exam)
        self.menubar.addAction(self.actionTickets)

        """
        # Несколько пунктов в меню
        self.actionTickets = QtWidgets.QAction(MainWindow)
        self.menu.addAction(self.actionTickets)
        self.create_win_info_exam_table = win_InfoExamTable(self)
        self.actionTickets.triggered.connect(self.fff)
        self.menubar.addAction(self.menu.menuAction())"""

        """self.menubar.addAction(self.menu.menuAction())
        ''' Создание окна вывода информации об экзаменуемых
        self.create_win_info_exam_table = win_InfoExamTable(self)
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.trigger.connect(self.create_win_info_exam_table.show())
        self.menu_2.addAction(self.action2)'''"""
        #self.menubar.addAction(self.menu_2.menuAction())
        #self.menubar.addAction(self.menu_3.menuAction())
        #self.menubar.addAction(self.menu_4.menuAction())


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusBar()

        self.nextButton.clicked.connect(self.correct_input)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Создание окна для ввода данных об экзаменуемом
        self.create_win_full_name_exam = win_FullNameExam(self)


    def open_table_exam(self):
        print("open_table_exam")

        self.create_win_info_exam_table.show()
        self.create_win_info_exam_table.info_exam()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextButton.setText(_translate("MainWindow", "Далее"))
        self.clearButton.setText(_translate("MainWindow", "Очистить"))
        self.label_time_to_prepare.setText(_translate("MainWindow",
                                                      "Введите время на подготовку:"))
        self.label_hours.setText(_translate("MainWindow", "ч.  :"))
        self.label_minutes.setText(_translate("MainWindow", "мин."))
        self.label_sum_tickets.setText(_translate("MainWindow",
                                                  "Введите количество билетов:"))
        #self.menu.setTitle(_translate("MainWindow", "Выданные билеты"))
        self.menu_2.setTitle(_translate("MainWindow", "Открыть списки"))
        self.menu_3.setTitle(_translate("MainWindow", "Очистить списки"))
        self.menu_4.setTitle(_translate("MainWindow", "Инструкция"))

        self.actionTickets.setText(_translate("MainWindow", "Выданные билеты"))

    # Стиль кнопки
    def properties_button(self, n, bg_color, border_color, color,
                          bg_color_h, border_color_h, color_h,
                          bg_color_p, border_color_p, color_p,
                          border_width, border_radius):
        # self.n = n
        # self.setupUi(self)
        n.bg_color = bg_color
        n.border_color = border_color
        n.color = color
        n.bg_color_h = bg_color_h
        n.border_color_h = border_color_h
        n.color_h = color_h
        n.bg_color_p = bg_color_p
        n.border_color_p = border_color_p
        n.color_p = color_p
        n.border_width = border_width
        n.border_radius = border_radius
        n.setStyleSheet('''
        QPushButton:!hover
        {
          background-color: ''' + bg_color + ''';
          border-style: solid;
          border-color: ''' + border_color + ''';
          border-width: ''' + border_width + '''; 
          border-radius: ''' + border_radius + '''; 
          color: ''' + color + ''';
        }
        QPushButton:hover
        {
          background-color: ''' + bg_color_h + ''';
          border-style: solid;
          border-color: ''' + border_color_h + ''';
          border-width: ''' + border_width + '''; 
          border-radius: ''' + border_radius + '''; 
          color: ''' + color_h + ''';
        }
        QPushButton:pressed
        {
          background-color: ''' + bg_color_p + ''';
          border-style: solid;
          border-color: ''' + border_color_p + ''';
          border-width: ''' + border_width + '''; 
          border-radius:  ''' + border_radius + '''; 
          color: ''' + color_p + ''';
        }''')

    # Метод, срабатывающий по нажатию кнопки "Н"овая пачка"
    def clear_tickets(self):
        self.combobox_hours.setEnabled(True)
        self.combobox_minutes.setEnabled(True)
        self.line_edit_sum_tickets.setReadOnly(False)
        self.line_edit_sum_tickets.setStyleSheet('''
                      background-color: "#ffffff";
                      border-style: solid;
                      border-color: "#909090";
                      border-width: 1px;
                      border-radius: 2px;
                      color: "#909090";''')

    # Метод проверки введенных данных на корректность
    def correct_input(self):
        global input_hours, input_minutes
        input_hours = self.combobox_hours.currentText()
        input_minutes = self.combobox_minutes.currentText()
        self.msg_box = QtWidgets.QMessageBox()
        self.msg_box.setFixedSize(100, 500)
        self.msg_box.adjustSize()

        if (input_hours == "00") and (input_minutes == "00"):
            self.msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            self.msg_box.setWindowTitle("Предупреждение")
            self.msg_box.setText("Введите корректное время на подготовку!")
            self.msg_box.exec()
        else:
            global inputSumTickets
            inputSumTickets = self.line_edit_sum_tickets.text()
            print("inputSumTickets", inputSumTickets)
            if str(inputSumTickets).isdigit() != True:
                self.msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                self.msg_box.setWindowTitle("Предупреждение")
                self.msg_box.setText("Проверьте правильность введенных данных!")
                self.msg_box.exec()
            elif int(inputSumTickets) < 0:
                self.msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                self.msg_box.setWindowTitle("Предупреждение")
                self.msg_box.setText("Количество билетов не может " + \
                                     "быть отрицательным числом!")
                self.msg_box.exec()
            elif int(inputSumTickets) == 0:
                self.msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                self.msg_box.setWindowTitle("Предупреждение")
                self.msg_box.setText("Количество билетов равно 0!")
                self.msg_box.exec()
            elif int(inputSumTickets) > 55:
                self.msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                self.msg_box.setWindowTitle("Предупреждение")
                self.msg_box.setText("Нельзя ввести больше 55 билетов!")
                self.msg_box.exec()
            else:
                inputSumTickets = int(inputSumTickets)
                # self.show_tickets
                self.create_tickets()
                # self.hidden_tickets()

    # Создание кнопок с билетами
    def create_tickets(self):
        # отключение списков выбора, поля ввода и кнопки
        self.combobox_hours.setEnabled(False)
        self.combobox_minutes.setEnabled(False)
        self.line_edit_sum_tickets.setReadOnly(True)
        self.line_edit_sum_tickets.setStyleSheet('''
              background-color: "#cccccc";
              border-style: solid;
              border-color: "#909090";
              border-width: 1px;
              border-radius: 2px;
              color: "#909090";''')
        self.nextButton.setEnabled(False)
        self.nextButton.setStyleSheet('''
                      background-color: "#cccccc";
                      border-style: solid;
                      border-color: "#909090";
                      border-width: 2px;
                      border-radius: 2px;
                      color: "#909090";''')
        """self.nextButton.setStyleSheet('''
                      background-color: "#17c14b";
                      border-style: solid;
                      border-color: "#2d8849";
                      border-width: 2px;
                      border-radius: 2px;
                      color: "#75e998";''')"""

        global lst_btn_number
        lst_btn_number = []

        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(13)

        bg_color = "#6cbef1"
        border_color = "#155b87"
        color = "#155b87"
        bg_color_h = "#bbe1f9"
        border_color_h = "#155b87"
        color_h = "#155b87"
        bg_color_p = "#3a84b3"
        border_color_p = "#155b87"
        color_p = "#bbe1f9"
        border_width = "1px"
        border_radius = "0px"

        yI = 100
        xJ = -65
        n = 0
        for j in range(1, inputSumTickets + 1):
            n += 1
            if (n - 1) % 5 == 0:
                yI += 31
                xJ = -65
            xJ += 99  # 97

            globals()["btn" + str(j)] = QtWidgets.QPushButton(self.centralwidget)
            globals()["btn" + str(j)].setGeometry(QtCore.QRect(xJ, yI, 100, 32))
            globals()["btn" + str(j)].setFont(font)
            self.properties_button(globals()["btn" + str(j)], bg_color, border_color, color,
                                   bg_color_h, border_color_h, color_h,
                                   bg_color_p, border_color_p, color_p,
                                   border_width, border_radius)
        _translate = QtCore.QCoreApplication.translate
        for i in range(1, inputSumTickets + 1):
            globals()["btn" + str(i)].setText(_translate("MainWindow", "Билет №" + str(i)))
            globals()["btn" + str(i)].setVisible(True)
            # globals()["btn" + str(i)].clicked.connect(
            #    lambda: self.f("btn" + str(i)))
            globals()["btn" + str(i)].clicked.connect(self.pressed_Btn_ticket)

    # Метод обработки нажатой кнопки с билетом
    def pressed_Btn_ticket(self):
        global numBtn
        sender = self.sender()
        # self.statusBar().showMessage(sender.text() + ' was pressed')
        textButton = sender.text()
        resFind = textButton.find("№")
        numBtn = textButton[resFind + 1:]

        if not (numBtn in lst_btn_number):
            bg_color = "#fa7070"
            border_color = "#9a2222"
            color = "#9a2222"
            bg_color_h = "#f3a5a5"
            border_color_h = "#9a2222"
            color_h = "#9a2222"
            bg_color_p = "#d33a3a"
            border_color_p = "#9a2222"
            color_p = "#f3a5a5"
            border_width = "1px"
            border_radius = "0px"
            self.properties_button(globals()["btn" + str(numBtn)], bg_color, border_color, color,
                                   bg_color_h, border_color_h, color_h,
                                   bg_color_p, border_color_p, color_p,
                                   border_width, border_radius)
            lst_btn_number.append(numBtn)
            self.create_win_full_name_exam.show()
        else:
            bg_color = "#6cbef1"
            border_color = "#155b87"
            color = "#155b87"
            bg_color_h = "#bbe1f9"
            border_color_h = "#155b87"
            color_h = "#155b87"
            bg_color_p = "#3a84b3"
            border_color_p = "#155b87"
            color_p = "#bbe1f9"
            border_width = "1px"
            border_radius = "0px"
            self.properties_button(globals()["btn" + str(numBtn)],
                                   bg_color, border_color, color,
                                   bg_color_h, border_color_h, color_h,
                                   bg_color_p, border_color_p, color_p,
                                   border_width, border_radius)
            lst_btn_number.remove(numBtn)

    ''''# Метод скрытия билетов
    def hidden_tickets(self):
        for j in range(1, inputSumTickets  + 1):
            globals()["btn" + str(j)].setVisible(False)

    # Метод появление билетов
    def show_tickets(self):
        for j in range(1, inputSumTickets  + 1):
            globals()["btn" + str(j)].setVisible(True)'''


# Свойства окна ввода сведений об экзаменуемом
class win_FullNameExam(QtWidgets.QWidget,
                           full_name_exam.Ui_FullNameExaminee):
    def __init__(self, window):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.window = window
        # Пока дочернее окно открыто запретить переход на главное
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.pushButton_Ok.clicked.connect(self.info_exam_correct)
        print("win_FullNameExam")

    # Проверка полей ввода на корректность
    def info_exam_correct(self):
        if self.lineEdit_surname.text() == "":
            self.msg_info_exam.setWindowTitle("Предупреждение")
            self.msg_info_exam.setText("Введите фамилию!")
            self.msg_info_exam.exec()
        elif self.lineEdit_name.text() == "":
            self.msg_info_exam.setWindowTitle("Предупреждение")
            self.msg_info_exam.setText("Введите имя!")
            self.msg_info_exam.exec()
        else:
            self.info_exam_notepad()
            # self.create_win_info_exam_table.show()
            '''self.create_win_FullNameExamine = win_FullNameExaminee(self)
            self.create_win_info_exam_table = win_InfoExamTable(self)'''

    # Метод ввода сведений об экзаменуемом и времени в блокнот
    def info_exam_notepad(self):
        global final_time
        start_time = Time()
        final_time = start_time + td(hours=int(input_hours),
                                        minutes=int(input_minutes))
        print("data",data,self.lineEdit_surname.text(),
              self.lineEdit_name.text(),input_hours,input_minutes)
        file = open("files\\InfoStud\\" +  data + \
                    "_tikets.txt", "a", encoding="utf-8")
        file.write("Билет №" + str(numBtn) + "|" + \
                   self.lineEdit_surname.text() + "|" + \
                   self.lineEdit_name.text() + \
                   "|" + start_time.strftime("%H:%M:%S") + \
                   " - " + \
                   final_time.strftime("%H:%M:%S") + "|\n")
        # lstTime.append(final_time-Time())
        file.close()
        self.close() #закрытие окна сведений об экзаменуемом
        self.lineEdit_surname.setText("")
        self.lineEdit_name.setText("")
        #self.create_win_info_exam_table.info_exam()



# Класс для вывода таблицы со сведениями об экзаменуемых
class win_InfoExamTable(QtWidgets.QMainWindow):
    def __init__(self, window):
        QtWidgets.QMainWindow.__init__(self)
        #self.setupUi(self)
        self.window = window
        # Пока дочернее окно открыто запретить переход на главное
        #self.setWindowModality(QtCore.Qt.ApplicationModal)

    # Метод внесения информации об экзаменуемом и начала отсчета времени
    def info_exam(self):
        print("info_exam")
        file_read = open("files\\InfoStud\\" + data + \
                         "_tikets.txt", "r", encoding="utf-8")
        #file_read = open(r"files\InfoStud\2020-07-25_18.08.28_tikets.txt", "r", encoding="utf-8")
        dataInfoExam = file_read.readlines()
        if dataInfoExam != []:
            lst_info_exam = []
            for i in range(0, len(dataInfoExam)):
                lst_line_info_exam = dataInfoExam[i].split("|")
                lst_info_exam.append(lst_line_info_exam)
                print(lst_line_info_exam)
            print("Список с данными:", lst_info_exam)
            # print("данные из файла:", lst_line_info_exam)

            # Добавление в список ID
            for i in range(0,len(lst_info_exam)):
                if i + 1 < 10:
                    str_ID = "0" + str(i+1)
                    lst_info_exam[i].insert(0, str_ID)
                else:
                    lst_info_exam[i].insert(0, str(i+1))


            # Оставшееся время, номер попытки
            # Формирование списков с временем начала и окончания
            print(final_time-Time())
            """ lst_full_time = []
            for i in range(0, len(lst_info_exam)):
                lst_full_time.append(lst_info_exam[i][4].split("-"))
            print("после изменений:", lst_info_exam)
            print(lst_full_time)"""
            # Формирование из списка lst_full_time, списка с [ЧЧ,МС,СС]
            '''for i in range(0, len(lst_info_exam)):
                time_left = lst_info_exam[4].split("-")
            lst_info_exam[i].insert(0, str_ID)'''

            central_widget = QtWidgets.QWidget(self)
            self.setCentralWidget(central_widget)
            self.setWindowTitle("Сведения об экзаменуемых")

            self.left = 20
            self.top = 70
            self.width = 700
            self.height = 200
            self.setGeometry(self.left, self.top, self.width, self.height)

            font = QtGui.QFont()
            font.setFamily("Bahnschrift SemiLight SemiConde")
            font.setPointSize(11)

            grid_layout = QtWidgets.QGridLayout()
            central_widget.setLayout(grid_layout)

            table_info_exam = QtWidgets.QTableWidget(self)  # Создаём таблицу
            table_info_exam.setColumnCount(5)  # Устанавливаем 5 столбцов
            table_info_exam.setRowCount(len(lst_info_exam))  #  строки
            table_info_exam.setFont(font)

            # Устанавливаем заголовки таблицы
            table_info_exam.setHorizontalHeaderLabels(["ID", "Номер билета",
                                         "Фамилия", "Имя",
                                         "Начало - окончание экзамена"])
            # Устанавливаем выравнивание на заголовки
            for i in range(0, 5):
                table_info_exam.horizontalHeaderItem(i).setTextAlignment(QtCore.Qt.AlignHCenter)

            # item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            '''t = QtWidgets.QTableWidgetItem("001")
            table_info_exam.setItem(0, 0, t)
            t.setTextAlignment(QtCore.Qt.AlignCenter)'''

            """table_info_exam.setItem(0, 1, QtWidgets.QTableWidgetItem("Билет №3"))
        table_info_exam.setItem(0, 2, QtWidgets.QTableWidgetItem("Иванов"))
        table_info_exam.setItem(0, 3, QtWidgets.QTableWidgetItem("Андрей"))
        table_info_exam.setItem(0, 4, QtWidgets.QTableWidgetItem("13:40:20-14:00:00"))

        table_info_exam.setItem(0, 5, QtWidgets.QTableWidgetItem("5 мин."))
        table_info_exam.item(0, 5).setBackground(QtGui.QColor("#ff6464"))

        '''btn = QPushButton("1")
                table.setCellWidget(0, 6, btn)'''
        combo = QtWidgets.QComboBox()
        combo.setFixedWidth(30)
        for t in range(1, 4):
            combo.addItem(str(t))
        table_info_exam.setCellWidget(0, 6, combo)"""

            for i in range(0, len(lst_info_exam)):
                for j in range(0, 5):
                    cell = QtWidgets.QTableWidgetItem(lst_info_exam[i][j])
                    print(i,j,lst_info_exam[i][j])
                    table_info_exam.setItem(i, j, cell)
                    cell.setTextAlignment(QtCore.Qt.AlignCenter)
                    cell.setFlags(QtCore.Qt.ItemIsEnabled)

            """# заполняем вторую строку
        table_info_exam.setItem(1, 0, QtWidgets.QTableWidgetItem("002"))
        table_info_exam.setItem(1, 1, QtWidgets.QTableWidgetItem("Билет №20"))
        table_info_exam.setItem(1, 2, QtWidgets.QTableWidgetItem("Петров"))"""

            # делаем ресайз колонок по содержимому
            table_info_exam.resizeColumnsToContents()

            grid_layout.addWidget(table_info_exam, 0, 0)

            file_read.close()



def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QtWidgets.QMessageBox.critical(None, 'Error', text)
    quit()


import sys
sys.excepthook = log_uncaught_exceptions
app = QtWidgets.QApplication(sys.argv)



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

