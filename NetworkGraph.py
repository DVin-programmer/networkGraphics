# coding: utf8
'''
Программа для построения сетевых графиков
-----------------------------------------
Автор: Винокурова Д.В.
'''
from tkinter import Tk, ttk, Label, Button, Entry, Canvas, StringVar,\
     messagebox, RIGHT, LEFT, TOP, BOTTOM, CENTER,\
     E,W,S,N, Menu, Toplevel, Scrollbar, X, Y, Frame,\
     SUNKEN, GROOVE, RIDGE, SUNKEN, RAISED, FLAT, HORIZONTAL, font, Text, WORD
from PIL import ImageTk, Image, _imagingtk
from random import randint
from openpyxl import load_workbook, Workbook
from openpyxl.styles import NamedStyle, Font, Side, Border, Alignment
import numpy as  np, os, sys, networkx as nx, \
       requests as rq, subprocess as sb, webbrowser as wb

def httpText(strF):
    strF = strF.replace("\\","%5C")
    strF = strF.replace("{","%7B")
    strF = strF.replace("}","%7D")
    strF = strF.replace(" ","%20")
    strF = strF.replace("^","%5E")
    strF = strF.replace("\n","%0A")
    strF = strF.replace("&","%26")
    
    strHTTP1 = "https://math.now.sh?from="
    strHTTP = strHTTP1 + strF + ".png"
    return strHTTP

#Генератор цвета
def colorGenerate():
    r1 = randint(43,240)
    g1 = randint(72,240)
    b1 = randint(70,240)
    resRGB = "#"+str(hex(r1)[2:])+str(hex(g1)[2:])+str(hex(b1)[2:])
    return resRGB

#Удаление старой информации и добавление новой
#Удаление старой информации и добавление новой
def clearInfoCombobox(event):
    if lstSave != []:
        lenSave = len(lstSave)
        lstEl = lstSave.pop()
        
    try:
        cnvTable.delete("all")
        button_Next.destroy()
        if flagWO == True:
            winWorkOrder.destroy()    
        print("try")
    except NameError:
        print("except")
        inputText()
    else:
        print("else")
        for i in range(0,lstEl):
            globals()['text_NumJ'+str(i)].destroy()
            globals()['DecsrJRow'+str(i)].destroy()
            globals()['TimeJRow'+str(i)].destroy()
        inputText()

'''
#Удаление старой информации и добавление новой
def clearInfoCombobox(event):
    if lstSave != []:
        lenSave = len(lstSave)
        lstEl = lstSave.pop()
    try:
        cnvTable.delete("all")
        button_Next.destroy()
        winWorkOrder.destroy()
        print("try")
    except NameError:
        print("except")
        inputText()
    else:
        print("else")
        for i in range(0,lstEl):
            globals()['text_NumJ'+str(i)].destroy()
            globals()['DecsrJRow'+str(i)].destroy()
            globals()['TimeJRow'+str(i)].destroy()
        inputText()
'''

#Ввод данных
def inputText():
    global cnvTable, button_Next
    NumJobsStr = combobox_NumJobs.get()
    NumJobsInt = int(NumJobsStr)
    lstSave.append(NumJobsInt)

    #Создание холста для таблицы
    height_yI = 127 + (NumJobsInt-3)*26
    cnvTable = Canvas(win, width = 478, height = height_yI)
    cnvTable.create_rectangle(10, 5, 478, height_yI,
                               outline = "#b7b7bb",
                               fill = "#FFFFFF")

    #Горизонтальные линии в таблице
    cnvTable.create_line(10, 5, 478, 5, width = 1)
    cnvTable.create_line(10, 50, 478, 50, width = 1)
    cnvTable.create_line(10, height_yI, 478, height_yI, width = 1)
    
    #Вертикальные линии в таблице
    cnvTable.create_line(10, 5, 10, height_yI, width = 1)
    cnvTable.create_line(80, 5, 80, height_yI, width = 1)
    cnvTable.create_line(360, 5, 360, height_yI, width = 1)
    cnvTable.create_line(478, 5, 478, height_yI, width = 1)

    #-------------------------------------------------
    cnvTable.create_text(20, 10, text = "Номер\nработы",
                         font = ('Calibri',12), anchor = "nw",
                         justify = CENTER)
    cnvTable.create_text(150, 20, text = "Описание работы",
                         font = ('Calibri',12), anchor = "nw",
                         justify = CENTER)
    cnvTable.create_text(370, 10, text = "Длительность\n(в днях)",
                         font = ('Calibri',12), anchor = "nw",
                         justify = CENTER)

    #Заполнение столбца "Номер работы"
    for i in range(0,NumJobsInt):
        yI = 124 + i*26
        globals()['text_NumJ'+str(i)] = Label(win, text = str(i+1),
                                              bg = "#ffffff",
                                              anchor = E,
                                              width = 4)
        globals()['text_NumJ'+str(i)].place(x = 20,y = yI)

    #Горизонтальные линии в таблице
    for i in range(0,NumJobsInt - 1):
        hrz_yI = 75 + i*26
        cnvTable.create_line(10, hrz_yI, 478, hrz_yI, width = 1)  

    #Заполнение столбцов "Описание работы" и "Длительность"
    for i in range(0,NumJobsInt):
        #Поля ввода для столбца "Описание работы"
        globals()['DecsrJRow'+str(i)] = Entry(win, width = 45,
                                          bg = '#ffffff', relief = FLAT)
        yI = 123 + i*26
        globals()['DecsrJRow'+str(i)].place(x = 90, y = yI)
        #--------------------------------------------------
        #Поля ввода для столбца "Длительность"
        globals()['TimeJRow'+str(i)] = Entry(win, width = 17,
                                             bg = "#e6e6e6", relief = FLAT,
                                             justify = CENTER)
        globals()['TimeJRow'+str(i)].place(x = 370, y = yI)
    #------------------------------------------------------      
    cnvTable.place(x = 5, y = 70)
    #------------------------------------------------------------
    button_Next = Button(win, text = 'Далее',command = checkTable,
                             bg = '#1d8bfc', width = 10)
    button_Next.place(x = 400, y = yI + 40)
    
#Проверка полей ввода на корректность          
def checkTable():
    flagError1 = False
    flagError2 = False
    NumJobsStr = combobox_NumJobs.get()
    NumJobsInt = int(NumJobsStr)
    for i in range(0,NumJobsInt):
        try:
            if globals()['DecsrJRow'+str(i)].get() == "":
                globals()['DecsrJRow'+str(i)].config(bg = "#f9555d")
                flagError1 = True
            else:
                globals()['DecsrJRow'+str(i)].config(bg = "#ffffff")
            if globals()['TimeJRow'+str(i)].get() == "" or\
               not(globals()['TimeJRow'+str(i)].get().isdigit()) or\
               int(globals()['TimeJRow'+str(i)].get()) == 0:
                globals()['TimeJRow'+str(i)].config(bg = "#f9555d")
                flagError2 = True
            else:
                globals()['TimeJRow'+str(i)].config(bg = "#ffffff")
        except ValueError:
                globals()['TimeJRow'+str(i)].config(bg = "#f9555d")
                flagError2 = True

    if flagError1 == False and flagError2 == False:
        #Считывание данных из столбцов "Описание работы" и "Длительность"
        global lstWorkDay, lstWorkDescr 
        lstWorkDay, lstWorkDescr = [], []
        for i in range(0,NumJobsInt):
            lstWorkDay.append(int(globals()['TimeJRow'+str(i)].get()))
            lstWorkDescr.append(str(globals()['DecsrJRow'+str(i)].get()))
        #print(lstWorkDay,lstWorkDescr)

        WorkOrder(NumJobsInt)
        

#Окно "Порядок выполнения работ"        
def WorkOrder(NumJobsInt):
    globals()["flagWO"] = True
    global winWorkOrder, MtrBtn
    MtrBtn = np.zeros((NumJobsInt - 1,NumJobsInt - 1), dtype = np.int32)
    button_Next["state"] = "disabled"
    
    winWorkOrder = Toplevel()
    winWorkOrder.title("Порядок работ")
    winWorkOrder.iconbitmap("files\\NetDiag.ico")
    winWOHeight = 123 + 26*(NumJobsInt - 1)
    winWorkOrder.geometry("500x"+str(winWOHeight))
    winRight(winWorkOrder)
    #-----------------------------
    middleWin = int(500/NumJobsInt)
    #------------------------------------------------------
    cnvWin = Canvas(winWorkOrder, width = 485, height = 200)
    cnvWin.create_rectangle(4, 5, 485, 50,
                            outline = "#0158ba",
                            fill = "#cbe0f7")
    cnvWin.place(x = 5, y = 5)
    #-----------------------------------------------
    text_TextB = "Укажите порядок выполнения работ:"
    label_TextB = Label(winWorkOrder,
                        text = text_TextB,
                        bg = "#cbe0f7")
    label_TextB.config(font = ('Calibri',12))
    label_TextB.place(x = 20, y = 20)
    #-------------------------------
    global dictBtn, dictBtnCol, dictBtnRow, sumE, lstBtn, lstBtnCol, lstBtnRow
    dictBtn, dictBtnCol, dictBtnRow = {}, {}, {}
    lstBtn, lstBtnCol, lstBtnRow = [], [], []
    sumE = 1
    #Создание кнопок для выбора очередности работ
    for i in range(0,NumJobsInt - 1):   
        for j in range(1,NumJobsInt):
            xJ = middleWin + (j - 1)*35 + 20
            if i < j:
                yI = 70 + i*24
                #Кнопки
                globals()['btnWorkOrder'+str(i)+"_"+str(j)] = \
                    Button(winWorkOrder,
                           text = str(i+1)+"⇾"+str(j+1),
                           #command = checkTable,
                           bg = "#9e9e9e",
                           width = 4,
                           relief = RIDGE,
                           activebackground = "#21e51c")
                globals()['btnWorkOrder'+str(i)+\
                          "_"+str(j)].place(x = xJ, y = yI)
                #------------------------------------------
                #Для того, чтобы обращаться по имени
                if sumE == 1:
                    dictBtn["button"] = str(i+1)+"_"+str(j+1)
                    dictBtnCol["button"] = str(j+1)
                    dictBtnRow["button"] = str(i+1)
                else:
                    dictBtn["button"+str(sumE)] = str(i+1)+"_"+str(j+1)
                    dictBtnCol["button"+str(sumE)] = str(j+1)
                    dictBtnRow["button"+str(sumE)] = str(i+1)
                sumE += 1
    #print(dictBtn)
    #----------------------------------------
    #Вызов функции для изменения цвета кнопок    
    for i in range(0,NumJobsInt - 1):
        for j in range(1,NumJobsInt):
            if i < j:
                globals()['btnWorkOrder'+str(i)+"_"+str(j)].bind("<Button-1>",
                                                                 btnOnOff)
    #--------------------------------------------------------------------
    winWorkOrder.protocol("WM_DELETE_WINDOW", DelWinWO)
    #------------------------------------------------------------
    button_Next2 = Button(winWorkOrder,
                          text = 'Далее',
                          command = checkButton,
                          bg = '#1d8bfc', width = 10)
    button_Next2.place(x = xJ - 40, y = yI + 40)
      
    
#Изменение цвета кнопок    
def btnOnOff(event):
    btnWid  = event.widget
    btnWidF = str(btnWid).find("b")
    btnWidCut = str(btnWid)[btnWidF:]
    print("=======lst:",lstBtn,lstBtnRow, lstBtnCol)
    if btnWid["bg"] == "#9e9e9e":
        btnWid["bg"] = "#21e51c"
        if not(dictBtn[str(btnWidCut)] in lstBtn):
            lstBtn.append(dictBtn[str(btnWidCut)])
            lstBtnCol.append(dictBtnCol[str(btnWidCut)])
            lstBtnRow.append(dictBtnRow[str(btnWidCut)])
            #print(lstBtn)
    else:
        btnWid["bg"] = "#9e9e9e"
        if dictBtn[str(btnWidCut)] in lstBtn:
            lstBtn.remove(dictBtn[str(btnWidCut)])
            lstBtnCol.remove(dictBtnCol[str(btnWidCut)])
            lstBtnRow.remove(dictBtnRow[str(btnWidCut)])
            #print(lstBtn)
#-----------------------------    
#Удаляет окно с порядком работ
#Разблокировка кнопки "Далее" на главном окне
def DelWinWO():
    winWorkOrder.destroy()
    button_Next["state"] = "normal"
    flagWO = False

#------------------------------------
#Проверка правильности нажатых кнопок
def checkButton():
    #print(len(set(lstBtnCol)),set(lstBtnCol))
    NumJobsStr = combobox_NumJobs.get()
    NumJobsInt = int(NumJobsStr)
    if len(set(lstBtnCol)) == NumJobsInt - 1 and\
       len(set(lstBtnRow)) == NumJobsInt - 1:
        #print("Все хорошо")
        chartCreation(lstBtn)
    else:
        messagebox.showwarning("Предупреждение",
                               "У каждой работы должна быть предшествующая!")
        #print("У каждой работы должна быть предшествующая")

#Создание сетевого графика (расчет характеристик вершин)
def chartCreation(lstBtn):
    NumJobsStr = combobox_NumJobs.get()
    NumJobsInt = int(NumJobsStr)
    #------------------------------------------------------------
    global dictInVtx, dictVtxValue, dictInVtxRev, dictVtxValueRev
    dictInVtx, dictVtxValue, dictInVtxRev, dictVtxValueRev = {}, {}, {}, {}
    dictVtxValue.update({1:[0,lstWorkDay[0],lstWorkDay[0],
                            lstWorkDescr[0]]})
    #-----------------------------------------
    #print(lstBtn)
    global lstBtnSort
    lstBtnSort = sorted(lstBtn, key = lambda last: last[2])
    #print(lstBtnSort)
    #--------------------------------------------------
    #Нахождение вершин которые ведут к текущей
    for l in range(0,len(lstBtnSort)):
        #Значение по ключу(номеру вершины)
        lstBtnSort2 = lstBtnSort[l].split('_')
        lstGet_dictInVtx = dictInVtx.get(int(lstBtnSort2[1]))
        print("lstGet_dictInVtx:",lstGet_dictInVtx)
        if lstGet_dictInVtx != None:
            dictInVtx.update({int(lstBtnSort2[1]):lstGet_dictInVtx+\
                              [int(lstBtnSort2[0])]})
        else:
            dictInVtx.update({int(lstBtnSort2[1]):[int(lstBtnSort2[0])]})
    print("dictInVtx:",dictInVtx)

    #-----------------
    #Заполнение вершин
    for t in range(2,NumJobsInt+1):
        lstES = [] 
        #print(t,len(dictInVtx[t]))
        
        #Если в вершину входит два пути
        if len(dictInVtx[t]) > 1:
            for t2 in range(0,len(dictInVtx[t])):
                '''print(dictInVtx[t],dictInVtx[t][t2],
                      dictVtxValue[dictInVtx[t][t2]][2])'''
                ES = dictVtxValue[dictInVtx[t][t2]][2]
                lstES.append(ES)
                dictVtxValue.update({t:[max(lstES),
                                        lstWorkDay[t-1],
                                        max(lstES) + lstWorkDay[t-1],
                                        lstWorkDescr[t-1]]})
            #print("Раннее окончание:",lstES)
        else:
            ES = dictVtxValue[dictInVtx[t][0]][2]
            dictVtxValue.update({t:[ES,
                                    lstWorkDay[t-1],
                                    ES + lstWorkDay[t-1],
                                    lstWorkDescr[t-1]]})
    print("dictVtxValue:",dictVtxValue)
    print("lstES:", lstES)
    #--------------------------------------------------
    #Нахождение вершин, пути от которых ведут к текущей (обратный проход)
    lstBtnSortRev = sorted(lstBtn)
    for l in range(0,len(lstBtnSortRev)):
        #Значение по ключу(номеру вершины)
        lstBtnSort2Rev = lstBtnSortRev[l].split('_')
        lstGet_dictInVtxRev = dictInVtxRev.get(int(lstBtnSort2Rev[0]))
        if lstGet_dictInVtxRev != None:
            dictInVtxRev.update({int(lstBtnSort2Rev[0]):lstGet_dictInVtxRev+\
                              [int(lstBtnSort2Rev[1])]})
        else:
            dictInVtxRev.update({int(lstBtnSort2Rev[0]):
                                 [int(lstBtnSort2Rev[1])]})
    print("dictInVtxRev:",dictInVtxRev)
    #--------------------------------------------
    #Заполнение вершин (проход в обратную сторону)
    dictVtxValueRev.update({NumJobsInt:[dictVtxValue[NumJobsInt][0],0,
                                        dictVtxValue[NumJobsInt][2]]})
    
    t = NumJobsInt - 1
    while t != 0:
        lstLF = []
        #print(t,len(dictInVtxRev[t])) 
        #Если в вершину входит два пути
        if len(dictInVtxRev[t]) > 1:
            for t2 in range(0,len(dictInVtxRev[t])):
                '''print(t,dictInVtxRev[t], dictInVtxRev[t][t2],
                      dictVtxValueRev[dictInVtxRev[t][t2]])'''
                LF = dictVtxValueRev[dictInVtxRev[t][t2]][0]
                ES = dictVtxValue[t][0]
                T = dictVtxValue[t][1]
                lstLF.append(LF)
                LS = min(lstLF) - T
                dictVtxValueRev.update({t:[min(lstLF) - T, LS - ES,
                                           min(lstLF)]})
            #print("Позднее начало:",lstLF)
        else:
            LF = dictVtxValueRev[dictInVtxRev[t][0]][0]
            ES = dictVtxValue[t][0]
            T = dictVtxValue[t][1]
            LS = LF - T
            #print(ES,LS, T,t)
            dictVtxValueRev.update({t:[LF - T, LS - ES, LF]})
        t -= 1
    print("dictVtxValueRev:",dictVtxValueRev)
    NetworkGraphViz()

#------------------------------------------------
#Построение сетевого графика, вычисление резервов
def NetworkGraphViz():
    NumJobsStr = combobox_NumJobs.get()
    NumJobsInt = int(NumJobsStr)
    #--------------------------------------------------------------
    os.environ["PATH"] += os.pathsep + "files\\Graphviz2.34\\bin\\"
    file = open("files\\NetworkGraph.gv","w",encoding = "utf-8")
    file.write('''\
digraph NetworkGraph
{
   //graph [charset = "utf8"]
   rankdir = LR
   layout = dot
   splines = spline
   node [style = "filled, bold", fillcolor = "#f2f4f7", fontname = "Arial"]
   edge [penwidth = 2]
''')

    #Объединение значений прямого и обратного проходов
    global dictVtxValueAll
    dictVtxValueAll = {}
    for i in range(1,NumJobsInt + 1):
        dictVtxValueAll.update({i:dictVtxValue[i] + dictVtxValueRev[i]})
    print("dictVtxValueAll:",dictVtxValueAll)
    #---------------------
    lstColor = []                                                           
    for i in range(1,NumJobsInt + 1):
        lstColor.append(colorGenerate())
    #print(lstColor)

    #Перенос слов в вершинах
    for i in range(1,NumJobsInt + 1):
        if len(dictVtxValueAll[i][3]) > 15:
            lstStr = dictVtxValueAll[i][3].split(' ')
            strJoin = lstStr[0]
            for t in range(1, len(lstStr)):
                if len(lstStr[t-1]+lstStr[t]) > 10:
                    strJoin += "\\n "+lstStr[t] + " "
                    
                else:
                    strJoin += " " + lstStr[t] + " "
            dictVtxValueAll.update({i:[dictVtxValue[i][0]] +\
                                        [dictVtxValue[i][1]]+\
                                        [dictVtxValue[i][2]]+\
                                        [strJoin] +\
                                        dictVtxValueRev[i]})
    #print("После изменений (слова с переносом):",dictVtxValueAll)
      
    #Запись вершин в файл
    for i in range(1,NumJobsInt + 1):
        file.write(u"   v" + str(i) + " [fontname = \"Arial\","+\
                   "color = \""+str(lstColor[i-1]) +\
                   "\", shape = record, label = \"{ " +\
                   str(dictVtxValueAll[i][0]) + " | " +\
                   str(dictVtxValueAll[i][1]) + " | " +\
                   str(dictVtxValueAll[i][2]) + " } | " + " <mI"+str(i)+"> "+\
                   str(i) + ". "+ str(dictVtxValueAll[i][3]) + " | {" +\
                   str(dictVtxValueAll[i][4]) + " | " +\
                   str(dictVtxValueAll[i][5]) + " | " +\
                   str(dictVtxValueAll[i][6]) + " }\"]\n")
    #-----------------------------------------------------    
    #Список связей вершин
    lstLinkVtx = []
    for l in range(0,len(lstBtnSort)):
        #Значение по ключу(номеру вершины)
        lstLinkVtx.append(lstBtnSort[l].split('_'))
    #print("lstLinkVtx:",lstLinkVtx)

    #Преобразование списка списков в кортеж
    lstTpl_LinkVtx = []
    for t in range(0,len(lstBtnSort)):
        lstTpl_LinkVtx.append((int(lstLinkVtx[t][0]),
                               int(lstLinkVtx[t][1])))
    print(lstTpl_LinkVtx)


    #---------------------------------------------
    #Нахождение всех путей для вычисления резервов
    G = nx.Graph()
    G.add_edges_from(lstTpl_LinkVtx)
    Reserves = list(nx.all_simple_paths(G, source = 1, target = NumJobsInt))
    #print("Reserves:",Reserves)

    #Создание индексов для последующего удаления
    lstIndexDel = []
    for t in range(0,len(Reserves)):
        if Reserves[t] != sorted(Reserves[t]):
            lstIndexDel.append(t)
    #print("lstIndexDel:",lstIndexDel)
    
    #Создание нового списка с необходимыми путями
    ReservesNew = []
    for t in range(0,len(Reserves)):
        if not(t in lstIndexDel):
            ReservesNew.append(Reserves[t])
    #print("Пути:",ReservesNew, "\nКоличество путей:", len(ReservesNew))
    #------------------------------------------------------------------
    #Вычисление резервов
    # sLst - список со значениями для сложения резервов
    strValueLst1 = []
    intValueLst1 = []
    for i in range(0,len(ReservesNew)):
        strValueLst2 = []
        intValueLst2 = []
        for l in range(0,len(ReservesNew[i])):
            k = ReservesNew[i][l]
            strValueLst2.append(str(dictVtxValueAll[k][1]))
            intValueLst2.append(dictVtxValueAll[k][1])
        strValueLst1.append(strValueLst2)
        intValueLst1.append(intValueLst2)
    #print("strValueLst1:",strValueLst1)

    '''#Вывод на экран подробного решения
    s = str(dictVtxValueAll[NumJobsInt][6])
    plus = " + "
    arrow = "➜"
    #Преобразование путей в str
    ReservesNewStr1 = []
    for i in range(0,len(ReservesNew)):
        ReservesNewStr2 = []
        for l in range(0,len(ReservesNew[i])):
            ReservesNewStr2.append(str(ReservesNew[i][l]))
        ReservesNewStr1.append(ReservesNewStr2)
    #print("ReservesNewStr1:",ReservesNewStr1)
    #Подробное решение, критический путь
    fileReserves = open("files\\ВычислениеРезервов.txt","w",encoding = "utf-8")
    for i in range(0, len(strValueLst1)):
        sPlus = plus.join(strValueLst1[i])
        sumEl = sum(intValueLst1[i])
        ReservesStr = arrow.join(ReservesNewStr1[i])
        #---------------------------------------
        str1 = "Путь " + str(ReservesStr) + ": \n"
        strSpace = ""
        for space in range(0,len(str1)):
            strSpace += " "
        #---------------------------------------------------
        str2 = strSpace + s + " - " + "(" + sPlus + ") = " +\
               s + " - " + str(sumEl) + " = " +\
               str(int(s) - sumEl)+"\n" 
        strDashes = ""
        for space in range(0,len(str2)-1):
            strDashes += "-"
        fileReserves.write(str1 + str2 + strDashes + "\n" )

        if int(s) - sumEl == 0:
            criticalPath = i

    fileReserves.write("Критический путь: " + \
          str(arrow.join(ReservesNewStr1[criticalPath])))
    fileReserves.close() '''      


    
    #----------------------
    # Запись вершин в файл
    for i in range(0,len(lstBtnSort)):
        file.write("   v" + lstLinkVtx[i][0] + ":<mI"+str(lstLinkVtx[i][0])+\
                   "> -> v" + lstLinkVtx[i][1]+":<mI"+str(lstLinkVtx[i][1])+\
                   "> [color = \"" + str(lstColor[int(lstLinkVtx[i][0])-1])+\
                   "\"]\n")
    '''file.write("v"+str((arrow+"v").join(ReservesNewStr1[criticalPath]))+\
               " [color = \"#FF0000\", penwidth = 3]")'''
    #print(ReservesNewStr1[criticalPath])
    file.write("\n}")
    file.close()
    os.system(r"startGV.bat files\\NetworkGraph.gv")
    #sb.call(["notepad.exe","ВычислениеРезервов.txt"])
    #os.system("start notepad.exe "+"files\\ВычислениеРезервов.txt")


    #========================================================================
    #Построение промежуточных сетевых графиков (схема с названием работ
    #без параметров)
    fileGV01 = open("files\\NetworkGraph01.gv","w",encoding = "utf-8")
    fileGV01.write('''\
digraph NetworkGraph01
{
   //graph [charset = "utf8"]
   rankdir = LR
   layout = dot
   splines = spline
   node [style = "filled, bold", fillcolor = "#f2f4f7", fontname = "Arial"]
   edge [penwidth = 2]
''')
    #--------------------
    #Запись вершин в файл
    for i in range(1,NumJobsInt + 1):
        fileGV01.write(u"   v" + str(i) + " [fontname = \"Arial\","+\
                   "color = \""+str(lstColor[i-1]) +\
                   "\", shape = record, label = \"{ " +\
                   "" + " | " +\
                   "" + " | " +\
                   "" + " } | " + " <mI"+str(i)+"> "+\
                   str(i) + ". "+ str(dictVtxValueAll[i][3]) + " | {" +\
                   "" + " | " +\
                   "" + " | " +\
                   "" + " }\"]\n")
    # Запись вершин в файл
    for i in range(0,len(lstBtnSort)):
        fileGV01.write("   v" + lstLinkVtx[i][0] + ":<mI"+str(lstLinkVtx[i][0])+\
                   "> -> v" + lstLinkVtx[i][1]+":<mI"+str(lstLinkVtx[i][1])+\
                   "> [color = \"" + str(lstColor[int(lstLinkVtx[i][0])-1])+\
                   "\"]\n")
    '''file.write("v"+str((arrow+"v").join(ReservesNewStr1[criticalPath]))+\
               " [color = \"#FF0000\", penwidth = 3]")'''
    #print(ReservesNewStr1[criticalPath])
    fileGV01.write("\n}")
    fileGV01.close()
    os.system(r"startGV.bat files\\NetworkGraph01.gv")

    #========================================================================
    #Построение промежуточных сетевых графиков (схема с ранним началом и
    #окончанием работ)
    fileGV02 = open("files\\NetworkGraph02.gv","w",encoding = "utf-8")
    fileGV02.write('''\
digraph NetworkGraph02
{
   //graph [charset = "utf8"]
   rankdir = LR
   layout = dot
   splines = spline
   node [style = "filled, bold", fillcolor = "#f2f4f7", fontname = "Arial"]
   edge [penwidth = 2]
''')
    #--------------------
    #Запись вершин в файл
    for i in range(1,NumJobsInt + 1):
        fileGV02.write(u"   v" + str(i) + " [fontname = \"Arial\","+\
                   "color = \""+str(lstColor[i-1]) +\
                   "\", shape = record, label = \"{ " +\
                   str(dictVtxValueAll[i][0]) + " | " +\
                   str(dictVtxValueAll[i][1]) + " | " +\
                   str(dictVtxValueAll[i][2]) + " } | " +\
                   " <mI"+str(i)+"> "+\
                   str(i) + ". "+ str(dictVtxValueAll[i][3]) + " | {" +\
                   "" + " | " +\
                   "" + " | " +\
                   "" + " }\"]\n")
    # Запись вершин в файл
    for i in range(0,len(lstBtnSort)):
        fileGV02.write("   v" + lstLinkVtx[i][0] + ":<mI"+str(lstLinkVtx[i][0])+\
                   "> -> v" + lstLinkVtx[i][1]+":<mI"+str(lstLinkVtx[i][1])+\
                   "> [color = \"" + str(lstColor[int(lstLinkVtx[i][0])-1])+\
                   "\"]\n")
    #print(ReservesNewStr1[criticalPath])
    fileGV02.write("\n}")
    fileGV02.close()
    os.system(r"startGV.bat files\\NetworkGraph02.gv")
    

    #=======================================================================
    #Запись в файл html
    if NumJobsInt < 7:
        wImg = "70%"
    elif NumJobsInt == 7:
        wImg = "70%"
    else:
        wImg = "95%"
        
    fileHTML = open("files\\Info.html","w",encoding = "utf-8")
    fileHTML.write('''<!DOCTYPE html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <title>Сетевой график</title>
	<link rel = "stylesheet" href = "Output.css">
	<link rel = "shorctcut icon" href = "NetDiag.ico">
  </head>
  <body>
    
	<div class = "text-content">
	 <h1 class = "align-center">Построение сетевого графика</h1>
	 <p><b>Сетевой график</b> – это ориентированный граф, где в вершинах 
	 располагаются выполняемые работы, дугами – изображается связь между ними.  
	 Каждая вершина содержит несколько параметров, используя необходимые 
	 формулы можно рассчитать значения в каждой ячейке (рис. 1, формулы (1-5))</p>
	 
	 <br />
	 <table cellspacing = "0" cellpadding = "3" width = "50%" align = "center" class = "imgTable">
	   <tr align = "center">
	     <td><img src="https://math.now.sh?from=T%5E%7B%D0%A0%D0%9D%7D_i" /></td>
		 <td><img src="https://math.now.sh?from=T_i" /></td>
		 <td><img src="https://math.now.sh?from=T%5E%7B%D0%A0%D0%9E%7D_i" /></td>
	   </tr> 
	   <tr align = "center">
	     <td colspan = "3"><Номер работы>.<Название задачи></td>
	   </tr>
	   <tr align = "center">
	     <td><img src="https://math.now.sh?from=T%5E%7B%D0%9F%D0%9D%7D_i" /></td>
		 <td><img src="https://math.now.sh?from=R_i" /></td>
		 <td><img src="https://math.now.sh?from=T%5E%7B%D0%9F%D0%9E%7D_i" /></td>
	   </tr>
	 </table>
	 <p class = "smallText"> Рис. 1. Вершина сетевого графика с параметрами </p>
	 
	 <!-- Формулы под картинкой с параметрами -->
	 <p class = "align-center">
	   <img src="https://math.now.sh?from=T%5E%7B%D0%A0%D0%9D%7D_i%20%3D%20max%28T%5E%7B%D0%A0%D0%9E%7D_%7Bk%7D%29" />
	   <img src="https://math.now.sh?from=%281%29" style = "padding: 0 3px 3px 10px" />
	 
	   <img style = "padding: 0 0 0 80px"
	   src="https://math.now.sh?from=T%5E%7B%D0%9F%D0%9D%7D_i%20%3D%20T%5E%7B%D0%9F%D0%9E%7D_i%20-%20T_i" />
	   <img src="https://math.now.sh?from=%283%29" style = "padding: 0 3px 3px 20px" />
	   
	   <br />
	   <img style = "padding: 0 0 0 20px"
	   src="https://math.now.sh?from=T%5E%7B%D0%A0%D0%9E%7D_i%20%3D%20T%5E%7B%D0%A0%D0%9D%7D_i%20%2B%20T_i" />
	   <img src="https://math.now.sh?from=%282%29" style = "padding: 0 3px 3px 20px" />
	   <img style = "padding: 0 0 0 80px"
	   src="https://math.now.sh?from=T%5E%7B%D0%9F%D0%9E%7D_i%20%3D%20min%28T%5E%7B%D0%9F%D0%9D%7D_%7Bj%7D%29" />
	   <img src="https://math.now.sh?from=%284%29" style = "padding: 0 3px 3px 10px" />
	   
	   <br />
	   <img 
	   src="https://math.now.sh?from=R_i%20%3D%20T%5E%7B%D0%9F%D0%9E%7D_i-T%5E%7B%D0%A0%D0%9E%7D_i%20%3D%20T%5E%7B%D0%9F%D0%9D%7D_i-T%5E%7B%D0%A0%D0%9D%7D_i%20" />
	   <img src="https://math.now.sh?from=%285%29" style = "padding: 0 3px 3px 20px" />
	   <p> где <img style = "padding: 20px 17px 0 8px" src="https://math.now.sh?from=i" /> 
	           - текущая работа <br />
	           <img  class = "textFormulas" src="https://math.now.sh?from=k%5Cin%20%5Cleft%5C%7Bi-1%2Ci-2%2C...%2Ci-N%5Cright%5C%7D" />
	           <br /><img class = "textFormulas" src="https://math.now.sh?from=j%5Cin%20%5Cleft%5C%7Bi%2B1%2Ci%2B2%2C...%2Ci%2BN%5Cright%5C%7D" />
	           <br />
	           <img class = "textFormulas" 
			        src="https://math.now.sh?from=T%5E%7B%D0%0A0%D0%9D%7D_i" />
			   - раннее начало		
			   
			   <br />
			   <img style = "padding: 0px 17px 0 50px"
			        src="https://math.now.sh?from=T_i" />
			   - длительность работы
			   
			   <br />
			   <img class = "textFormulas" 
			        src="https://math.now.sh?from=T%5E%7B%D0%A0%D0%9E%7D_i" />
			   - раннее окончание		
			   
			   <br />
			   <img class = "textFormulas" 
			        src="https://math.now.sh?from=T%5E%7B%D0%9F%D0%9D%7D_i" />
			   - позднее начало
			   
			   <br />
			   <img class = "textFormulas" 
			        src="https://math.now.sh?from=T%5E%7B%D0%9F%D0%9E%7D_i" />
		       - позднее окончание
				
			   <br />
			   <img style = "padding: 0px 17px 0 50px"
			        src="https://math.now.sh?from=R_i" />
			   - временной резерв
			   
	   </p>
	 </p>
	 
     <p> Описание и длительность необходимых работ представлены в таблице 1.</p>
	 <table cellspacing = "0" cellpadding = "3" width = "50%" align = "center">
	   <caption class = "smallText"> Таблица 1. Описание выполняемых работ</caption>
	   <tbody>
	     <tr align = "center" style = "background-color: #3aa9fe; ">
	       <th>Номер <br /> работы </th>
		   <th>Описание работы </th>
		   <th>Длительность <br />(в днях) </th>
	     </tr>
''')
    #Запись таблицы в файл html
    for i in range(0,NumJobsInt):
            fileHTML.write('''	     <tr class = "selectionColor">
	       <td align = "center">'''+str(i+1)+'''.</td>
		   <td>''' + lstWorkDescr[i] + '''</td>
		   <td align = "center">''' + str(lstWorkDay[i]) + '''</td>
	     </tr>''')
    fileHTML.write('''		</tbody>
	  </table>
	  <br />
	  <p> Последовательность выполнения работ, которая была указана в окне
	  ввода программы представлена на схеме (рис. 2). </p>
	  <a href = "NetworkGraph01.svg"><img src = "NetworkGraph01.jpg"
	     width = ''' + wImg + '''
	  title = "Открыть в полном размере" class = "imgSetting"/></a>
	  <p class = "smallText"> Рис. 2. Последовательность необходимых работ </p>
	  
	  <p> Рассчитаем значения параметров <b>раннего начала</b>
	  и <b>раннего окончания</b> работ, используя формулы (1), (2). В первой
	  вершине раннее начало работы будет равно нулю. Все остальные вычисления
	  размещены в блоке ниже и на сетевом графике (рис. 3):</p>
	  <!-- формулы в div с полосой прокрутки -->
	  <div class = "WinFormulas">
	    <p style = "padding: 0">
	      <img src="https://math.now.sh?from=T%5E%7B%D0%A0%D0%9D%7D_1%20%3D%200" />
	    </p>
	    <p style = "padding: 0 0 20px 0">
	      <img src="https://math.now.sh?from=
		  T%5E%7B%D0%A0%D0%9E%7D_1%20%3D
		  %20T%5E%7B%D0%A0%D0%9D%7D_1%20%2B%20T_1
		  %3D%20''' + str(dictVtxValueAll[1][0]) +\
                   '''%20%2B%20''' + str(dictVtxValueAll[1][1]) +\
                   '''%20%3D%20''' +\
                   str(dictVtxValueAll[1][0] + dictVtxValueAll[1][1]) + '''" />
	    </p>''')
    for i in range(2,NumJobsInt + 1):
        fileHTML.write('''

		<p style = "padding: 0">''' +\
		  maxValue_HTML(i)+\
		  '''
	    </p>
	    <p style = "padding: 0 0 20px 0">
	      <img src="https://math.now.sh?from=
		  T%5E%7B%D0%A0%D0%9E%7D_%7B''' + str(i) +\
                    '''%7D%20%3D%20T%5E%7B%D0%A0%D0%9D%7D_%7B''' + str(i) +\
                    '''%7D%20%2B%20T_%7B''' + str(i) +\
                    '''%7D%3D%20''' + str(dictVtxValueAll[i][0]) +\
                   '''%20%2B%20''' + str(dictVtxValueAll[i][1]) +\
                   '''%20%3D%20''' +\
                   str(dictVtxValueAll[i][0] + dictVtxValueAll[i][1]) +\
                   '''" />
	    </p>''')


    fileHTML.write('''
	  </div>

	  <a href = "NetworkGraph02.svg"><img src = "NetworkGraph02.jpg"
	     width = "''' + wImg + '''"
	  title = "Открыть в полном размере" class = "imgSetting"/></a>
	  <p class = "smallText"> Рис. 3. Результаты вычислений
	  раннего начала и окончания работ</p>
	  

	  <p> Следующий этап построения сетевого графика заключается в
	  нахождении <b>позднего окончания</b>, <b>позднего начала</b> и
	  <b>резерва времени</b> проводимых работ. В конечной работе <b>«'''+\
	  str(NumJobsInt) + ". " + lstWorkDescr[NumJobsInt-1]  +\
          '''»</b> значения позднего 
	  начала и окончания работ соответствуют раннему началу и раннему
	  окончанию работ. Все расчеты (рис. 4) проводятся от последней работы в
	  обратном направлении стрелочек по формулам (3), (4), (5):</p>
	  <div class = "WinFormulas">''')
    fileHTML.write('''
	    <p style = "padding: 0">
	      <img src="https://math.now.sh?from=
	      T%5E%7B%D0%9F%D0%9E%7D_%7B''' + str(NumJobsInt) +\
              '''%7D%20%3D%20''' + str(dictVtxValueAll[NumJobsInt][6]) +'''" />
           </p>'''+\
	    '''
            <p style = "padding: 0">
	      <img src="https://math.now.sh?from=
	      T%5E%7B%D0%9F%D0%9D%7D_%7B''' + str(NumJobsInt) +\
              '''%7D%20%3D%20''' + str(dictVtxValueAll[NumJobsInt][4]) +'''" />
            </p>
	    <p style = "padding: 0 0 20px 0">
	      <img src="https://math.now.sh?from=
	      R_%7B''' + str(i) + '''%7D%20%3D%20T%5E%7B%D0%9F%D0%9D%7D_%7B'''+\
              str(NumJobsInt)+'''%7D-T%5E%7B%D0%A0%D0%9D%7D_%7B''' +\
              str(NumJobsInt) +\
              '''%7D%20%3D%20''' + str(dictVtxValueAll[NumJobsInt][4]) +\
              '''%20-%20'''+ str(dictVtxValueAll[NumJobsInt][0]) +\
              '''%20%3D%20''' +\
              str(dictVtxValueAll[NumJobsInt][5]) + '''" />
	    </p>''')
    i = NumJobsInt - 1
    while i != 0:
        fileHTML.write('''

		<p style = "padding: 0">''' +\
		  minValue_HTML(i)+\
	    '''</p>
	    <p style = "padding: 0">
	      <img src="https://math.now.sh?from=
	      T%5E%7B%D0%9F%D0%9D%7D_%7B''' + str(i) +\
              '''%7D%20%3D%20T%5E%7B%D0%9F%D0%9E%7D_%7B'''+\
              str(i)+'''%7D-T_%7B''' + str(i) +\
              '''%7D%20%3D%20''' + str(dictVtxValueAll[i][6]) +\
              '''%20-%20'''+ str(dictVtxValueAll[i][1]) + '''%20%3D%20''' +\
              str(dictVtxValueAll[i][4]) + '''" />
	    </p>
	    <p style = "padding: 0 0 20px 0">
	      <img src="https://math.now.sh?from=
	      R_%7B''' + str(i) + '''%7D%20%3D%20T%5E%7B%D0%9F%D0%9D%7D_%7B'''+\
              str(i)+'''%7D-T%5E%7B%D0%A0%D0%9D%7D_%7B''' + str(i) +\
              '''%7D%20%3D%20''' + str(dictVtxValueAll[i][4]) +\
              '''%20-%20'''+ str(dictVtxValueAll[i][0]) + '''%20%3D%20''' +\
              str(dictVtxValueAll[i][5]) + '''" />
	    </p>''')
        i -= 1
    fileHTML.write('''	
	  </div>
	  <a href = "NetworkGraph.svg"><img src = "NetworkGraph.jpg"
	     width =  "''' + wImg + '''" title = "Открыть в полном размере"
             class = "imgSetting"/></a>
	  <p class = "smallText"> Рис. 4. Результаты построения
	  сетевого графика</p>
	  	  
	  <p>Вычислим резервы времени по каждому из путей:</p>
	  <div class = "WinFormulas">''')
    #-------------------------------------
    #Критический путь, резервы времени
    s = str(dictVtxValueAll[NumJobsInt][6])
    plus = " + "
    arrow = "➜"
    #Преобразование путей в str
    ReservesNewStr1 = []
    for i in range(0,len(ReservesNew)):
        ReservesNewStr2 = []
        for l in range(0,len(ReservesNew[i])):
            ReservesNewStr2.append(str(ReservesNew[i][l]))
        ReservesNewStr1.append(ReservesNewStr2)
        
    for i in range(0, len(strValueLst1)):
        sPlus = plus.join(strValueLst1[i])
        sumEl = sum(intValueLst1[i])
        ReservesStr = arrow.join(ReservesNewStr1[i])
        #---------------------------------------
        str1 = '''
	    <div class = "divIndent"> Путь ''' +\
               '''<div class = "colorPath">''' +\
               str(ReservesStr) + "</div> : \n"
        strSpace = ""
        for space in range(0,len(str1)):
            strSpace += " "
        #---------------------------------------------------
        str2 = strSpace + s + " - " + "(" + sPlus + ") = " +\
               s + " - " + str(sumEl) + " = " +\
               str(int(s) - sumEl)+'''</div>
		<hr> '''
        fileHTML.write(str1 + str2)

        if int(s) - sumEl == 0:
            criticalPath = i

    fileHTML.write('''<div class = "divIndent">Критический путь: <div class = "colorCrPath">''' + \
          str(arrow.join(ReservesNewStr1[criticalPath])))

    fileHTML.write('''</div></div>
	  </div>
   </div>
 </body>
</html>
''')
    fileHTML.close()

#Нахождение max значений раннего начала
def maxValue_HTML(i):
    if len(dictInVtx[i]) > 1:
        htmlReturn = '''
	      <img src="https://math.now.sh?from=
                          T%5E%7B%D0%A0%D0%9D%7D_%7B'''+ str(i) +\
                          '''%7D%20%3D%20max%28'''
        #max(T^{РО}_{i-1})
        for t in range(0,len(dictInVtx[i])):
             htmlReturn += '''T%5E%7B%D0%A0%D0%9E%7D_%7B'''+\
                           str(dictInVtx[i][t])
             if t + 1 < len(dictInVtx[i]):
                  htmlReturn += '''%7D%2C'''
        #max(T^{РО}_{i-1}) = ...
        htmlReturn += '''%7D%29%20%3D%20max%28'''
        for t in range(0,len(dictInVtx[i])):
             htmlReturn += str(dictVtxValueAll[dictInVtx[i][t]][2])
             if t + 1 < len(dictInVtx[i]):
                  htmlReturn += '''%2C'''
        htmlReturn += '''%29%20%3D%20''' +\
                      str(dictVtxValueAll[i][0]) + '''" />'''
    else:
        htmlReturn = '''
	      <img src="https://math.now.sh?from=
                          T%5E%7B%D0%A0%D0%9D%7D_%7B'''+ str(i) +\
                          '''%7D%20%3D%20''' +\
                          str(dictVtxValueAll[i][0]) +'''" />'''
    return htmlReturn
        
#Нахождение значений min позднего начала
def minValue_HTML(i):
    if len(dictInVtxRev[i]) > 1:
        htmlReturn2 = '''
	      <img src="https://math.now.sh?from=
                          T%5E%7B%D0%9F%D0%9E%7D_%7B'''+ str(i) +\
                          '''%7D%20%3D%20min%28'''
        #max(T^{РО}_{i-1})
        for t in range(0,len(dictInVtxRev[i])):
             htmlReturn2 += '''T%5E%7B%D0%9F%D0%9D%7D_%7B'''+\
                           str(dictInVtxRev[i][t])
             if t + 1 < len(dictInVtxRev[i]):
                  htmlReturn2 += '''%7D%2C'''
        #max(T^{РО}_{i-1}) = ...
        htmlReturn2 += '''%7D%29%20%3D%20min%28'''
        for t in range(0,len(dictInVtxRev[i])):
            #Ищем в dictInVtxRev i-ую вершину со значением
             htmlReturn2 += str(dictVtxValueAll[dictInVtxRev[i][t]][4])
             if t + 1 < len(dictInVtxRev[i]):
                  htmlReturn2 += '''%2C'''
        htmlReturn2 += '''%29%20%3D%20''' +\
        str(dictVtxValueAll[i][6]) + '''" />'''
    else:
        htmlReturn2 = '''
	      <img src="https://math.now.sh?from=
                          T%5E%7B%D0%9F%D0%9E%7D_%7B'''+ str(i) +\
                          '''%7D%20%3D%20''' +\
                          str(dictVtxValueAll[i][6]) +'''" />'''
    return htmlReturn2

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
def winCenter(winC):
    winC.update_idletasks()
    width = winC.winfo_width()
    height = winC.winfo_height()
    x = (winC.winfo_screenwidth() // 2) - (width // 2)
    y = (winC.winfo_screenheight() // 2) - (height // 2)
    winC.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def winRight(winR):
    winR.update_idletasks()
    width = winR.winfo_width()
    height = winR.winfo_height()
    x = (winR.winfo_screenwidth() // 2) #+ (width // 2)
    y = (winR.winfo_screenheight() // 2) - (height // 2)
    winR.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        
def SaveTable():
    NumJobsStr = combobox_NumJobs.get()
    NumJobsInt = int(NumJobsStr)
    #---------------------------------------------------------
    try:
        print(lstWorkDescr)
        wb = Workbook()
        sheet = wb.active
        sheet.title = "Проводимые работы"

        #Задаем стиль1
        ns1 = NamedStyle(name = "style1")
        ns1.font = Font(bold = True, size = 12)
        border = Side(style = "thin", color = "000000")
        ns1.border = Border(left = border, top = border,
                            right = border, bottom = border)
        ns1.alignment = Alignment(wrap_text = True, horizontal = "center",
                                  vertical = "center")
        wb.add_named_style(ns1)
        #---------------------
        #Задаем стиль2
        ns2 = NamedStyle(name = "style2")
        ns2.font = Font(size = 12)
        border = Side(style = "thin", color = "000000")
        ns2.border = Border(left = border, top = border,
                            right = border, bottom = border)
        ns2.alignment = Alignment(horizontal = "center",
                                  vertical = "center")
        wb.add_named_style(ns2)
        #---------------------
        #Задаем стиль2
        ns3 = NamedStyle(name = "style3")
        ns3.font = Font(size = 12)
        border = Side(style = "thin", color = "000000")
        ns3.border = Border(left = border, top = border,
                            right = border, bottom = border)
        ns3.alignment = Alignment(wrap_text = True, horizontal = "left",
                                  vertical = "center")
        wb.add_named_style(ns3)

        sheet.column_dimensions["B"].width = 42
        sheet.column_dimensions["C"].width = 15
        sheet.row_dimensions[1].height = 30

        row = 1
        sheet["A"+str(row)].style = "style1"
        sheet["B"+str(row)].style = "style1"
        sheet["C"+str(row)].style = "style1"

        sheet["A"+str(row)] = "Номер\nработы"
        sheet["B"+str(row)] = "Описание работы"
        sheet["C"+str(row)] = "Длительность\n(дней)"

        for i in range(0,NumJobsInt):
            row += 1
            sheet["A"+str(row)].style = "style2"
            sheet["B"+str(row)].style = "style3"
            sheet["C"+str(row)].style = "style2"

            sheet["A"+str(row)] = str(i+1)
            sheet["B"+str(row)] = lstWorkDescr[i]
            sheet["C"+str(row)] = lstWorkDay[i]

        fileName = "ПроводимыеРаботы.xlsx"
        wb.save(fileName)

        os.chdir(sys.path[0])
        os.system('start excel.exe "%s\\%s"' % (sys.path[0],fileName,))

    except (KeyError, NameError):
        messagebox.showwarning("Предупреждение",
                               "Таблица не создана! Нажмите кнопку \"Далее\".")
    except PermissionError:
        messagebox.showwarning("Предупреждение",
                               "Закройте MS Excel!")
    except IndexError:
        messagebox.showwarning("Предупреждение",
                               "Заполните таблицу и нажмите на кнопку \"Далее\"!")

def Theory():
    wb.open("Theory.pdf",new = 2)


#=========================================================================
win = Tk()
win.title("Построение сетевого графика")
win.geometry('500x520')
win.resizable(False, False)
winCenter(win)
win.iconbitmap("files\\NetDiag.ico")
#-------------------------
#Создание меню
mainmenu = Menu(win)
win.config(menu = mainmenu)
mainmenu.add_command(label = "Сохранить таблицу в Excel", command = SaveTable)
mainmenu.add_command(label = "Инструкция", command = Theory)
#------------------------------------------------------------
cnvWin = Canvas(win, width = 485, height = 200)
cnvWin.create_rectangle(4, 5, 485, 50,
                               outline = "#fe8900",
                               fill = "#fadeaf")
cnvWin.place(x = 5, y = 5)
#----------------------------------------------------------------
label_NumJobs = Label(win, text = "Выберите количество работ:",
                      bg = "#fadeaf")
label_NumJobs.config(font = ('Calibri',12))
label_NumJobs.place(x = 20,y = 20)
#---------------------------------
lst_NumJobs = list(range(5,13))

combobox_NumJobs = ttk.Combobox(win, state = "readonly",
                         values = lst_NumJobs, width = 3)
combobox_NumJobs.current(2)
combobox_NumJobs.bind("<<ComboboxSelected>>", clearInfoCombobox)
style = ttk.Style()
style.map('TCombobox', fieldbackground=[('readonly','white')])

NumJobsStr = combobox_NumJobs.get()
NumJobsInt = int(NumJobsStr)
combobox_NumJobs.place(x = 230,y = 23)

lstSave = [2]
sumE = 1
flagBtn = False
flagWO = False
#-------------------------------------------------------------
label_AboutAuthor = Label(win, text = "Винокурова Д.В., 2020")
label_AboutAuthor.config(font = ('Calibri',10))
label_AboutAuthor.place(x = 10,y = 465)

#----------------------------------------------
#win.protocol("WM_DELETE_WINDOW", delete_window)

win.mainloop()
