import random #STEP3. to select randomized pivot  (me)

comparison_count = 0 # STEP 2 : 전역변수 to track the number of comparisons (me)

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = randomized_partition(arr, low, high)
        
        # Recursively sort the sub-arrays
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def randomized_partition(arr, low, high): #STEP 3 : randomized pivot partition 얻기
    # low와 high 사이의 무작위 인덱스를 선택
    rand_pivot_idx = random.randint(low, high)
    
    # 무작위로 선택된 피벗을 첫 번째 요소(low)와 교환
    arr[low], arr[rand_pivot_idx] = arr[rand_pivot_idx], arr[low]
    
    # 이후 기존의 partition 로직을 그대로 수행
    return partition(arr, low, high)

def partition(arr, low, high):
    global comparison_count #STEP 2 : me

    # STEP3: Select the random! element as the pivot
    pivot = arr[low]
    
    # 'i' tracks the boundary of elements smaller than the pivot
    i = low + 1
    
    for j in range(low + 1, high + 1):
        comparison_count += 1  # STEP 2 : Increment counter for every comparison made against the pivot (me)

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
comparison_count = 0 # STEP2 : Reset counter
quick_sort(unsorted_array, 0, len(unsorted_array) - 1)
print(f"Q1 Sorted Array: {unsorted_array}")
print(f"Comparisons (Average Case, n=10): {comparison_count}") # STEP2 : Testing the Worst Case (Adversarial Input) ---
print("-" * 40)

# STEP2 : Testing the Worst Case (Adversarial Input) ---
adversarial_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
comparison_count = 0 # Reset counter
quick_sort(adversarial_array, 0, len(adversarial_array) - 1)

print(f"Adversarial Sorted Array: {adversarial_array}")
print(f"Comparisons (Worst Case, n=10): {comparison_count}")