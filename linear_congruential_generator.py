def lcg(modulus, a, c, seed):
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed

a = lcg(2**31,1103515245,12345,10)

for num in a:
    print(num)