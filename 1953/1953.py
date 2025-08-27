import sys
from collections import deque

sys.stdin = open('sample_input.txt')

# 총 테스트 케이스의 개수 T
T = int(input())

# 델타 정의 (상하좌우)
dr = [-1, 1, 0, 0]     # 행
dc = [0, 0, -1, 1]     # 열

# 터널 구조물의 이동 가능 여부 정리 (상하좌우)
structure = {
    1: [1, 1, 1, 1],  # 터널 1
    2: [1, 1, 0, 0],  # 터널 2
    3: [0, 0, 1, 1],  # 터널 3
    4: [1, 0, 0, 1],  # 터널 4
    5: [0, 1, 0, 1],  # 터널 5
    6: [0, 1, 1, 0],  # 터널 6
    7: [1, 0, 1, 0]   # 터널 7
}


# 함수 정의
def find_route(N, M, R, C, L, t_map):
    """
    지하 터널 지도와 맨홀 뚜껑의 위치, 경과된 시간이 주어질 때
    탈주범이 위치할 수 있는 장소의 개수를 계산하는 함수

    N: 지하 터널 지도의 세로 크기
    M: 지하 터널지도의 가로 크기
    R: 맨홀 뚜껑의 세로 위치 (0 <= R <= N-1)
    C: 맨홀 뚜껑의 가로 위치 (0 <= C <= M-1)
    L: 탈출 후 소요된 시간 (1 <= L <= 20)
    t_map: 지하 터널 지도
    """
    
    # deque 객체 생성
    dq = deque([])

    # 시작 지점의 위치 행 좌표, 열 좌표와 탈출 후 소요 시간 추가
    # 탈출한 지 한 시간 뒤 지하 터널에 들어갔으므로 시작 당시 소요 시간 = 1
    dq.append([R, C, 1])

    # 탈주범의 방문 여부를 판단하기 위한 N * M 크기의 빈 2차원 리스트 생성
    # 0: 방문하지 않음
    # 1: 방문
    visited = [[0] * M for _ in range(N)]

    # 시작 당시 한 시간이 소요된 이후이므로, 시작점은 1
    visited[R][C] = 1

    # 탈주범이 위치할 수 있는 장소의 개수 초기화
    count = 0

    # 종료 조건: 더이상 방문할 곳이 없을 때까지 반복
    while dq:
        # dq.append 하였던 현재 위치 정보를 꺼냄
        r, c, time = dq.popleft()

        # 현 위치의 터널 구조물 타입
        structure_type = t_map[r][c]

        # 만약, 시간을 초과할 경우 경로 탐색 종료
        if time > L:
            break

        count += 1

        # 델타 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 이동 위치의 범위 내 존재 여부 판별
            # 이동 위치의 방문 여부 판별
            # 이동 위치의 터널 구조물 존배 여부 판별
            # 셋 중 하나라도 충족할 경우 continue
            if not (0 <= nr < N and 0 <= nc < M) or visited[nr][nc] != 0 or t_map[nr][nc] == 0:
                continue

            # 이동 위치의 터널 구조물 타입
            next_structure_type = t_map[nr][nc]

            # 현재 위치한 터널에서 이동 가능 여부 판별
            can_move = structure[structure_type][i]

            # 터널 구조물의 연결 여부 판별
            if i == 0:                                              # 위로 이동할 경우
                next_tunnel = structure[next_structure_type][1]     # 이동 위치 구조물의 아래가 뚫려 있어야 함
            elif i == 1:                                            # 아래로 이동할 경우
                next_tunnel = structure[next_structure_type][0]     # 이동 위치 구조물의 위가 뚫려 있어야 함
            elif i == 2:                                            # 왼쪽으로 이동할 경우
                next_tunnel = structure[next_structure_type][3]     # 이동 위치 구조물의 오른쪽이 뚫려 있어야 함
            else:                                                   # 오른쪽으로 이동할 경우
                next_tunnel = structure[next_structure_type][2]     # 이동 위치 구조물의 왼쪽이 뚫려 있어야 함

            # 터널 구조물이 연결되어 있고, 이동 가능하다면
            if can_move and next_tunnel:
                # 방문 시간 증가
                visited[nr][nc] = time + 1
                # 이동한 위치를 큐에 추가 후 탐색 반복
                dq.append([nr, nc, time + 1])

    return count



for test_case in range(1, T + 1):
    # 지하 터널 지도의 세로 크기 N, 가로 크기 M, 세로 위치 R, 가로 위치 C, 소요 시간 L
    N, M, R, C, L = map(int, input().split())

    # 지하 터널 지도 정보
    tunnel_map = [list(map(int, input().split())) for _ in range(N)]

    result = find_route(N, M, R, C, L, tunnel_map)

    print(f'#{test_case} {result}')
