#!/usr/bin/python3
"""Module contains code for solving the coin change problem only.
"""


def makeChange(coins, total):
    """Find the minimum number of coins to make total
    """
    '''
    if total <= 0:
        return 0

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
'''

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
