def next_gap(gap):
    """다음 간격을 계산합니다 (절반으로 줄이되 올림 처리)"""
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)

def in_place_merge_gap(arr, left, mid, right):
    """
    배열 요소를 뒤로 한 칸씩 밀어내는(Shifting) 대신,
    일정 간격(Gap)만큼 떨어진 요소들을 직접 스왑하여 O(1) 공간으로 병합합니다.
    """
    gap = next_gap(right - left + 1)
    
    while gap > 0:
        i = left
        while i + gap <= right:
            j = i + gap
            # 앞의 요소가 뒤의 요소보다 크면 위치를 바꿈 (Shifting 방지)
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
        # 간격을 다시 절반으로 줄임
        gap = next_gap(gap)

def in_place_merge_sort_iterative(arr):
    """
    재귀 함수(콜 스택)조차 사용하지 않는 Bottom-up 방식
    -> 진정한 O(1) 공간 복잡도 달성
    """
    n = len(arr)
    curr_size = 1
    
    while curr_size < n:
        left = 0
        while left < n - 1:
            mid = min(left + curr_size - 1, n - 1)
            right = min(left + 2 * curr_size - 1, n - 1)
            
            in_place_merge_gap(arr, left, mid, right)
            left += 2 * curr_size
            
        curr_size *= 2

# 테스트 진행 (길이가 11인 까다로운 배열도 에러 없이 완벽 동작)
test_arr = [12, 11, -3, 13, 5, 6, 7, -1, 9, 20, 2]
in_place_merge_sort_iterative(test_arr)
print(f"정렬된 배열: {test_arr}")