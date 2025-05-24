import numpy as np

def greedy_knapsack(costs, values, budget):
    ratio = values / costs
    sorted_indices = np.argsort(ratio)[::-1]

    total_cost = 0
    selected = []

    for i in sorted_indices:
        if total_cost + costs[i] <= budget:
            selected.append(i)
            total_cost += costs[i]
    
    return selected
