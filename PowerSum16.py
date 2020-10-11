# What is the sum of the digits of the number 21000? Q16

num = 2 ** 1000

numString = str(num)

sum = 0
for n in range(len(numString)):
    a = int(numString[n])
    sum += a

print(sum)