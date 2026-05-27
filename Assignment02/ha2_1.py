def find_and_print_lis(arr):
    n = len(arr)
    if n == 0:
        return []

    # dp[i] stores the length of the LIS ending at index i
    dp = [1] * n

    # parent[i] stores the index of the previous element in the LIS
    # We use this to reconstruct the actual path
    parent = [-1] * n

    # Build the dp array and track the parents
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j

    # Find the index of the maximum value in dp
    max_len = 0
    max_idx = -1
    for i in range(n):
        if dp[i] > max_len:
            max_len = dp[i]
            max_idx = i

    # Reconstruct the sequence by working backwards
    lis = []
    curr = max_idx
    while curr != -1:
        lis.append(arr[curr])
        curr = parent[curr]

    # The sequence is built backwards, so reverse it
    lis.reverse()

    return max_len, lis

# The input array
arr = [10, 22, 9, 33, 21, 50, 41, 60]

length, sequence = find_and_print_lis(arr)

print(f"Input Array: {arr}")
print(f"Length of LIS: {length}")
print(f"Actual LIS Elements: {sequence}")