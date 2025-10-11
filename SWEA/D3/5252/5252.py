# [SWEA / D3] 5252. [파이썬 S/W 문제해결 최적화] 1일차 - 공통 단어 검색

# import sys
# sys.stdin = open('sample_input.txt')

# 테스트 케이스의 개수 T
T = int(input())

for tc in range(1, T + 1):
    # A의 단어 개수 N, B의 단어 개수 M
    N, M = map(int, input().split())

    # A가 만든 영어 단어장
    list_a = []
    for _ in range(N):
        list_a.append(input())

    # B가 만든 영어 단어장
    list_b = []
    for _ in range(M):
        list_b.append(input())
    
    # 공통으로 들어있는 단어의 개수
    count = 0

    # A의 단어장을 순회하면서
    for word in list_a:
        # 동일한 단어가 B의 단어장에도 있으면 개수 증가
        if word in list_b:
            count += 1
    
    print(f'#{tc} {count}')