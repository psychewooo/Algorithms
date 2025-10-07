# [SWEA / D3] 13218. 조별 과제

# import sys
# sys.stdin = open('sample_input.txt')


def team(num):
    """
    학생들을 조로 나누었을 때,
    3명 이상의 학생으로 구성된 조의 수의 최댓값을 반환하는 함수
    """

    # 학생의 수가 3명 미만이면, 조의 수는 0
    if num < 3:
        return 0

    # 학생의 수가 3명 이상이면, 학생의 수를 3으로 나눈 결과의 몫이 곧 조의 수
    else:
        return num // 3


# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 학생의 수 N
    N = int(input())

    print(f'#{tc} {team(N)}')