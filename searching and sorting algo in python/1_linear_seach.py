def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30
print(f"Linear Search Result at index: {linear_search(arr, target)}")

# Time Complexity:
'''Best Case: O(1)
    worst: O(n)
'''
# Space cpmplexity: O(1)