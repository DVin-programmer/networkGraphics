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
print("Индексы:",lst_index)

# Создание списков в количестве lst_sum
for i in range(sum_lst):
    globals()["lst"+str(i+1)] = [1]
print(globals())

num_is_table = 5
print("len(t)",len(t))
for k in range(0, len(t)):
    print("---------------")
    i = 0
    quantity = 0
    while i != len(t):
        if i in lst_index:
            i += 1
        #if i == k:
        #    i += 1
        print("k:", k," i:", i)

        print(t[k][1] == num_is_table)
        if t[k][1] == num_is_table:
            globals()["lst" + str(k + 1)].append(t[k][1])
        print("По индексам "+ str(k)+" и "+str(i), '=',
              t[k][1], t[i][0], t[k][1] == t[i][0])
        if t[k][1]  == t[i][0]:
            print("индекс:",i)
            quantity += 1
            if quantity > 1:
                globals()["lst" + str(len(lst_index)+1)] = [1]
                globals()["lst" + str(len(lst_index)+1)].append(t[k][1])
            elif k in lst_index:
                globals()["lst" + str(k + 1)].append(t[k][1])
        i += 1
        if i + 1 > len(t):
            break
        #if t[k][1]  == t[i][0]

print(globals())



"""lst_index = []
lst_for_create = []
num_is_table = 5
for j in range(1,num_is_table + 1):
    sum_lst = 0
    print("---------------")
    for i in range(len(t)):
        print(t[i][0], j,t[i][0] == j)
        if t[i][0] == j:
            sum_lst += 1
    print("sum_lst:",sum_lst)
    if sum_lst > 1:
        lst_for_create.append(sum_lst)
            #lst_index.append(i)
#print("Количество путей из 1:", sum_lst)
print("lst_for_create:", lst_for_create)"""




'''i = 0
while i:
    if i in lst_index:
       i += 1'''


