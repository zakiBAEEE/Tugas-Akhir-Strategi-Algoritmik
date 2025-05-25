import numpy as np

def greedy_knapsack(cost, value, budget):
    value = np.array(value, dtype=float)
    cost = np.array(cost, dtype=float)

    items = []
    for i in range(len(value)):
        if cost[i] > 0:
            ratio = value[i] / cost[i]
        else:
            ratio = 0  
        items.append((i, ratio))

    # Urutkan berdasarkan rasio engagement per rupiah (descending)
    items.sort(key=lambda x: x[1], reverse=True)

    selected = []
    total_cost = 0

    for i, _ in items:
        if total_cost + cost[i] <= budget:
            selected.append(i)
            total_cost += cost[i]

    return selected
