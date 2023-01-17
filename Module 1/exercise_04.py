n = int(input("Enter a number: "))

i = 1

nums = []

total = 0.0

while i<=n:
    x = float(input("Enter number " + str(i) + ": "))
    total += x
    nums.append(x)
    i+=1
print(nums)
print(total/n)


    