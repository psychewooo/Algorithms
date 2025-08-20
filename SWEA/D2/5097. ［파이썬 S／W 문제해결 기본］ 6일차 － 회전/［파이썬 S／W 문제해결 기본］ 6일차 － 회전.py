# 테스트 케이스 개수 T
T = int(input())

from collections import deque

for test_case in range(1, T + 1):
    # N개의 숫자로 이루어진 수열, 맨 앞의 숫자를 맨 뒤로 보내는 작업의 횟수 M
    N, M = map(int, input().split())
    # N개의 자연수 목록
    num = list(map(int, input().split()))

    # deque 객체 rotation 생성
    rotation = deque(num)

    # M번 동안 맨 앞의 숫자를 맨 뒤로 보내기
    # popleft()는 맨 앞의 숫자를 반환, 제거하므로
    # 그 값을 받아 맨 뒤로 append()한다

    # N <= M 이므로
    # M % N만큼만 반복하면 됨
    for _ in range(M % N):
        rotation.append(rotation.popleft())

    print(f'#{test_case} {rotation[0]}')