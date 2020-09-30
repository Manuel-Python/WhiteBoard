# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

sum = 0
firstNum = 1 # 1st term of sequence
secondNum = 1 # 2nd term of sequence
nextTerm = 0

while sum < 4000000:
    nextTerm = firstNum + secondNum
    firstNum = secondNum
    secondNum = nextTerm

    if nextTerm % 2 == 0:
        sum += nextTerm

print("The sum of the even Fibonacci terms below 4,000,000 is {} ".format(sum))