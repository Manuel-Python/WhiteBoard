# Pandigital prime Q41
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

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


def pandigitalTest(num):
    a = str(num)
    l = findLen(a)
    index2 = 0
    print(l)
    for index1 in range(0,l):
        char = a[index1]

        for test in a:
            print(" {} {}".format(test,char))
            if index1 == index2:
                print("Test {} {}".format(index1, index2))
                continue
            if char == test:
                 return False
            index2 += 1
    # if isPrime(num):
    #     return True
    # else:
    #     return False
    return True



# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter


# 167809
# 167863
# 167873
# 167879
# 167887
# 167899
# 167953
print(pandigitalTest(167899))
#a = 1234567890
# for n in range(1,9999999999):
#     if pandigitalTest(n):
#         print(n)