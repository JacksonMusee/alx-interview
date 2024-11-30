#!/usr/bin/python3
"""Module contains code for solving the coin change problem only.
"""


def makeChange(coins, total):
    """Find the minimum number of coins to make total
    """
    memo = {0: 0}

    for i in range(1, total + 1):
        for coin in coins:
            subproblem = i - coin

            if subproblem in memo:
                current_best = memo.get(i)
                if current_best:
                    memo[i] = min(current_best, memo.get(subproblem) + 1)
                else:
                    memo[i] = memo.get(subproblem) + 1

    return memo.get(total, -1)
