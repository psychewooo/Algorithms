# [SWEA / D2] 1946. 간단한 압축 풀기

# import sys
# sys.stdin = open('input.txt')

# 테스트 케이스의 개수 T
T = int(input())

for tc in range(1, T + 1):
    # 주어진 알파벳과 숫자 쌍의 개수 N
    N = int(input())

    # 압축을 풀었을 때의 내용을 담을 빈 리스트
    arr = []

    for _ in range(N):
        # 주어진 알파벳 Ci, 알파벳의 연속된 개수 Ki
        Ci, Ki = input().split()
        arr.append(Ci * int(Ki))

    document = ''.join(arr)

    # 형식에 맞게 출력
    print(f'#{tc}')
    for i in range(0, len(document), 10):
        print(document[i:i + 10])