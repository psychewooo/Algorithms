# [SWEA / D4] 5247. 연산

# import sys
from collections import deque
# sys.stdin = open('sample_input.txt')

# 사용할 수 있는 연산
calculation = [
    lambda x: x + 1,
    lambda x: x - 1,
    lambda x: x * 2,
    lambda x: x - 10
]


def bfs(N, M):
    """
    너비 우선 탐색을 통하여
    자연수 N을 최소한의 연산을 통해 M으로 만들 때
    연산의 횟수를 반환하는 함수
    """

    # 시작 지점의 숫자, 연산의 횟수
    q = deque([(N, 0)])

    # 중복 방문 체크 (기존에 계산한 숫자인가?)
    # 1 이상 1,000,000 이하의 숫자
    visited = [False] * 1000001

    # 시작 지점 방문 처리
    visited[N] = True

    while q:
        number, calculate_cnt = q.popleft()

        # 종료 조건
        if number == M:
            return calculate_cnt

        for cal in calculation:
            next_number = cal(number)

            if 1 <= next_number <= 1000000:
                if not visited[next_number]:
                    visited[next_number] = True
                    q.append((next_number, calculate_cnt + 1))


# 테스트 케이스의 개수 T
T = int(input())

for tc in range(1, T + 1):
    # 자연수 N, 연산을 통해 만드는 다른 자연수 M
    N, M = map(int, input().split())

    print(f'#{tc} {bfs(N, M)}')