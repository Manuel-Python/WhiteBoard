#Lattice paths
#Problem 15

from math import factorial

#binomial coefficient function
# nck(n,k) from #http://radiusofcircle.blogspot.com
def nck(n,k):
    #function which will return the binomial coefficient
    #of n,k
    return factorial(n)//(factorial(k)*factorial(n-k))

#Number of lattice paths from (0,0) to (a,b) is given by
#binomial coefficient C(a+b,a)
print ("Number of lattice paths is: {}".format(nck(20+20,20)))
