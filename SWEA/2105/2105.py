# 델타 정의 (4방향 대각선, 우하, 좌하, 좌상, 우상)
dr = [1, 1, -1, -1]     # 행
dc = [1, -1, -1, 1]     # 열


def dfs(start_r, start_c, r, c, direction):
    """
    깊이 우선 탐색을 통해
    디저트를 가장 많이 먹을 수 있는 경로를 찾는 함수

    :param start_r: 시작 위치의 행 좌표
    :param start_c: 시작 위치의 열 좌표
    :param r: 현재 위치의 행 좌표
    :param c: 현재 위치의 열 좌표
    :param direction: 이동 방향
    """
    # 글로벌 변수 불러오기
    global count
    global max_count

    # 현재 위치의 디저트 종류 기록
    visited_dessert.append(dessert[r][c])

    # 디저트 먹은 횟수 증가
    count += 1

    # 델타 탐색
    # 사각형 모양 이동: 지금과 같은 방향으로 움직이거나, 방향 전환
    for i in range(direction, direction + 2):
        if i >= 4:      # 인덱스가 범위를 초과할 경우 (이 조건이 없으면 list index out of range)
            break       # 탐색 종료

        nr = r + dr[i]
        nc = c + dc[i]

        # 다시 출발점으로 돌아오는 조건
        if nr == start_r and nc == start_c:
            max_count = max(max_count, count)
            continue

        # 이동할 위치가 범위 내에 있으며
        if 0 <= nr < N and 0 <= nc < N:
            # 아직 방문하지 않은 곳이고, 디저트의 종류가 중복되지 않으면
            if not visited[nr][nc] and dessert[nr][nc] not in visited_dessert:
                visited[nr][nc] = True
                # 이동할 위치에서 재귀 호출
                dfs(start_r, start_c, nr, nc, i)

                # 다음 탐색을 위해 초기화
                visited[nr][nc] = False

    visited_dessert.pop()
    count -= 1


T = int(input())

for test_case in range(1, T + 1):
    # 디저트 카페가 모여있는 지역의 한 변의 길이 N
    N = int(input())

    # N * N 크기의 디저트 카페에서 팔고 있는 디저트 종류에 대한 정보
    dessert = [list(map(int, input().split())) for _ in range(N)]

    # 방문 여부를 기록할 리스트 생성
    # True: 방문, False: 방문하지 않음
    visited = [[False] * N for _ in range(N)]

    # 방문한 디저트의 종류를 기록하는 빈 리스트 생성 (같은 숫자의 디저트를 팔고 있는 카페는 안 가야하니까!)
    visited_dessert = []

    # 디저트를 먹은 횟수 변수 초기화
    count = 0

    # 가능한 경우 중 디저트를 가장 많이 먹은 경우
    max_count = -1

    for r in range(N):
        for c in range(N):

            # 시작 위치에서 탐색 시작
            # 탐색을 시작하며 방문 기록 변경
            visited[r][c] = True

            # 시작 위치의 좌표, 현재 위치의 좌표, 시작 방향 우하 (똑같아서 헷갈림..)
            dfs(r, c, r, c, 0)

            # 다음 탐색을 위한 초기화
            visited[r][c] = False

    print(f'#{test_case} {max_count}')