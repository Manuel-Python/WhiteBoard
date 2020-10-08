#The following iterative sequence is defined for the set of positive integers:Q14
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

testNum = 0
testCount = 0

def sequence(num):
    count = 1
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = (3 * num) + 1
        count += 1
    #print("{} ".format(num), end='')

    return count

for n in range(2,1000000):
    a = sequence(n)
    if a > testCount:
        testNum = n
        testCount = a

print("{} has {} terms".format(testNum, testCount))