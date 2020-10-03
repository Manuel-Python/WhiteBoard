# What is the smallest positive number that is evenly divisible  Q5
# by all of the numbers from 1 to 20?


def isDivisable(num) :
    divTest = True
    for n in range(1, 21):
        if num % n != 0:
                divTest = False
                break
    return divTest

numTest = False
num = 21
while numTest == False:
    if isDivisable(num):
        numTest = True
        print("Smallest positive number is {}".format(num))
    num += 1

print('\007') # ring bell when finished