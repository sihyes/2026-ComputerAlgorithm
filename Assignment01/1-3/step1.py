def in_place_merge(arr, left, mid, right, max_val):
    i = left
    j = mid + 1
    k = left
    
    # Merge elements by storing both old and new values in the same index
    while i <= mid and j <= right:
        if (arr[i] % max_val) <= (arr[j] % max_val):
            arr[k] += (arr[i] % max_val) * max_val
            i += 1
        else:
            arr[k] += (arr[j] % max_val) * max_val
            j += 1
        k += 1
        
    # Process remaining elements
    while i <= mid:
        arr[k] += (arr[i] % max_val) * max_val
        i += 1
        k += 1
        
    while j <= right:
        arr[k] += (arr[j] % max_val) * max_val
        j += 1
        k += 1
        
    # Decode the array to finalize the sorted values
    for index in range(left, right + 1):
        arr[index] //= max_val

def in_place_merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return
        
    # Max_val must be strictly greater than any element in the array
    max_val = max(arr) + 1
    
    # Bottom-up iterative approach to maintain O(1) space (avoids recursion stack)
    curr_size = 1
    while curr_size < n:
        left = 0
        while left < n - 1:
            mid = min(left + curr_size - 1, n - 1)
            right = min(left + 2 * curr_size - 1, n - 1)
            
            in_place_merge(arr, left, mid, right, max_val)
            left += 2 * curr_size
            
        curr_size *= 2

# Testing the algorithm
test_arr = [9, 3, 5, 1, 8, 2, 7, 4, 6]
in_place_merge_sort(test_arr)
print(f"Q3 Sorted Array (Iterative O(1) Space): {test_arr}")