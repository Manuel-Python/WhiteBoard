
sum = 0
firstNum = 1 # 1st term of sequence
secondNum = 1 # 2nd term of sequence
nextTerm = 0
index = 2

while len(str(nextTerm)) != 1000:
    nextTerm = firstNum + secondNum
    firstNum = secondNum
    secondNum = nextTerm
    index += 1

print(index)
print(nextTerm)
#print("The sum of the even Fibonacci terms below 4,000,000 is {} ".format(sum))