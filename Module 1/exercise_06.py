x = int(input("Enter a row number from 1 to 5: "))
y = int(input("Enter a col number from 1 to 5: "))

l = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
l[x-1][y-1] = 1

y = 0
x = 0
while y<5:
    print(l[x])
    x += 1
    if x == 5:
        break


