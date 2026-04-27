def insertion_sort(arr):
    """
    Perform insertion sort on the given array using the decrease and conquer technique.

    Parameters:
        arr (list): The array to be sorted.

    Returns:
        None: The array is sorted in place.
    """
    # Iterate through the array from the second element to the last
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted
        j = i - 1  # Index of the last element in the sorted portion

        # Debugging statement to track the current key
        print(f"Sorting key: {key}, Current array: {arr}")

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1

        # Place the key at its correct position
        arr[j + 1] = key

        # Debugging statement to show array after placing the key
        print(f"Placed key: {key}, Updated array: {arr}")

# Example usage:
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
#    print("Original array:", arr)
    insertion_sort(arr)
    print("Sorted array:", arr)

