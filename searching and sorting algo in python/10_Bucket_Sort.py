#Bucket Sort distributes elements into buckets, sorts each bucket individually, and then concatenates them.
def bucket_sort(arr):
    bucket_count = len(arr)
    max_value = max(arr)
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int(num / max_value * (bucket_count - 1))
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()  # Sorting individual buckets using any efficient method

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

# Example usage
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print(f"Bucket Sort Result: {bucket_sort(arr)}")

#Time Complexity:
''' average time: O(n+k) where k is the number of buckets
Worst: O(n^2)
'''
#Space complexity: O(n+k)