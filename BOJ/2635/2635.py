# [BAEKJOON / SILVER5] 2635. 수 이어가기

# import sys
# sys.stdin = open('input.txt')

# 주어진 첫 번째 양의 정수 N
N = int(input())

# 최대 개수의 수들을 담을 빈 리스트
result = []

# 규칙에 따라 만들 수 있는 수들의 최대 개수
# 숫자를 리스트에 담을 것이므로 수들의 최대 개수는 곧 리스트의 길이
max_length = 0


# 두 번째로 올 수 있는 숫자 탐색
for second in range(1, N + 1):
    numbers = [N]   # N을 첫 번째 값으로 가지는 리스트 numbers
    numbers.append(second)  # 두 번째 숫자 추가

    # 다음 숫자는 앞의 앞의 수에서 앞의 수를 뺀 것이므로, 인덱스 활용
    while numbers[-2] - numbers[-1] >= 0:
        next_number = numbers[-2] - numbers[-1]
        numbers.append(next_number)

    if max_length < len(numbers):
        max_length = len(numbers)   # 최댓값 갱신
        result = numbers    # 가장 긴 수열을 찾았을 때 result를 해당 수열로 업데이트

print(max_length)
print(*result)