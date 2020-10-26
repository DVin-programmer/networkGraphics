from termcolor import cprint
'''
Пути: [[1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 5], [1, 5]]
Количество путей: 4'''
t = [(1, 2), (2, 3), (1, 3), (2, 4), (1, 5), (3, 5), (4, 5)]

# Поиск связей у которых первая цифра 1
sum_lst = 0
lst_index = []
for i in range(len(t)):
    if t[i][0] == 1:
        sum_lst += 1
        lst_index.append(i)
print("Количество путей из 1:", sum_lst)
print("Индексы:", lst_index)

# Создание списков в количестве lst_sum с нулевым элементов 1
for i in range(sum_lst):
    globals()["lst"+str(i)] = [1, t[lst_index[i]][1]]
#print(globals())


"""num_is_table = 5
# i = 1, ..., 6
k = 0
index = []
#for k in range(len(lst_index) + p):
while k <= len(lst_index):
    #print("\n===== длина списка", len(lst_index) + p, "\n")
    i = 0
    quantity = 0
    while i != len(t):
        cprint("index:" + str(index), color="magenta")
        if i in index:
            i += 1
        if i in lst_index:
            i += 1
        j = globals()["lst" + str(k)][len(globals()["lst" + str(k)]) - 1:][0]
        print("--------------------------------------------------------------")
        print(t)
        cprint("\nk (по lst_index): " + str(k) +  "  j (последний эл. списка " +\
               "lst" + str(k) + ") : "+ str(j), color="cyan")
        if j == t[i][0]:
            cprint('Итерация [' + str(i) + "]:" + \
                   "   lst" + str(k) + " = " + str(globals()["lst" + str(k)]) + \
                   '  t = ' + str(t[i]) + '\n' + \
                   str(j) + " " + str(t[i][0]) + \
                   " " + str(j == t[i][0]), color="green")
            quantity += 1
            if quantity > 1:
                globals()["lst" + str(len(lst_index))] = []
                for l in range(len(globals()["lst" + str(k)]) - 1):
                    globals()["lst" + str(len(lst_index))].append(globals()["lst" + str(k)][l])
                    print(globals()["lst" + str(len(lst_index))], globals()["lst" + str(k)][l])
                '''globals()["lst" + str(len(lst_index))] += \
                    globals()["lst" + str(k)][:len(globals()["lst" + str(k)]) - 1]
                print("сложение списков:", globals()["lst" + str(k)][:len(globals()["lst" + str(k)]) - 1])
                globals()["lst" + str(len(lst_index))].append(t[i][1])'''
                index.append(i)
                globals()["lst" + str(len(lst_index))].append(t[i][1])
                globals()["lst" + str(k)].append(t[i][1])
            else:
                globals()["lst" + str(k)].append(t[i][1])
            #v += 1
        else:
            cprint('Итерация [' + str(i) + "]:" + \
                   "   lst" + str(k) + " = " + str(globals()["lst" + str(k)]) + \
                   '  t = ' + str(t[i]) + '\n' + \
                   str(j) + " " + str(t[i][0]) + \
                   " " + str(j == t[i][0]), color="red")
        print("--------------------------------------------------------")
        print("результат добавления:", globals()["lst" + str(k)])
        i += 1
        #print("Последний элемент списка:",
        #      globals()["lst" + str(k)][len(globals()["lst" + str(k)]) - 1:][0])
        '''if globals()["lst" + str(k)][len(globals()["lst" + str(k)]) - 1:][0] != num_is_table:
            i = 0'''
    k += 1

print(globals())"""

