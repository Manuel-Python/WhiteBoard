# Double-base palindromes Q36
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def isPalindrome(n) :
    num = str(n)
    numLen = len(num)
    if numLen == 1:
        return True
    numTest = False
    for i in range(0, int(numLen/2)): # range half the number
        if num[i] != num[(numLen-1)-i]: # test the first half to last half
            numTest = False
            break
        else:
            numTest = True
    return numTest

sum = 0
for n in range(1,1000000):
    n_bin = bin(n)[2:]
    if isPalindrome(n) and isPalindrome(n_bin):
        sum += n
        print("{} {}".format(n, n_bin))

print("Palindrome sum is {}.".format(sum))
