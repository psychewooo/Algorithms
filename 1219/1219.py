# [SWEA / D4] 1219. 길 찾기

# import sys
# sys.stdin = open('input.txt')


# 함수 정의
def is_dfs(current_position, adj_list, visited):
    if current_position == 99:
        return True

    # 현재 위치는 방문 처리
    visited[current_position] = True

    # 인접 위치 순회하기
    for next_position in adj_list[current_position]:
        if not visited[next_position]:
            if is_dfs(next_position, adj_list, visited):
                # 정점에 도착할 수 있는 경우 결과 1
                return True

    return False


# 총 10개의 테스트 케이스
for _ in range(1, 11):
    # 테스트 케이스의 번호 tc, 길의 총 개수 V
    # 길의 총 개수는 곧 그래프 정점의 개수
    tc, V = map(int, input().split())

    # 순서쌍
    arr = list(map(int, input().split()))

    # 간선의 수 E
    E = len(arr) // 2

    # 인접 리스트 생성
    # 정점의 개수는 최대 100개이므로, 최대 범위 내에서 생성
    adj_list = [[] for _ in range(100)]

    for i in range(E):
        node1, node2 = arr[2 * i], arr[2 * i + 1]
        adj_list[node1].append(node2)

    # 방문 기록을 위한 리스트 생성
    visited = [False] * (100)

    # 출발점에서 깊이 우선 탐색 시작
    if is_dfs(0, adj_list, visited):
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)