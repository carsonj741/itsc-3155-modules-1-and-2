def uList(list1):
    list2 = []

    for x in list1:
        if x not in list2:
            list2.append(x)
    
    return list2

list1 = [1,2,3,1,2,3,4,5]
updatedList = uList(list1)
print(updatedList)
