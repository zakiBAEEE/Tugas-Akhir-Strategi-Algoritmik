import numpy as np

def greedy_knapsack(cost, value, budget):
    value = np.array(value)
    cost = np.array(cost)

    items = [(i, value[i] / cost[i]) for i in range(len(value))]
    items.sort(key=lambda x: x[1], reverse=True)

    selected = []
    total_cost = 0

    for i, _ in items:
        if total_cost + cost[i] <= budget:
            selected.append(i)
            total_cost += cost[i]

    return selected
