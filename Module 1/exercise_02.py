x = input("Enter a string: ")
y = input("Enter another string: ")

if x in y:
    print(True)
elif y in x:
    print(True)
else:
    print(False)