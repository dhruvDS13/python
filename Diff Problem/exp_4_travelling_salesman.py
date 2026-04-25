#PROG 4
import itertools

def calculate_total_distance(path, dist_matrix):
    total_dist = 0
    for i in range(len(path) - 1):
        total_dist += dist_matrix[path[i]][path[i + 1]]
    total_dist += dist_matrix[path[-1]][path[0]]  # Return to starting city
    return total_dist

def traveling_salesman(dist_matrix):
    n = len(dist_matrix)
    cities = list(range(n))
    min_distance = float('inf')
    best_path = None

    # Generate all permutations of cities
    for perm in itertools.permutations(cities):
        dist = calculate_total_distance(perm, dist_matrix)
        if dist < min_distance:
            min_distance = dist
            best_path = perm

    return best_path, min_distance

# Example usage
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
best_path, min_distance = traveling_salesman(dist_matrix)
print("Best path:", best_path)
print("Minimum distance:", min_distance)


#knapsack

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the dp table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
max_value = knapsack(weights, values, capacity)
print("Maximum value in Knapsack:", max_value)