#Special Pythagorean triplet Q9
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

for a in range(1, 1000):
    for b in range(1, 1000):
        p1 = (a ** 2) # a^2
        p2 = (b ** 2) # b^2
        c = (p1 + p2) ** (0.5) # sqrt (p1 + p2) = c

        if (a + b + c) == 1000:
            print("values are {0}, {1}, {2}".format(a,b,int(c)))
            print(int(a*b*c))
            break

