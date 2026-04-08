def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
arr = [10, 20, 30, 40, 50]
target = 40
print(f"Binary Search Result at index: {binary_search(arr, target)}")

#Time Complexity:
'''Best Case: 𝑂(1)
Worst Case:O(nlogn) '''
#Space Complexity: 𝑂(1).