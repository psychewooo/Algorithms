# [SWEA / D3] 3142. 영준이와 신비한 뿔의 숲
# 2. for문 활용 풀이

# import sys
# sys.stdin = open('sample_input.txt')

# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 뿔의 수 N, 짐승의 수 M
    N, M = map(int, input().split())

    # 유니콘의 수 i
    # 트윈혼의 수 M - i
    for unicorn in range(M + 1):
        twin_horn = M - unicorn

        if N == unicorn + (M - unicorn) * 2:
            print(f'#{tc} {unicorn} {twin_horn}')
            # 탐색 중단
            # 해당 문제의 경우 break 유무가 실행 시간을 크게 단축시키지는 않음 (5 ms 차이)
            break