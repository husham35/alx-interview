#!/usr/bin/python3
"""
Prime game module.
"""

def generate_primes(n):
    """
    Generate a list of prime numbers up to n using the Sieve of Eratosthenes.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False

    return sieve

def count_primes(sieve, n):
    """
    Count the number of primes less than or equal to n.
    """
    return sum(sieve[:n+1])

def determine_winner(marias_wins, bens_wins):
    """
    Determine the winner based on the number of wins.
    """
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'

def isWinner(x, nums):
    """
    Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = generate_primes(max_num)

    marias_wins = bens_wins = 0

    for n in nums[:x]:
        primes_count = count_primes(primes, n)
        if primes_count % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1

    return determine_winner(marias_wins, bens_wins)
