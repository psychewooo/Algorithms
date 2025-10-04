# [SWEA / D3] 2814. 최장 경로

# import sys
# sys.stdin = open('sample_input.txt')


def dfs(current_node, length, visited):
    """
    깊이 우선 탐색을 통해
    그래프에서의 최장 경로의 길이를 반환하는 함수

    경로의 길이는 경로 상에 등장하는 정점의 개수
    """
    # 글로벌 변수 불러오기
    global max_length

    # 최댓값 갱신
    if max_length < length:
        max_length = length

    for next_node in adj_list[current_node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, length + 1, visited)
            visited[next_node] = False


# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 두 개의 자연수 N, M
    N, M = map(int, input().split())

    # 인접 리스트를 통한 그래프 구현
    adj_list = [[] for _ in range(N + 1)]

    for i in range(M):
        node1, node2 = map(int, input().split())

        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    # 조건: 정점이 하나일 때 경로의 길이는 무조건 1
    max_length = 1

    # 방문 여부를 기록할 리스트 생성
    visited = [False] * (N + 1)

    # 노드 탐색
    # 인덱스를 맞추기 위해 0부터 시작하였으므로 탐색은 1부터 시작
    for node in range(1, N + 1):
        # 방문 처리
        visited[node] = True
        # DFS 시작
        # 현재 노드, 현재 경로의 길이, 방문 여부
        dfs(node, 1, visited)
        visited[node] = False

    print(f'#{tc} {max_length}')