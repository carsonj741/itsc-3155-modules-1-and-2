x = 0
list1 = []

sum = 0
while x<5:
    y = input("Enter number #" + str(x + 1) + ": ")
    print(y)

    if y.isdigit() == False:
        print("Invalid input. Please enter an int.")
    else:
        list1.append(y)
        sum += int(y)
        x+=1
print("Your sum is :" + str(sum))

