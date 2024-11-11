#!/usr/bin/python3
"""
Module to calculate the minimum operations required to reach n 'H' characters
using only 'Copy All' and 'Paste' operations.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to
    get exactly n 'H' characters.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
