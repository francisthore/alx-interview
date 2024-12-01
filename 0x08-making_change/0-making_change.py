#!/usr/bin/python3

"""Takes a pile of coins and makes change"""


def makeChange(coins, total):
    """Makes change by flipping coins"""
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    count, value, index = 0, total, 0
    while value > 0 and index < len(coins):
        if value >= coins[index]:
            value -= coins[index]
            count += 1
        else:
            index += 1
    return count if value == 0 else -1
