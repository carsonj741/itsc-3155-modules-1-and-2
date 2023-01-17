word = str(input("Enter a string: "))
letter = []
spread = []
y = 0
a = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0


for x in word:
    letter.append(x)
    y+=1


if y%3 >= 1:
    h = y%3
    y = int(y/3) 

if y%3 == 0:
    y = int(y/3)
 





while a <= y:
    if a<y and h != 0:
        spread += [["","",""]]
        a += 1
        continue
    if h == 1 and a==y:
        spread +=[[""]]
        a += 1
        break
    if h == 2 and a==y:
        spread +=[["",""]]
        a +=1
        break
    if h==0 and a<y:
        spread += [["","",""]]
        a+=1
    if h==0 and a==y:
        break

        
        
    


for w in letter:
    spread[c][d] = w
    d += 1
    if d == 3:
        c +=1
        d = 0
    if c == y+1:
        break
    if c == y and h == 0:
        break


print(spread)




    



