#PROGRAM 1
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr)
print("Sorted array:", arr) 