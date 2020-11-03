#Based on code from https://codereview.stackexchange.com/questions/39946/optimizing-solution-for-project-euler-problem-23-non-abundant-sums


def GetSumOfDivs(n):
    i = 2
    upper = n
    total = 1
    while i < upper:
        if n%i == 0:
            upper = n/i
            total += upper
            if upper != i: total += i
        i += 1
    return total


def isabundant(n): return GetSumOfDivs(n) > n
lAbundants = [x for x in range(12, 28123) if isabundant(x) == True]
dAbundants = {x:x for x in lAbundants}

sums = 1
for i in range(2, 28123):
    boo = True
    for k in lAbundants:
        if k < i:
            if (i-k) in dAbundants:
                boo = False
                break
        else : break
    if boo == True: sums += i

print(sums)

# def is_abundant(n):
#     max_divisor = int(n / 2) + 1
#     sum = 0
#     for x in range(1, max_divisor):
#         if n % x == 0:
#             sum += x
#     return sum > n
#
# abundants = list(x for x in range(1, 28123) if is_abundant(x))
#
# sums = 0
# for i in range(12, 28123):
#     for abundant in abundants:
#         if abundant >= i and is_abundant(i + abundant):
#             sums += i
# print(sums)