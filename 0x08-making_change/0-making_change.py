#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): A list of coin denominations.
        total (int): The target amount.

    Returns:
        int: The minimum number of coins needed, or -1 if it's not possible.
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Sort coins in descending order for greedy approach
    coins.sort(reverse=True)

    # Initialize dynamic programming list with `total + 1` (impossible value)
    dp = [total + 1] * (total + 1)
    print(dp)
    dp[0] = 0

    # Build solution bottom-up
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] <= total else -1
