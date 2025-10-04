# [SWEA / D4] 3143. 가장 빠른 문자열 타이핑

# import sys
# sys.stdin = open('sample_input.txt')

# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 타이핑할 문자열 sentence, 저장되어 있는 문자열 word
    sentence, word = map(str, input().split())

    # 두 문자열의 길이 N, M
    N = len(sentence)
    M = len(word)

    # 문자열 순회를 위한 인덱스
    index = 0   # 초기화

    # sentence 안에 word가 들어가는 횟수를 담을 변수
    word_count = 0   # 초기화

    # 슬라이딩: 인덱스가 N - M + 1 미만인 동안 sentence 순회
    while index < N - M + 1:

        # word의 길이만큼 잘라낸 문자열 chunk
        chunk = sentence[index:index + M]

        if chunk == word:   # 잘라낸 문자가 word와 동일하다면
            word_count += 1
            index += M  # 다음 탐색은 word의 길이만큼 인덱스를 이동한 후 진행

        else:   # 잘라낸 문자가 word와 동일하지 않다면
            index += 1  # 인덱스 이동

    result = word_count + N - (M * word_count)

    print(f'#{tc} {result}')