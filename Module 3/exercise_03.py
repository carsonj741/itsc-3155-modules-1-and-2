def frequency(value):
    value = value.lower()
    value = value.replace(" ","")
    list1={}
    for x in value:
        if x in list1:
            list1[x] += 1
        else:
            list1[x] = 1
    return list1

value = str(input("Enter a string: "))

print(frequency(value))