# [SWEA / D3] 4406. 모음이 보이지 않는 사람

# import sys
# sys.stdin = open('1_input_sample.txt')

# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 주어진 단어
    word = input()

    # 알파벳의 모음을 담은 리스트
    vowel = ['a', 'e', 'i', 'o', 'u']

    # 자음을 담을 빈 문자열
    invisible = ''

    # 주어진 단어를 순회하며 자음만을 찾아낸다
    for char in word:
        if char not in vowel:
            invisible += char
    
    print(f'#{tc} {invisible}')