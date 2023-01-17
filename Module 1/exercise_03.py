x = int(input("Enter an integer greater than 1:"))

i = 0

if x>1:
    while i<=x:
        print("The cube of " + str(i) + " is " + str(i**3))
        i += 1
else:
    print("Please enter a value greater than one")