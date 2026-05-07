INF = int(1e9 + 7)

# Step 1: 경로를 기록하도록 플로이드-워셜 알고리즘 수정
def floyd_warshall_with_path(W, length):
    # 최단 거리 배열 초기화
    dist = [[W[i][j] for j in range(length)] for i in range(length)]

    # 다음 방문할 정점을 저장할 배열 초기화
    next_v = [[None] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            # 간선이 존재하면 도착점을 다음 방문 노드로 설정
            if dist[i][j] != INF and i != j:
                next_v[i][j] = j

    # Floyd-Warshall 3중 루프
    for r in range(length):
        for p in range(length):
            for q in range(length):
                # HINT 적용: min() 함수 대신 if문을 사용하여 거리가 갱신될 때 경로도 저장
                if dist[p][q] > dist[p][r] + dist[r][q]:
                    dist[p][q] = dist[p][r] + dist[r][q]
                    # p에서 q로 갈 때, 우선 p에서 r로 가는 방향으로 출발해야 함
                    next_v[p][q] = next_v[p][r]

    return dist, next_v

# 경로 추적 및 출력 함수
def print_shortest_path(vs, vd, next_v):
    if next_v[vs][vd] is None:
        print(f"(v{vs}, v{vd}) 경로가 존재하지 않습니다.")
        return

    path = [vs]
    curr = vs
    while curr != vd:
        curr = next_v[curr][vd]
        path.append(curr)

    # 결과 포맷팅하여 출력
    path_formatted = " -> ".join([f"v{node}" for node in path])
    print(f"(v{vs}, v{vd}) 의 최단 경로 정점들: {path_formatted}")


# Step 2: 주어진 입력 W 적용
W = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

length = len(W)
dist, next_v = floyd_warshall_with_path(W, length)

print("=== 플로이드-워셜 최단 경로 추적 결과 ===")
# Step 3: (v1, v3) 와 (v0, v2) 최단 경로 출력
print_shortest_path(1, 3, next_v)
print_shortest_path(0, 2, next_v)