x = input("Enter a string: ")
letter = []
back = []
c = 0

z = len(x)

print(z)

for y in x:
    letter.append(y)

print(letter)

while c<z:
    back += [""]
    c +=1

a = 0
b = z-1



while a<z:
    back[a] = letter[b]
    b -= 1
    a+=1
print(back)


