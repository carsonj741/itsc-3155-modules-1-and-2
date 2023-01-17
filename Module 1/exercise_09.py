list1 = []

i = 0

while i < 5:
    list1.append(str(input("Enter a word: ")))
    i+=1

print("Words: " + str(list1))

word = str(list1[0]) + " " + str(list1[1]) + " " + str(list1[2]) + " " + str(list1[3]) + " " + str(list1[4])

print("One string: " + word)