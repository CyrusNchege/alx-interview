#!/usr/bin/python3
""" Prime Game """

def isWinner(x, nums):
    """ Prime Game """
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] is True:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    primes = []
    for i in range(len(sieve)):
        if sieve[i] is True:
            primes.append(i)
    player1 = 0
    for n in nums:
        c = 0
        for p in primes:
            if p > n:
                break
            c += 1
        if c % 2 == 1:
            player1 += 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"