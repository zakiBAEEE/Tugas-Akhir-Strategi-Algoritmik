def total_value(selected_indices, values):
    return sum(values[i] for i in selected_indices)

def total_cost(selected_indices, costs):
    return sum(costs[i] for i in selected_indices)

def efficiency(value, cost):
    return value / cost if cost > 0 else 0
