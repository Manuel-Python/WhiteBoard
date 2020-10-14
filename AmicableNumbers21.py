print("Amicable Numbers Q21")

#Evaluate the sum of all the amicable numbers under 10000.


def divisorSum(num):
    sum = 0
    for divisor in range(1,int(num/2)+1): #int(num/2+1)
        if num % divisor == 0:
            sum += divisor
    return sum


total = 0
for n in range(1,10000):
    a = divisorSum(n)
    b = divisorSum(a)
    if b == n and a != b:
        total += n

print("The total of amicable numbers is {}.".format(total))



