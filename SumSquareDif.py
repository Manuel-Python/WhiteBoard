print("Find the difference between the sum of the squares of the first one hundred") #Q6
print("numbers and the square of the sum.\n")

sumSquares = 0
sum = 0
for n in range(1,101):
    sum += n
    sumSquares += n ** 2

sum = sum ** 2
print("Sum = {} and squares = {}".format(sum,sumSquares))

answer = sum - sumSquares
print("The Q6 answer is {}".format(answer))

print('\007') # ring bell when finished