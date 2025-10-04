# [SWEA / D3] 6485. 삼성시의 버스 노선

# import sys
# sys.stdin = open('s_input.txt')

# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 버스 노선의 개수
    N = int(input())

    # 정류장을 지나는 버스의 수를 기록할 빈 딕셔너리 생성
    route = {}

    # 번호가 붙여진 5,000개의 버스 정류장 생성
    for i in range(1, 5001):
        route[i] = 0

    # start 부터 end 까지 다니는 버스 노선 N개
    for _ in range(N):
        start, end = map(int, input().split())

        # 정류장을 지나는 버스의 수 기록하기
        for j in range(start, end + 1):
            route[j] += 1

    # 버스 정류장의 수 P
    P = int(input())

    # Cj번 버스 정류장을 지나는 버스 노선의 개수를 담을 빈 리스트 생성
    result = []

    for _ in range(P):
        result.append(route[int(input())])

    # 형식에 맞게 출력
    print(f'#{tc}', *result)