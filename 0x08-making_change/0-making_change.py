#!/usr/bin/python3
"""Module contains code for solving the coin change problem only.
"""


def makeChange(coins, total):
    """Find the minimum number of coins to make total
    """
    if total <= 0:
        return 0

    memo = [float('inf')] * (total + 1)
    memo[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            memo[i] = min(memo[i], memo[i - coin] + 1)

    return memo[total] if memo[total] != float('inf') else -1
