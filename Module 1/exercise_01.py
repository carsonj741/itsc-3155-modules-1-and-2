x = int(input("Enter a grade from 0 to 100: "))

if x<=100 and x>=90:
    print("Your grade is an A")
elif x<=89 and x>=80:
    print("Your grade is an B")
elif x<=79 and x>=70:
    print("Your grade is an C")
elif x<=69 and x>=60:
    print("Your grade is an D")
elif x<=59 and x>=0:
    print("Your grade is an F")
else:
    print("Error, you did not enter a number within the range.")