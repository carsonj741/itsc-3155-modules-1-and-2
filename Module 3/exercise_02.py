def combine(list1,list2):
    list3 = {}
    for x, value in list1.items():
        if x in list2.keys():
            list3[x] = value + list2[x]
    return list3

list1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
list2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

list4 = combine(list1, list2)

print(list4)
