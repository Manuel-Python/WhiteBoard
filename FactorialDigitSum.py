#Factorial digit sum
#Problem 20

#Find the sum of the digits in the number 100!

total = 0
for n in range(100,0,-1):
    if total == 0:
        total = n
        continue
    total = total * n

a = str(total)

total = 0
for char in a:
    total += int(char)

print(total)
