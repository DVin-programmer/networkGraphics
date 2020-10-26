from termcolor import cprint

dict_in_vtx_rev = {1: [2, 3, 5], 2: [3, 4], 3: [5], 4: [5]}

lst = []
len_way = []
for i in range(1, len(dict_in_vtx_rev) + 1):
    print(dict_in_vtx_rev.get(i), len(dict_in_vtx_rev.get(i)))
    len_way.append(len(dict_in_vtx_rev.get(i)))
    for j in range(0, len(dict_in_vtx_rev.get(i))):
        #cprint("Итерация [" + str(j+1) + "] " + str(dict_in_vtx_rev.get(i)[j]), color="blue")
        #print(dict_in_vtx_rev.get(dict_in_vtx_rev.get(i)[j]))
        #print("------------------------------------")
        #globals()["lst" + str(i) + str(j+1)] = [i, dict_in_vtx_rev.get(i)[j]]
        lst.append([i, dict_in_vtx_rev.get(i)[j]])
#print(globals())
print()
print(len_way)
print(lst)

for i in range(len(lst)):
    for j in range(len_way[0], len(lst)):
        print(j)
        print(lst[i][1], lst[j][0], lst[i][1] == lst[j][0],'индексы',i,j)


'''for i in range(1, len(dict_in_vtx_rev) + 1):
    for j in range(0, len(dict_in_vtx_rev.get(i))):
        print("lst" + str(1) + str(j + 1),globals()["lst" + str(1) + str(j + 1)])'''


