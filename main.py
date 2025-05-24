from utils.data_loader import load_dataset, prepare_knapsack_data
from algorithms.greedy import greedy_knapsack
from algorithms.dynamic_programming import dp_knapsack
from utils.metrics import total_cost, total_value, efficiency

BUDGET = 1_000_000  # misalnya 1 juta rupiah
PLATFORM = 'instagram'

# Load & siapkan data
df = load_dataset(PLATFORM)
costs, values = prepare_knapsack_data(df)

# Greedy
selected_greedy = greedy_knapsack(costs, values, BUDGET)
val_greedy = total_value(selected_greedy, values)
cost_greedy = total_cost(selected_greedy, costs)

# DP
selected_dp = dp_knapsack(costs, values, BUDGET)
val_dp = total_value(selected_dp, values)
cost_dp = total_cost(selected_dp, costs)

print("\n=== GREEDY ===")
print(df.iloc[selected_greedy][['name', 'estimated_cost', 'profit_score']])
print(f"Total Cost: {cost_greedy}, Total Value: {val_greedy}, Efficiency: {efficiency(val_greedy, cost_greedy):.4f}")

print("\n=== DYNAMIC PROGRAMMING ===")
print(df.iloc[selected_dp][['name', 'estimated_cost', 'profit_score']])
print(f"Total Cost: {cost_dp}, Total Value: {val_dp}, Efficiency: {efficiency(val_dp, cost_dp):.4f}")
