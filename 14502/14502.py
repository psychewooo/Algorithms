# import sys
# sys.stdin = open('input.txt')

import copy
from collections import deque

# 지도의 세로 크기 N, 가로 크기 M
N, M = list(map(int, input().split()))

# 지도의 모양 map
map = [list(map(int, input().split())) for _ in range(N)]


# 안전 영역 크기의 최댓값 초기화
max_safe_area = 0

# 1. 지도를 순회하며 빈 칸 (0) 찾기
# 빈 칸의 정보를 담을 빈 리스트 생성
spot_zero = []

# 바이러스의 정보를 담을 빈 리스트 생성
spot_virus = []

for r in range(N):
    for c in range(M):
        if map[r][c] == 0:
            spot_zero.append((r, c))
        elif map[r][c] == 2:
            spot_virus.append((r, c))


# 2. 벽 생성
# 0으로 가득 찬 공간 중 3개를 뽑아 벽을 세운다

# itertools 사용 못한다고 하여 for문을 통한 조합 구현
for i in range(len(spot_zero)):
    for j in range(i + 1, len(spot_zero)):
        for k in range(j + 1, len(spot_zero)):

            first_wall = spot_zero[i]
            second_wall = spot_zero[j]
            third_wall = spot_zero[k]

            # deepcopy를 통한 지도 복사
            current_map = copy.deepcopy(map)

            # 현재 지도에 벽 생성
            current_map[first_wall[0]][first_wall[1]] = 1
            current_map[second_wall[0]][second_wall[1]] = 1
            current_map[third_wall[0]][third_wall[1]] = 1


            # 3. 바이러스 확산
            # 델타 정의 - 상하좌우
            dr = [-1, 1, 0, 0]      # 행
            dc = [0, 0, -1, 1]      # 열

            q = deque(spot_virus)

            while q:
                r, c = q.popleft()

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < N and 0 <= nc < M and current_map[nr][nc] == 0:
                        current_map[nr][nc] = 2
                        q.append((nr, nc))


            # 4. 바이러스 확산 후 안전 영역 세기
            # 현재 순회 중인 곳의 안전 영역 크기 초기화
            safe_area = 0

            for r in range(N):
                for c in range(M):
                    if current_map[r][c] == 0:
                        safe_area += 1

            # 5. 안전 영역 크기의 최댓값 갱신
            if max_safe_area < safe_area:
                max_safe_area = safe_area

print(max_safe_area)