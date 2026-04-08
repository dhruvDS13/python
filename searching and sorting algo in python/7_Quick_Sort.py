def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
print(f"Quick Sort Result: {quick_sort(arr)}")

#Time Complexity:O(nlog(n)) 
#worst : O(n^2)
#Space complexity: O(nlogn)