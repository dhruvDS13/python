#Counting Sort counts the occurrences of each element and uses this information to place elements directly into the sorted array.
def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    sorted_array = []
    for i in range(len(count)):
        sorted_array.extend([i] * count[i])

    return sorted_array

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
print(f"Counting Sort Result: {counting_sort(arr)}")

#Time Complexity:O(n+k) where n is the number of elements and k is the range of input values.
#Space Complexity: O(k)