def min_postage_stamps_dp(target, stamp_denominations):
    # dp[i]: i 금액을 맞추기 위해 필요한 최소 우표 개수
    # 초기값은 무한대(float('inf'))로 설정, dp[0]은 0
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    
    # 역추적을 위한 배열: 해당 금액을 만들 때 마지막으로 추가된 우표를 기록
    first_stamp_used = [0] * (target + 1)
    
    # 1원부터 target 금액까지 차례대로 최소 개수를 계산 (Bottom-Up)
    for current_amount in range(1, target + 1):
        for stamp in stamp_denominations:
            # 현재 우표 액면가가 맞춰야 할 금액보다 작거나 같고,
            # 이 우표를 사용했을 때 기존에 기록된 최소 개수보다 더 적다면 업데이트
            if current_amount >= stamp and dp[current_amount - stamp] + 1 < dp[current_amount]:
                dp[current_amount] = dp[current_amount - stamp] + 1
                first_stamp_used[current_amount] = stamp
                
    # 목표 금액을 만들 수 없는 경우
    if dp[target] == float('inf'):
        return -1, {}

    # 사용된 우표 내역 역추적 (Backtracking)
    stamps_used = {}
    current = target
    while current > 0:
        stamp = first_stamp_used[current]
        stamps_used[stamp] = stamps_used.get(stamp, 0) + 1
        current -= stamp
        
    return dp[target], stamps_used

# 테스트 실행
stamps = [1500, 1225, 350, 100, 70, 34, 21, 10, 1]
target_cost = 140

count, breakdown = min_postage_stamps_dp(target_cost, stamps)
print(f"최소 우표 개수 (DP): {count}")
print(f"사용된 우표 내역 (DP): {breakdown}")