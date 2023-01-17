x = input("Enter a string: ")
upper = []
lower = []


y = len(x)

x = x.replace(" ","")

print(x)

for z in x:
     if z == z.upper():
        upper.append(z)
     if z == z.lower():
        lower.append(z)



print(upper)
print(lower)

lower = "".join(lower)
upper = "".join(upper)

print(lower+upper)

