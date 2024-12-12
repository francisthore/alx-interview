#!/usr/bin/python3
"""
  Determines the winner of a game based on the strategic
  removal of prime numbers and their multiples from a set
  of consecutive integers.
"""


def isWinner(x, nums):
    """Determines winner of game"""
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        rounds = list(range(1, num + 1))
        primes = get_primes(1, num)

        if not primes:
            ben_wins += 1
            continue

        maria_turn = True

        while True:
            if not primes:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            prime = primes.pop(0)
            rounds.remove(prime)
            rounds = [n for n in rounds if n % prime != 0]
            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None


def is_prime(n):
    """Check if num is pirme"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(start, end):
    """returns a list of primes in a range"""
    return [n for n in range(start, end + 1) if is_prime(n)]
