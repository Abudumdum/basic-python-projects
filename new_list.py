

def new_list(list_1, list_2):
    list_3 = []
    for x in list_1:
        if x % 2 == 1:
            list_3.append(x)
    for x in list_2:
        if x % 2 == 0:
            list_3.append(x)
    return list_3


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [23, 45, 22, 67, 78, 98, 35, 71]

print(new_list(list_1, list_2))
