
print("What is the 10 001st prime number? Q7\n")

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

count = 0
prime = 0
number = 2
while count != 10001:
    if isPrime(number):
        prime = number
        count+= 1
    number += 1

print("The 10001 prime is {}".format(prime))