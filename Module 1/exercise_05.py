list1 = []
list2 = []
cList = []

a = 0
b = 0

x = 0
y = 0

while a < 5:
    list1.append(int(input("Enter a number for the first list: ")))
    a += 1
while b < 5:
    list2.append(int(input("Enter a number for the second list: ")))
    b += 1
while x == 0:
    if list1[y] in list2:
        cList.append(int(list1[y])) 
    y += 1
    if y == 5:
        break

print("First list: " + str(list1))
print("Second list: " + str(list2))
print("Common list: " + str(cList))
    
