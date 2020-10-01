#Largest prime factor Q3
#What is the largest prime factor of the number 600851475143 ?

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

high = 0 #HCF
for n in range(1, 600851475144):
    if 600851475143 % n == 0:
        if not(n % 2 == 0): #Disregard prime test if / 2
            if isPrime(n):
                if high < n:
                    high = n

print(high)
