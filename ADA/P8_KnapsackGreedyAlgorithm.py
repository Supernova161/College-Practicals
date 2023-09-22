def fractional_knapsack(weights, values, capacity):
    items = [(w, v) for w, v in zip(weights, values)]
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0
    knapsack = []

    for weight, value in items:
        if capacity >= weight:
            knapsack.append((weight, 1))
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            knapsack.append((weight, fraction))
            total_value += fraction * value
            break

    return total_value, knapsack

# Example usage:
weights = [10, 20, 30]
values = [60, 100, 120]
knapsack_capacity = 50

max_value, selected_items = fractional_knapsack(weights, values, knapsack_capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
