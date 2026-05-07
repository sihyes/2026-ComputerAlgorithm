def find_minimum_stamps(target, stamps):
    # dp[i]는 금액 i를 만들기 위해 필요한 최소 우표 개수
    # 초기값은 무한대(float('inf'))로 설정
    dp = [float('inf')] * (target + 1)
    
    # 각 금액을 만들 때 마지막으로 사용한 우표의 액면가를 저장하는 배열 (역추적 용도)
    used_stamp = [-1] * (target + 1)
    
    # 0원을 만드는 데 필요한 우표는 0개
    dp[0] = 0
    
    # 1센트부터 목표 금액(target)까지 반복하며 최소 우표 개수 계산
    for i in range(1, target + 1):
        for stamp in stamps:
            # 현재 금액(i)이 우표의 액면가보다 크거나 같을 때만 갱신 가능
            if i >= stamp:
                # 기존에 알려진 최소 개수보다, 현재 우표를 사용했을 때의 개수가 더 적다면 갱신
                if dp[i - stamp] + 1 < dp[i]:
                    dp[i] = dp[i - stamp] + 1
                    used_stamp[i] = stamp  # 사용한 우표 기록


    for i in range(1, target + 1):  # 1부터 140까지 모든 경우에서 DP 테이블 출력

        # 목표 금액을 만들 수 없는 경우 (이 문제에서는 1센트가 있어 발생하지 않음)
        if dp[target] == float('inf'):
            print(f"{i:>4} cents | 만들 수 없음")  # 각 경우의 DP 테이블 출력
            continue
            
        # 역추적하여 어떤 우표들을 사용했는지 확인
        result_stamps = []
        current_amount = i
        while current_amount > 0:
            stamp = used_stamp[current_amount]
            result_stamps.append(stamp)
            current_amount -= stamp

        print(f"{i:>4} cents | {dp[i]:>6}개 | {result_stamps}")  # 각 경우의 DP 테이블 출력
            
    
    return dp[target], result_stamps
    

# 주어진 조건
target_amount = 140
available_stamps = [1, 10, 21, 34, 70, 100, 350, 1225, 1500]

# 함수 실행
min_count, stamps_used = find_minimum_stamps(target_amount, available_stamps)

# 결과 출력
print(f"목표 금액: {target_amount}센트")
print(f"필요한 최소 우표 개수: {min_count}개")
print(f"사용된 우표 조합: {stamps_used}")