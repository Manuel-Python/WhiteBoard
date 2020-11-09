#Circular primes Q35
#How many circular primes are there below one million?

def rotate(strg, n):
    return strg[n:] + strg[:n]

def rotateNum(num):
    a = str(num)
    l = findLen(a)

    for i in range(0,l):
        a = rotate(a,-1)
        if not isPrime(int(a)):
           return False

    return True



def isPrime(n) :

    # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True

# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

print("How many circular primes are there below one million?")

count = 0
for n in range(1,1000000):
    if rotateNum(n):
        count += 1
        print(n)

print("The count is {}".format(count))