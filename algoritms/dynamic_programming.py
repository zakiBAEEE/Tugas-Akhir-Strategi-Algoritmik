import numpy as np

def dp_knapsack(costs, values, budget):
    n = len(values)
    W = int(budget)

    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Mengisi tabel DP
    for i in range(1, n + 1):
        for w in range(W + 1):
            if costs[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - int(costs[i-1])] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # Lacak item terpilih
    w = W
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= int(costs[i-1])

    return selected[::-1]
