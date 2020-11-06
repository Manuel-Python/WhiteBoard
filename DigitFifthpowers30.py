#Digit fifth powers Q30

#Surprisingly there are only three numbers that can be written
# as the sum of fourth powers of their digits:

#1634 = 14 + 64 + 34 + 44
#8208 = 84 + 24 + 04 + 84
#9474 = 94 + 44 + 74 + 44

#As 1 = 14 is not a sum it is not included.

#The sum of these numbers is 1634 + 8208 + 9474 = 19316.

#Find the sum of all the numbers that can be written as the sum of
# fifth powers of their digits.

def fifthPower(num):
    numArray = []
    a = str(num)
    #index = 0
    for n in a:
        #numArray.append(n)
        #index += 1
        total = int(n) ** 5
    # n1 = int(numArray[0]) ** 5
    # n2 = int(numArray[1]) ** 5
    # n3 = int(numArray[2]) ** 5
    # n4 = int(numArray[3]) ** 5
    # n5 = int(numArray[4]) ** 5
    #
    # total = n1 + n2 + n3 + n4 + n5

    if total == num:
        print(num)
        return True
    else:
        return False

    # print("{} {} {} {}".format(n1,n2,n3,n4)) 240559 A443839
    # print(total)
sum = 0
for n in range(2,99999):
    if fifthPower(n):
        sum += n

print(sum)
