def compute_metrics(selected_indices, cost_list, value_list, start_time, end_time):
    total_cost = sum(cost_list[i] for i in selected_indices)
    total_value = sum(value_list[i] for i in selected_indices)
    duration = end_time - start_time

    return {
        "total_cost": total_cost,
        "total_value": total_value,
        "duration": duration
    }
