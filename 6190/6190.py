# [SWEA / D3] 6190. 정곤이의 단조 증가하는 수

# import sys
# sys.stdin = open('s_input.txt')


# 함수 정의
def monotonic(number):
    """
    입력한 숫자가 단조 증가하는 수임을 판별하는 함수
    :param number: 양의 정수
    """

    # type 'int'는 길이를 가질 수 없으므로, type 'str'으로 변환한다
    str_num = str(number)

    # 한 자릿수 숫자의 경우 단조 증가하는 수
    if len(str_num) == 1:
        return number

    else:
        for i in range(len(str_num) - 1):
            # 단조 조건을 만족하지 못하는 경우가 있다면 즉시 종료
            if str_num[i] > str_num[i + 1]:
                # 조건: 단조 증가하는 수가 없다면 -1 출력
                return -1

        # 반복문이 끝날 동안 종료되지 않았다면 단조라는 의미이므로 숫자 반환
        # 결과 출력은 다시 int로 한 것은 이후에 max 계산을 쉽게 하기 위함
        return number


# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 양의 정수의 개수 N
    N = int(input())

    # N개의 정수 목록
    numbers = list(map(int, input().split()))

    # 1. 정수 두 개의 곱을 단조 여부를 판별한 후 담을 빈 리스트
    multiple_lst = []

    # 2. N개의 양의 정수 중 두 개를 골라서 곱한다
    # 두 개이니까 for문을 통하여 조합 구현
    for i in range(N):
        for j in range(i + 1, N):
            multiple_num = numbers[i] * numbers[j]
            multiple_lst.append(monotonic(multiple_num))

    # 리스트 내의 최댓값 구하기
    print(f'#{tc} {max(multiple_lst)}')