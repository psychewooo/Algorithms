# [SWEA / D3] 3431. 준환이의 운동관리

# import sys
# sys.stdin = open('sample_input.txt')


def limit(min, max, do):
    """
    일주일에 min분 이상 max분 이하의 운동을 하여야 할 때
    시간 제한과 운동 시간을 비교하여 결과를 반환하는 함수
    """

    # 1. 필요한 양보다 운동을 덜 하였을 경우
    if do < min:
        return min - do

    # 2. 제한된 운동 시간을 충족할 경우
    elif min <= do <= max:
        return 0

    # 3. 필요한 양보다 더 많은 운동을 하고 있을 경우
    elif do > max:
        return -1


# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 최소 운동 시간 L분, 최대 운동 시간 U분, 이번 주 운동 시간 X분
    L, U, X = map(int, input().split())

    print(f'#{tc} {limit(L, U, X)}')