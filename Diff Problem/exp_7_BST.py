def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.
    
    Parameters:
        arr (list): The sorted array to search.
        target (int): The element to search for.
    
    Returns:
        int: The index of the target if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        # Debugging print statement to observe values
        print(f"Low: {low}, High: {high}, Mid: {mid}, Mid-value: {arr[mid]}")

        if arr[mid] == target:  # Check if the middle element is the target
            return mid  # Target found at index mid
        elif arr[mid] < target:  # Target is in the right half
            low = mid + 1
        else:  # Target is in the left half
            high = mid - 1
    
    return -1  # Target not found

# Example usage:
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    result = binary_search(arr, target)

    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found.")
