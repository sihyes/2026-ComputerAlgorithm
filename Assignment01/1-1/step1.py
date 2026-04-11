def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        
        # Recursively sort the sub-arrays
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # Select the first element as the pivot
    pivot = arr[low]
    
    # 'i' tracks the boundary of elements smaller than the pivot
    i = low + 1
    
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            # Swap elements to move smaller ones to the left
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    # Swap the pivot into its correct, sorted position
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    
    # Return the final index of the pivot
    return i - 1

# Testing the algorithm
unsorted_array = [21, 3, 12, 15, 7, 32, 4, 25, 9, 18]
quick_sort(unsorted_array, 0, len(unsorted_array) - 1)
print(f"Q1 Sorted Array: {unsorted_array}")