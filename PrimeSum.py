#Find the sum of all the primes below two million. Q10

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

sum = 0

for n in range(1,2000000):
    if isPrime(n):
        sum += n

print("The sum of the primes bellow 2 million is {}".format(sum))