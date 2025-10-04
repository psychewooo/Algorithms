# [SWEA / D3] 3142. 영준이와 신비한 뿔의 숲
# 1. 연립방정식 활용 풀이

# import sys
# sys.stdin = open('sample_input.txt')

# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 뿔의 수 N, 짐승의 수 M
    N, M = map(int, input().split())
		
	# 유니콘의 수 x, 트윈혼의 수 y
	# x + y = M, x + 2y = N
	# x = 2M - N, y = N - M
    print(f'#{tc} {2 * M - N} {N - M}')