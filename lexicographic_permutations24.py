#Lexicographic permutations Q24

#What is the millionth lexicographic permutation of the digits 0,
# 1, 2, 3, 4, 5, 6, 7, 8 and 9?


# code based on https://blog.dreamshire.com/solutions/project_euler/project-euler-problem-024-solution/

from math import factorial

def perm(n, s):
    if len(s)==1: return s
    q, r = divmod(n, factorial(len(s)-1))
    return s[q] + perm(r, s[:q] + s[q+1:])

a = perm(int(1000000)-1, '0123456789')
print("The millionth lexicographic permutation is {}".format(a))

