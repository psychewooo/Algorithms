# [SWEA / D3] 12368. 24시간

# import sys
# sys.stdin = open('sample_input.txt')


def time(now, later):
    """
    현재 시각 now와 앞으로 지날 시간 later을 입력받아
    later 시간이 지난 후의 시각을 24시간 제로 반환하는 함수
    """
    
    result = now + later

    if result < 24:
        return result
    
    elif result == 24:
        # 조건: 자정을 표기하는 유일한 방법은 '0시'
        return 0

    else:
        return result % 24


# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 현재 시각 A, 앞으로 지날 시간 B
    A, B = map(int, input().split())

    print(f'#{tc} {time(A, B)}')