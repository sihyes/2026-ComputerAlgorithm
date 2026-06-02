A = [24, 75, 92, 83, 61, 48, 97, 50]

# 방법 1
def findMaxMin_1(A):
    count = 0
    n = len(A)
    max_val = min_val = A[0]
    for i in range(1, n):
        count += 1  
        if A[i] > max_val:
            max_val = A[i]
        
        count += 1 
        if A[i] < min_val:
            min_val = A[i]

    return min_val, max_val, count

# 방법 2
def findMaxMin_2(A, i, j):
    count = 0
    if i == j:  # 요소 1개
        return A[i], A[i], 0
    
    elif j == i + 1:  # 요소 2개
        count += 1  
        if A[i] < A[j]:
            return (A[i], A[j], count)
        else:
            return (A[j], A[i], count)
    else:
        mid = (i + j) // 2
        (min1, max1, c1) = findMaxMin_2(A, i, mid)
        (min2, max2, c2) = findMaxMin_2(A, mid + 1, j)
        
        # 합칠 때 발생하는 비교 2회
        count = c1 + c2 + 2
        return min(min1, min2), max(max1, max2), count

# 결과
min_val_1, max_val_1, count1 = findMaxMin_1(A)
print(f"방법 1 - 최솟값: {min_val_1}, 최댓값: {max_val_1}, 비교 횟수: {count1}")

min_val_2, max_val_2, count2 = findMaxMin_2(A, 0, len(A) - 1)
print(f"방법 2 - 최솟값: {min_val_2}, 최댓값: {max_val_2}, 비교 횟수: {count2}")