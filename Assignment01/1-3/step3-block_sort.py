import math

def swap(arr, i, j):
    """두 요소의 위치를 바꿉니다 (O(1) 공간)"""
    arr[i], arr[j] = arr[j], arr[i]

def block_swap(arr, a, b, size):
    """블록(덩어리) 단위로 위치를 바꿉니다. 한 칸씩 밀어내지 않아 O(N) Shifting을 방지합니다."""
    for i in range(size):
        swap(arr, a + i, b + i)

def insertion_sort(arr, left, right):
    """작은 구간이나 마지막 버퍼 정렬을 위한 삽입 정렬"""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def block_merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return

    # 1. 블록 크기 설정: O(sqrt(N))
    block_size = int(math.sqrt(n))
    if block_size < 2:
        insertion_sort(arr, 0, n - 1)
        return

    # 2. 배열을 block_size 단위로 쪼개어 각각 먼저 정렬
    # 이 과정은 전체 시간 복잡도 O(N log N) 범위 내에 들어갑니다.
    for i in range(0, n, block_size):
        end = min(i + block_size, n)
        insertion_sort(arr, i, end - 1)

    # 3. 내부 버퍼(Internal Buffer) 확보
    # 배열의 맨 마지막 블록을 '가짜 임시 배열(버퍼)'처럼 취급하여 병합 과정에서 사용합니다.
    buffer_start = n - (n % block_size if n % block_size != 0 else block_size)
    
    # 4. 블록 병합 (Block Merging)
    # 인접한 두 정렬된 블록을 합칠 때, 빼둔 버퍼 구역을 활용해 요소를 스왑합니다.
    # (새로운 메모리를 할당하지 않고 내 집 안방을 비워서 작업실로 쓰는 원리)
    for i in range(0, buffer_start - block_size, block_size):
        # 최적화: 이미 정렬되어 있다면 스킵
        if arr[i + block_size - 1] <= arr[i + block_size]:
            continue
            
        # 두 블록(현재 블록과 다음 블록)을 섞기 위해 버퍼 구역과 스왑하며 위치를 맞춤
        # *주의: 이 루프는 블록 스왑의 개념을 보여주는 단순화된 과정입니다.
        left = i
        right = i + block_size
        buf = buffer_start
        
        # 내부 버퍼를 활용해 병합 (요소 밀어내기 없음!)
        for k in range(block_size):
            if arr[left] <= arr[right]:
                swap(arr, left, buf + k)
                left += 1
            else:
                swap(arr, right, buf + k)
                right += 1
                
        # 남은 요소들을 원래 자리로 블록 스왑
        block_swap(arr, i, buf, block_size)

    # 5. 마지막으로, 작업실(버퍼)로 썼던 배열 끝부분만 다시 정렬해 상태를 복구합니다.
    insertion_sort(arr, buffer_start, n - 1)

# 테스트(12개원소)
test_arr = [12, 11, -3, 13, 5, 6, 7, -1, 9, 20, 2, 32]
block_merge_sort(test_arr)
print(f"정렬된 배열: {test_arr}")