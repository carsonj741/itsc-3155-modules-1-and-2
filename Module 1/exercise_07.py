x = 0

total = 0

nums = []
evenNums = []

while x == 0:
    val = input("Enter a number or QUIT to quit: ")
    if(val == "QUIT"):
        y = 0
        x=1
        break
    else:
        nums.append(int(val))
        total += 1

print("All nums: " + str(nums))


while y < total:
    if nums[y] % 2 == 0:
        val2 = nums[y]
        evenNums.append(int(val2))       
    elif total == 0:
        print("No values entered")
        break
    y+=1

print("Even nums: " + str(evenNums))