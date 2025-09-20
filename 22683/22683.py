# [SWEA / D3] 22683. 나무 베기

# import sys
# from collections import deque
# sys.stdin = open('sample_input.txt')

# 델타 정의 상우하좌 (90도 시계 방향 회전)
dr = [-1, 0, 1, 0]     # 행
dc = [0, 1, 0, -1]     # 열


# BFS 함수 정의
def bfs(start, destination, N, K, field):
    """
    너비 우선 탐색을 통해
    출발지에서 목적지까지 최소 리모컨 조작 횟수를 구하는 함수

    단, 목적지까지 이동시킬 수 없다면 -1을 출력한다
    """

    # X 좌표, Y 좌표, 방향, 조작 횟수, 나무를 벤 횟수
    q = deque([(start[0], start[1], 0, 0, 0)])

    # 방문 기록을 위해 튜플을 저장할 set 생성
    visited = set()

    # 시작 지점과 방향, 나무를 벤 횟수 방문 기록
    visited.add((start[0], start[1], 0, 0))

    while q:
        r, c, direction, count, cut = q.popleft()

        # 종료 조건
        if (r, c) == destination:
            return count

        # 1. 전진
        nr = r + dr[direction]
        nc = c + dc[direction]

        # 벽 체크
        if 0 <= nr < N and 0 <= nc < N:
            # 1-1. 이동 가능한 땅이거나, 도착 지점이라면
            if field[nr][nc] == 'G' or (nr, nc) == destination:
                # 방문 기록을 살펴본 후
                if (nr, nc, direction, cut) not in visited:
                    # 방문 기록 남기기
                    visited.add((nr, nc, direction, cut))
                    q.append((nr, nc, direction, count + 1, cut))

            # 1-2. 나무를 만나면
            elif field[nr][nc] == 'T':
                # 1-3. 그리고 벨 수 있는 횟수가 남아있다면
                    if cut < K:
                        if (nr, nc, direction, cut) not in visited:
                            # 나무를 자른 후 방문 기록 남기기
                            visited.add((nr, nc, direction, cut + 1))
                            q.append((nr, nc, direction, count + 1, cut + 1))

        # 2. 우회전
        n_right = (direction + 1) % 4
        if (r, c, n_right, cut) not in visited:
            visited.add((r, c, n_right, cut))
            q.append((r, c, n_right, count + 1, cut))

        # 3. 좌회전
        n_left = (direction + 3) % 4
        if (r, c, n_left, cut) not in visited:
            visited.add((r, c, n_left, cut))
            q.append((r, c, n_left, count + 1, cut))

    # 조건: 목적지까지 이동시킬 수 없다면 -1을 출력
    return -1


# 테스트 케이스의 개수 T
T = int(input())

for tc in range(1, T + 1):
    # 필드의 크기 N, 나무를 벨 수 있는 횟수 K
    N, K = map(int, input().split())

    # 필드의 정보
    field = [input() for _ in range(N)]

    # 좌표에 존재하지 않는 값으로 초기 설정
    start = (-1, -1)
    destination = (-1, -1)

    # 배열을 탐색하여 현재 RC카의 위치와 이동 시키고자 하는 위치 찾기
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                start = (i, j)

            elif field[i][j] == 'Y':
                destination = (i, j)

    print(f'#{tc} {bfs(start, destination, N, K, field)}')