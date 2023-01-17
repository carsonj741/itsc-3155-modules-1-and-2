nums = []
nums2 = []
dNums = []
oNums = []

i = 1
x = 0
y = 0
z = y+1
a = 0


while i<=10:
   nums.append(int(input("Enter number " + str(i) + ": ")))
   i += 1

nums2 = nums

print("Original list: " + str(nums))

while x==0:
    if nums[y] == nums2[z]:
        dNums.append(int(nums[y])) 
    z += 1
    if z == 10:
        y+=1
        z=y+1
    if(y==9):
        break
while x==0:
    if nums[a] not in dNums:
        oNums.append(int(nums[a]))
    a +=1
    if a == 10:
        break

print("Nums that appear once: " + str(oNums))
    