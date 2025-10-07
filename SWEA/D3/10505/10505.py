# [SWEA / D3] 10505. 소득 불균형

# import sys
# sys.stdin = open('input.txt')

# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 사람의 수 N
    N = int(input())

    # 각 사람의 소득
    earnings = list(map(int, input().split()))

    # 국가의 평균 소득
    average = sum(earnings) / N

    count = 0

    # 각 사람의 소득 목록을 순회하며
    for person in earnings:
        # 평균 이하의 소득을 가진 사람의 수를 셈
        if person <= average:
            count += 1
    
    print(f'#{tc} {count}')