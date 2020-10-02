#Find the largest palindrome made from the product of two 3-digit numbers. Q4

def isPalindrome(n) :
    num = str(n)
    numLen = len(num)
    numTest = False
    for i in range(0, int(numLen/2)): # range half the number
        if num[i] != num[(numLen-1)-i]: # test the first half to last half
            numTest = False
            break
        else:
            numTest = True
    return numTest

palindrome = 0
palX = 0
palY = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        result = x * y
        if isPalindrome(result):
            if result > palindrome:
                palX = x
                palY = y
                palindrome = result

print("Highest palindrome = {}, which is {} x {}".format(palindrome, palX, palY))


