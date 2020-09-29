#Find the sum of all the multiples of 3 or 5 below 1000.
#Project Euler Q1

sum = 0

for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0: # check if multiples of 3 or 5
        sum += n

print("The sum of the multiples of 3 or 5 below 1000 is {} ".format(sum))

