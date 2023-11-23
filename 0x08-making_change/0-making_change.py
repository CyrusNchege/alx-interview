#!/usr/bin/python3
""" Making Change"""


def makeChange(coins, total):
    """ Given a pile of coins of different values, determine the fewest number
        of coins needed to meet a given amount total.
        Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        while coin <= total:
            total -= coin
            num_coins += 1
    if total == 0:
        return num_coins
    return -1