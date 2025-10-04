# [SWEA / D2] 1984. 중간 평균값 구하기

# import sys
# sys.stdin = open('input.txt')

# 테스트 케이스의 개수 T
T = int(input())

for tc in range(1, T + 1):
    # 입력 받은 10개의 수
    numbers = list(map(int, input().split()))

    # 오름차순 정렬
    numbers.sort()

    # 최대 수와 최소 수를 제외한 나머지 숫자의 합을 담을 변수
    number_sum = 0

    # 최소 수: numbers[0]
    # 최대 수: numbers[9]
    for i in range(1, 9):   # i = 1, 2, ..., 8
        number_sum += numbers[i]

    # 소수점 첫째 자리에서 반올림
    average = round(number_sum / 8)

    print(f'#{tc} {average}')