def dp_knapsack(costs, values, budget, scale_factor=10000):
    scaled_costs = [int(c / scale_factor) for c in costs]
    scaled_budget = int(budget / scale_factor)

    n = len(values)
    W = scaled_budget

    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if scaled_costs[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - scaled_costs[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= scaled_costs[i - 1]

    return selected[::-1]
