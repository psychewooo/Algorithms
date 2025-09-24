# [SWEA / D3] 3142. 영준이와 신비한 뿔의 숲
# 3. DFS 풀이 (제한시간 초과)

# import sys
# sys.stdin = open('sample_input.txt')


def dfs(unicorn, twin_horn, N, M):
    """
    깊이 우선 탐색을 통해
    영준이가 본 유니콘의 수와 트윈혼의 수를 반환하는 함수
    """

    # 종료 조건
    if M == unicorn + twin_horn:
        if N == unicorn + twin_horn * 2:
            return unicorn, twin_horn
        return None

    # 탐색
    # 유니콘의 수 증가
    result = dfs(unicorn + 1, twin_horn, N, M)
    if result:
        return result

		# 트윈혼의 수 증가
    result = dfs(unicorn, twin_horn + 1, N, M)
    if result:
        return result


# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 뿔의 수 N, 짐승의 수 M
    N, M = map(int, input().split())

    # DFS 탐색 시작
    # 유니콘의 수, 트윈혼의 수, 뿔의 수, 짐승의 수
    result = dfs(0, 0, N, M)

    if result:
        unicorn_num, twin_horn_num = result
        print(f'#{tc} {unicorn_num} {twin_horn_num}')