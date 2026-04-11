import random

# 비교 횟수 측정을 위한 전역 변수
comparison_count = 0

def quick_sort(arr, low, high):
    if low < high:
        # 무작위 피벗을 사용하는 파티션 함수 호출
        pi = randomized_partition(arr, low, high)
        
        # 재귀적으로 하위 배열 정렬
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def randomized_partition(arr, low, high):
    # low와 high 사이의 무작위 인덱스를 선택
    rand_pivot_idx = random.randint(low, high)
    
    # 무작위로 선택된 피벗을 첫 번째 요소(low)와 교환
    arr[low], arr[rand_pivot_idx] = arr[rand_pivot_idx], arr[low]
    
    # 이후 기존의 partition 로직을 그대로 수행
    return partition(arr, low, high)

def partition(arr, low, high):
    global comparison_count
    
    # 이제 arr[low]는 무작위로 선택된 피벗입니다.
    pivot = arr[low]
    i = low + 1
    
    for j in range(low + 1, high + 1):
        comparison_count += 1 # 비교 연산 카운트
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    # 피벗을 올바른 위치로 이동
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

# --- 이전의 악의적인(Adversarial) 배열 테스트 ---
adversarial_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
comparison_count = 0
quick_sort(adversarial_array, 0, len(adversarial_array) - 1)

print(f"정렬된 배열: {adversarial_array}")
print(f"비교 횟수 (n=10): {comparison_count}")